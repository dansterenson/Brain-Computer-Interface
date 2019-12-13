import click
from . import client
from . import server
from . import web


@click.group()
def cli():
    pass

@click.command()
@click.argument('address')
@click.argument('user', type=int)
@click.argument('thought')
def upload_thought(address, user, thought):
    try:
        client.upload_thought(address, int(user), thought)
    except Exception as e:
        print (f'ERROR: {e}')
        return 1


@click.command()
@click.argument('address')
@click.argument('data')
def run(address, data):
    try:
        server.run(address, data)
    except Exception as e:
        print(f'ERROR: {e}')
        return 1


@click.command()
@click.argument('address')
@click.argument('data_dir')
def run(address, data):
    web.run_webserver(address, data)


if __name__ == "__main__":
    cli()



