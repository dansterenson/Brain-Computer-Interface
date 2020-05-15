import os
import click
from Noesis.client import upload_snapshot
from Noesis.server import run_server
from Noesis.web import run_webserver
from Noesis.reader import Reader


@click.group()
def cli():
    pass


@cli.group('server')
def server():
    pass


@cli.group('client')
def client():
    pass


@cli.group('web')
def web():
    pass


cur_path = os.path.dirname(__file__)
good = 'sample.mind'
good1 = os.path.join(cur_path, 'tmp_server')
good2 = os.path.join(cur_path, good)


@server.command()
@click.option('--address', default='127.0.0.1:1234')
@click.option('--data_dir', default=good1)
def run(address, data_dir):
    try:

        run_server(address, data_dir)
    except Exception as e:
        print(f'ERROR: {e}')
        return 1


@client.command()
@click.option('--address', default='127.0.0.1:1234')
@click.option('--file_path', default=good2)
def upload(address, file_path, ver):
    if ver == 'v1':
        reader_ver = BinReader
    elif ver == 'v2':
        reader_ver = ProtoReader
    else:
        raise Exception('Version format is not supported')

    with Reader(file_path, reader_ver) as reader:
        upload_snapshot(address, reader)


@web.command()
@click.argument('address')
@click.argument('data_dir')
def run_web(address, data_dir):
    run_webserver(address, data_dir)


if __name__ == "__main__":

    cli()






