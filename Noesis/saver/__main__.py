import json
import sys
import ntpath
import click
from ..msg_queue import MessageQueue
from .saver import Saver
from ..parsers import Parser
from .utils.logger import create_logger

logger = create_logger("saver")


@click.group()
def cli():
    pass


@cli.command('save')
@click.option('-d', '--database', default='mongodb://localhost:27017')
@click.argument('topic_name')
@click.argument('data_path')
def save_cmd(database, topic_name, data_path):
    parser_mng = Parser()
    available_parsers = parser_mng.supported_parsers

    if topic_name not in available_parsers:
        print(f'Topic name {topic_name} is not valid, available parsers: {available_parsers.keys()}')
        return
    saver = Saver(database)
    with open(data_path) as f:
        data = json.load(f)
        try:
            saver.save(topic_name, data)

        except NameError as e:
            print(f'ERROR: saver error: {e}.')
            sys.exit(1)
        print(f"From '{ntpath.basename(f.name)}' successfully saved {topic_name}.")


@cli.command('run-saver')
@click.argument('database', default='mongodb://localhost:27017')
@click.argument('mq_url', default="rabbitmq://127.0.0.1:5672/")
def run_save_cmd(database, mq_url):
    saver = Saver(database)
    mq = MessageQueue(mq_url)
    parser_mng = Parser()
    supported_parsers = parser_mng.supported_parsers

    def callback(ch, method, properties, body):
        data = json.loads(body)
        topic_name = data['result_name']
        saver.save(topic_name, data)

    for parser in supported_parsers:
        exchange_name = "parsed_" + parser
        mq.exchange_declaration(exchange_name)
        res = mq.queue_declaration('')
        mq.queue_binding(res.method.queue, exchange_name)
        mq.consume_from_queue(res.method.queue, callback)

    logger.debug(f'Saver is listening on mq')
    mq.start_consuming()


if __name__ == '__main__':
    cli()
