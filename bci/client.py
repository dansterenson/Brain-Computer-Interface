import datetime as dt
import socket
import struct
import click

from .thought import Thought
from .utils import Connection
_HEADER_FORMAT = 'QQI'


def _serialize_thought(user_id, timestamp, thought):
    header = struct.pack(_HEADER_FORMAT, user_id, timestamp, len(thought))
    return header + thought.encode()


def upload_thought(address, user, thought):
    ip_address, port = address.split(":")
    timestamp = int(dt.datetime.now().timestamp())
    message = _serialize_thought(int(user), timestamp, thought)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.connect((ip_address, int(port)))
            connection.sendall(message)
            print("done")
    except socket.error as e:
        print("Error - Failed sending message {}".format(e))


