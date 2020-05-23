import json
import click
import sys
import ntpath
from ..msg_queue import MessageQueue
from .parser_manager import run_parser
from .utils.logger import create_logger

logger = create_logger("parser")


@click.group()
def cli():
    pass


@cli.command('parse')
@click.argument('parser_name')
@click.argument('path_to_data')
def parse_cmd(parser_name, path_to_data):
    with open(path_to_data) as f:
        data = json.load(f)

    try:
        parser_result = run_parser(parser_name, data)

    except NameError as e:
        print(f'ERROR: parser error: {e}.')
        sys.exit(1)
    print(f"From '{ntpath.basename(f.name)}' parsed {parser_name}.")
    print(f'Parser result:\n{parser_result}')


@cli.command('run-parser')
@click.argument('parser_name')
@click.argument('message_queue_url')#, default="rabbitmq://127.0.0.1:5672/")
def run_parser_cmd(parser_name, message_queue_url):
    print(message_queue_url)
    message_queue = MessageQueue(message_queue_url)
    message_queue.exchange_declaration("snapshots")
    message_queue.queue_declaration(parser_name)
    message_queue.queue_binding(parser_name, 'snapshots')

    def callback_func(ch, method, properties, body):
        logger.info(f'parser manager got a snapshot from mq')
        data = json.loads(body)
        parsed_result = run_parser(parser_name, data)
        parser_exchange_name = "parsed_" + parser_name
        message_queue.exchange_declaration(parser_exchange_name)
        message_queue.queue_publish(parser_exchange_name, '', json.dumps(parsed_result))
        logger.info(f'{parser_name} parser saved parsed data to parser_{parser_name} exchange in mq')

    message_queue.consume_from_queue(parser_name, callback_func)
    logger.info(f'parser is listening on mq')
    message_queue.start_consuming()


if __name__ == '__main__':
    cli()
