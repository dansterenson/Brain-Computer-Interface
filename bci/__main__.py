import click
from . import upload
from . import run_webserver
from . import run


@click.group()
def cli():
    pass


cli.add_command(upload)
cli.add_command(run_webserver)
cli.add_command(run)

if __name__ == "__main__":
    cli()



