import os
import sys

import click
from Haruspex.client import upload_snapshot
from Haruspex.server import run_server
from Haruspex.web import run_webserver
from Haruspex.reader import Reader


@click.group()
def cli():
    pass


cur_path = os.path.dirname(__file__)
good = 'sample.mind'
good1 = os.path.join(cur_path, 'tmp_server')
good2 = os.path.join(cur_path, good)


@cli.command()
@click.option('--address', default='127.0.0.1:1234')
@click.option('--data_dir', default=good1)
def run(address, data_dir):
    try:
        run_server(address, data_dir)
    except Exception as e:
        print(f'ERROR: {e}')
        return 1


@cli.command()
@click.option('--address', default='127.0.0.1:1234')
@click.option('--file_path', default=good2)
def upload(address, file_path):
    with Reader(file_path) as reader:
        upload_snapshot(address, reader)



@cli.command()
@click.argument('address')
@click.argument('data_dir')
def run_web(address, data_dir):
    run_webserver(address, data_dir)


if __name__ == "__main__":
    run()





