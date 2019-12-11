import datetime as dt
import socket
import struct
import threading
from pathlib import Path
import click

_SERVER_BACKLOG = 1000
_HEADER_FORMAT = 'QQI'
_HEADER_SIZE = struct.calcsize(_HEADER_FORMAT)


def _format_timestamp(timestamp):
    datetime = dt.datetime.fromtimestamp(timestamp)
    return f'{datetime:%Y-%m-%d_%H-%M-%S}'


def _receive_all(connection, size):
    chunks = []
    while size > 0:
        chunk = connection.recv(size)
        if not chunk:
            raise RuntimeError('incomplete data')
        chunks.append(chunk)
        size -= len(chunk)
    return b''.join(chunks)


class Handler(threading.Thread):
    def __init__(self, connection, data_dir):
        super().__init__()
        self.connection = connection
        self.lock = threading.Lock()
        self.data_dir = data_dir

    def run(self):
        with self.connection:
            header_data = _receive_all(self.connection, _HEADER_SIZE)
            user_id, timestamp, size = struct.unpack(_HEADER_FORMAT, header_data)
            data = _receive_all(self.connection, size)
            thought = data.decode()
            user_dir_path = Path(self.data_dir) / str(user_id)
            user_dir_path.mkdir(parents=True, exist_ok= True)
            file_path = user_dir_path / f'{_format_timestamp(timestamp)}.txt'
            self.lock.acquire()
            if file_path.exists():
                exists = True
            else:
                exists = False
            with open(file_path, mode='a') as f:
                if exists:
                    f.write('\n' + thought)
                else:
                    f.write(thought)
            self.lock.release()


@click.command()
@click.argument('address')
@click.argument('data')
def run(address, data):
    ip_address, port = address.split(":")
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((ip_address, int(port)))
        server.listen(_SERVER_BACKLOG)

        with server:
            while True:
                connection, client_address = server.accept()
                handler = Handler(connection, data)
                handler.start()

    except socket.error as e:
        print('Error - Bind failed. Message {}'.format(e))

    except Exception as e:
        print('Error -  Message {}'.format(e))


if __name__ == '__main__':
    pass
