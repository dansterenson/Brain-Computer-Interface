import click
import sys
from .gui import run_server

@click.group()
def cli():
    pass


@cli.command('run-server')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8080)
@click.option('-H', '--api-host', default='127.0.0.1')
@click.option('-P', '--api-port', default=5000)
def get_result(host, port, api_host, api_port):
    """Runs the gui-server on given ddress and display data from api"""
    try:
        run_server(host, port, api_host, api_port)
    except Exception as e:
        print(f"ERROR: failed running gui: {e}")
        sys.exit(1)


if __name__ == '__main__':
    cli()
