import json

import click
import sys
from requests import get
from shutil import copyfile

@click.group()
def cli():
    pass


@cli.command('get-users')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=5000)
def get_users(host, port):
    """Returns a list of all users"""
    try:
        res = get(f'http://{host}:{port}/users')
        print(res.text)
    except Exception as e:
        print(f"ERROR: failed fetching data from api: {e}")
        sys.exit(1)


@cli.command('get-user')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=5000)
@click.argument('user_id')
def get_user(host, port, user_id):
    """Returns details of a given user"""
    try:
        res = get(f'http://{host}:{port}/users/{user_id}')
        print(res.text)
    except Exception as e:
        print(f"ERROR: failed fetching data from api: {e}")
        sys.exit(1)


@cli.command('get-snapshots')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=5000)
@click.argument('user_id')
def get_snapshots(host, port, user_id):
    """Returns a list of user's snapshots"""
    try:
        res = get(f'http://{host}:{port}/users/{user_id}/snapshots')
        print(res.text)
    except Exception as e:
        print(f"ERROR: failed fetching data from api: {e}")
        sys.exit(1)


@cli.command('get-snapshot')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=5000)
@click.argument('user_id')
@click.argument('snapshot_id')
def get_snapshot(host, port, user_id, snapshot_id):
    """Returns snapshot of a given user and given snapshot"""
    try:
        res = get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}')
        print(res.text)
    except Exception as e:
        print(f"ERROR: failed fetching data from api: {e}")
        sys.exit(1)


@cli.command('get-result')
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=5000)
@click.option('-s', '--save', default=None)
@click.argument('user_id')
@click.argument('snapshot_id')
@click.argument('result')
def get_result(host, port, save, user_id, snapshot_id, result):
    """Returns details of a given result of specific user"""
    try:
        res = get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result}')
        print(res.text)
    except Exception as e:
        print(f"ERROR: failed fetching data from api: {e}")
        sys.exit(1)
    try:
        if save is not None:
            with open(save, 'w+') as f:
                if result in ['color_image', 'depth_image']:
                    data_load = json.loads(res.text[1:-2])
                    res_path = data_load["parsed_path"]
                    copyfile(res_path, save)
                    print(f"{result} data was saved to file, path: {save}")
                else:
                    f.write(res.text)
                    print(f"Result was saved to file, path: {save}")
    except Exception as e:
        print(f"ERROR: failed to write data to given path: {e}")
        sys.exit(1)


if __name__ == '__main__':
    cli()
