import json
import click
from Haruspex.server.msg_queue import MessageQueue
from .saver import Saver
from Haruspex.parsers import get_parser_dict

@click.group()
def cli():
    pass

@cli.command('save')
@click.option('--database', '-d', default='mongodb://localhost:27017')
@click.argument('topic_name')
@click.argument('data_path')
def save_cmd(database, topic_name, data_path):
    parsers = get_parser_dict()
    if topic_name not in parsers:
        print (f'Topic name {topic_name} is not valid, available parsers: {parsers}')
        return
    saver = Saver(database)
    with open(data_path, 'r') as file:
        data_from_file = file.read()
        saver.save(data_from_file, topic_name)


@cli.command('run-saver')
@click.argument('database', default='mongodb://localhost:27017')
@click.argument('mq_url', default="rabbitmq://127.0.0.1:5672/")
def run_save_cmd(database, mq_url):
    parsers = ['color_image', 'depth_image', 'feelings', 'pose']
    saver = Saver(database)
    mq = MessageQueue(mq_url)

    def callback(ch, method, properties, body):
        saver.save(body)

    for parser in parsers:
        exchange_name = parser + '_parsed'
        mq.exchange_declaration(exchange_name)
        res = mq.queue_declaration('')
        mq.queue_binding(res.method.queue, exchange_name)
        mq.consume_from_queue(res.method.queue, callback)

    mq.start_consuming()




if __name__ == '__main__':
    cli()
