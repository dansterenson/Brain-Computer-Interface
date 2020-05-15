import click
import sys
from .server import run_server
from ..msg_queue import MessageQueue


@click.group()
def cli():
    pass


@cli.command('run-server')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8000)
@click.argument('mq_url', default="rabbitmq://127.0.0.1:5672/")
def run_server_cmd(host, port, mq_url):
    """gets uploaded messages from clients and saves them to mq """

    def publish_function(message_to_publish):
        mq = MessageQueue(mq_url)
        mq.exchange_declaration('snapshots')
        mq.queue_publish('snapshots', '', message_to_publish)
        mq.close()

    try:
        run_server(host, port, publish_function)

    except Exception as e:
        print(f'ERROR: running server failed failed: {e}')
        sys.exit(1)


if __name__ == '__main__':
    cli()
