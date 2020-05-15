import click
from . import run_api_server
import sys

@click.group()
def cli():
    pass


@cli.command('run-server')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=5000)
@click.option('-d', '--database', default='mongodb://localhost:27017')
def run_api_cmd(host, port, database):
    """ Runs the api-server on the and loads data from data base"""
    try:
        run_api_server(host, port, database)
    except Exception as e:
        print(f"ERROR: Api server error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    cli()
