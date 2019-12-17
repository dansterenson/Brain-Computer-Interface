import datetime as dt
import socket
import time
from .thought import Thought
from .utils.connection import Connection


def upload_thought(address, user, thought):
    ip_address, port = address.split(":")
    timestamp = int(dt.datetime.now().timestamp())
    thought_obj = Thought(user, timestamp, thought)
    try:
        with Connection.connect(ip_address, int(port)) as con:
            con.sendall(thought_obj.serialize())
            print("done")

    except socket.error as e:
        print("Error - Failed sending message {}".format(e))


