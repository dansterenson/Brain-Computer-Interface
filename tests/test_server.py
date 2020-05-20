import pytest
from Noesis.client import upload_sample
from Noesis.server import run_server
import threading
import time


def test_my_server(capsys):
    def print_function(data):
        print(data)

    host = '127.0.0.1'
    port = 8000
    server = threading.Thread(target=run_server, args=(host, port, print_function))
    server.daemon = True
    server.start()
    time.sleep(1)
    upload_sample((host, port), 'data/test_file.mind.gz')
    time.sleep(1)
    captured = capsys.readouterr()
    assert f"Running on http://{host}:{port}/" in captured.err
    assert '{"user_id": 5, "user_name": "Dan Sterenson", "birthday": 767404800, "gender": "m",' in captured.out
