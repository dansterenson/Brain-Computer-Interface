import click
from . import upload_thought
from . import run_server
from . import run_webserver


@click.group()
def cli():
    pass


@cli.command()
@click.argument('address')
@click.argument('user', type=int)
@click.argument('thought')
def upload(address, user_id, thought):
    try:
        upload_thought(address, int(user_id), thought)
    except Exception as e:
        print(f'ERROR: {e}')
        return 1


@cli.command()
@click.argument('address')
@click.argument('data_dir')
def run(address, data_dir):
    try:
        run_server(address, data_dir)
    except Exception as e:
        print(f'ERROR: {e}')
        return 1


@cli.command()
@click.argument('address')
@click.argument('data_dir')
def run_web(address, data_dir):
    run_webserver(address, data_dir)


if __name__ == "__main__":
    cli()



