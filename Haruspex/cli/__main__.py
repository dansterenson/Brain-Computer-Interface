import click
import json
from requests import get

@click.group()
def cli():
    pass


@cli.command('get-users')
@click.option('--host', '-h', default='127.0.0.1')
@click.option('--port', '-p', default=5000)
def get_users(host, port):
    res = get(f'http://{host}:{port}/users').json()
    print(res)


@cli.command('get-user')
@click.option('--host', '-h', default='127.0.0.1')
@click.option('--port', '-p', default=5000)
@click.argument('user_id')
def get_user(host, port, user_id):
    res = get(f'http://{host}:{port}/users/{user_id}').json()
    print(res)


@cli.command('get-snapshots')
@click.option('--host', '-h', default='127.0.0.1')
@click.option('--port', '-p', default=5000)
@click.argument('user_id')
def get_snapshots(host, port, user_id):
    res = get(f'http://{host}:{port}/users/{user_id}/snapshots').json()
    print(res)


@cli.command('get-snapshot')
@click.option('--host', '-h', default='127.0.0.1')
@click.option('--port', '-p', default=5000)
@click.argument('user_id')
@click.argument('snapshot_id')
def get_snapshot(host, port, user_id, snapshot_id):
    res = get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}').json()
    print(res)


@cli.command('get-result')
@click.option('--host', '-h', default='127.0.0.1')
@click.option('--port', '-p', default=5000)
@click.option('--save', '-s', default=None)
@click.argument('user_id')
@click.argument('snapshot_id')
@click.argument('result')
def get_result(host, port, save, user_id, snapshot_id, result):
    res = get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result}').json()
    if save is not None:
        with open(save, 'w+') as f:
            f.write(get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result}/data').json())
    else:
        print(res)


if __name__ == '__main__':
    cli()