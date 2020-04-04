import socket
import time

import pytest

from Haruspex.utils import Listener
from Haruspex.utils.protoco1l import Hello
from Haruspex.utils import Connection
from Haruspex.utils.protoco1l import User

_PORT = 1234
_HOST = '127.0.0.1'
_BACKLOG = 5000
_REUSEADDR = True
_DATA = b'Hello, world!'


@pytest.fixture
def listener():
    return Listener(_PORT, host=_HOST, backlog=_BACKLOG, reuseaddr=_REUSEADDR)


def test_attributes(listener):
    assert listener.port == _PORT
    assert listener.host == _HOST
    assert listener.backlog == _BACKLOG
    assert listener.reuseaddr == _REUSEADDR


def test_defaults():
    listener = Listener(_PORT)
    assert listener.host == '0.0.0.0'
    assert listener.backlog == 1000
    assert listener.reuseaddr is True


def test_repr(listener):
    assert repr(listener) == f'Listener(port={_PORT!r}, host={_HOST!r}, backlog={_BACKLOG!r}, reuseaddr={_REUSEADDR!r})'


def test_close(listener):
    assert socket.socket().connect_ex((_HOST, _PORT)) != 0
    listener.start()
    try:
        time.sleep(0.1)
        assert socket.socket().connect_ex((_HOST, _PORT)) == 0
    finally:
        listener.stop()
    assert socket.socket().connect_ex((_HOST, _PORT)) != 0


def test_accept(listener):
    sock = socket.socket()
    listener.start()
    try:
        time.sleep(0.1)
        with Connection.connect(_HOST, _PORT) as con:
            connection = listener.accept()
        try:
            user = User(42, 'Dan', 34534, 'm')
            hello = Hello(user)
            first = hello.serialize()
            con.send_message(first)
            sec = connection.receive_message()
            thrid = hello.deserialize(sec)
            assert thrid.__repr__()  == user.__repr__()
        finally:
            connection.close()
    finally:
        listener.stop()
