import datetime as dt
import socket
import struct
import threading
from pathlib import Path
from Haruspex.utils import Listener
from Haruspex.utils import Hello
from Haruspex.utils import Config
from Haruspex.utils import Snapshot
from Haruspex.parsers import AddParser
from Haruspex.parsers import MainParser



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
            user = Hello.deserialize(self.connection.receive_message())
            config = Config(list(AddParser.parsers_dict.keys()))
            config_message = Config.serialize(config)
            self.connection.send_message(config_message)
            snapshot = Snapshot.deserialize(self.connection.receive_message())
            self.lock.acquire()
            for parser_name in AddParser.parsers_dict:
                cur_parser = AddParser.parsers_dict[parser_name]
                cur_parser(user, snapshot, self.data_dir)
            self.lock.release()
            print("snapshot saved\n")


def run_server(address, data_dir):
    ip_address, port = address.split(":")
    with Listener(ip_address, int(port)) as listener:
        while True:
            connection = listener.accept()
            handler = Handler(connection, data_dir)
            handler.start()


if __name__ == '__main__':
    pass
