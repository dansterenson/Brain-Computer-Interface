import click
import sys
import logging
from .client import upload_sample


@click.group()
def cli():
    pass


@cli.command('upload-sample')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8000)
@click.argument('file_path')
def upload_sample_cmd(host, port, file_path):
    """ reads a sample from a given path and sends it to a server """
    try:
        upload_sample((host, port), file_path)
    except Exception as e:
        print(f'ERROR: uploading sample failed: {e}')
        sys.exit(1)


if __name__ == '__main__':
    cli()
