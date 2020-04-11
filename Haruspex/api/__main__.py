import click
from . import run_api_server


@click.group()
def cli():
    pass


@cli.command('run-server')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=5000)
@click.option('-d', '--database', default='mongodb://localhost:27017')
def run_api_cmd(host, port, database):
    run_api_server(host, port, database)


if __name__ == '__main__':
    cli()
