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


if __name__ == "__main__":
    cli()



