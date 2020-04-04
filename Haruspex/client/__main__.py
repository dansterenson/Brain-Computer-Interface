import click
from .client import upload_sample


@click.group()
def cli():
    pass


@cli.command('upload-sample')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=8000)
@click.argument('file_path')
def upload_sample_cmd(host, port, file_path):
    upload_sample((host, port), file_path)


if __name__ == '__main__':
    cli()
