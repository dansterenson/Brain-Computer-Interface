import mongomock
import pytest
from Noesis.saver import Saver
from mock import patch, MagicMock
from Noesis.api import run_api_server
import threading
import time
from Noesis import cli
import os
from subprocess import Popen, PIPE

data1 = {'user_info': {
    "user_id": 5,
    "user_name": "Dan Sterenson",
    "birthday": 767404800,
    "gender": 'm',
},
    'data': "testAPI",
    'timestamp': 767404840
}

data2 = {'user_info': {
    "user_id": 5,
    "user_name": "Dan Sterenson",
    "birthday": 767404800,
    "gender": 'm',
},
    'data': "testAPI",
    'timestamp': 767404841
}

data3 = {'user_info': {
    "user_id": 7,
    "user_name": "Dan Gittik",
    "birthday": 76734534800,
    "gender": 'm',
},
    'data': "testAPI",
    'timestamp': 767404842
}


@pytest.fixture
def create_api_and_cli():
    with patch("pymongo.MongoClient", MagicMock(return_value=mongomock.MongoClient())):
        s = Saver('mongodb://127.0.0.1:1234')

        s.save('pose', data1)
        s.save('pose', data2)
        s.save('pose', data3)
        host = '127.0.0.1'
        port = 5000
        api_server = threading.Thread(target=run_api_server, args=(host, port, 'mongodb://127.0.0.1:1234'))
        api_server.daemon = True
        api_server.start()
        time.sleep(2)


def test_cli_users(create_api_and_cli):
    process = Popen(["python", "-m", "Noesis.cli", "get-users"], stdout=PIPE)
    (output, err) = process.communicate()
    assert output == b'[{"user_id":5,"user_name":"Dan Sterenson"},{"user_id":7,"user_name":"Dan Gittik"}]\n\n'


def test_api_get_user(create_api_and_cli):
    process = Popen(["python", "-m", "Noesis.cli", "get-user", "5"], stdout=PIPE)
    (output, err) = process.communicate()
    assert output == b'[{"birthday":767404800,"gender":"m","user_id":5,"user_name":"Dan Sterenson"}]\n\n'


def test_api_get_user_snapshots(create_api_and_cli):
    process = Popen(["python", "-m", "Noesis.cli", "get-snapshots", "5"], stdout=PIPE)
    (output, err) = process.communicate()
    assert output == b'[{"datetime":767404840,"snapshot_id":767404840},{"datetime":767404841,"snapshot_id":767404841}]\n\n'


def test_api_get_user_snapshot_results(create_api_and_cli):
    process = Popen(["python", "-m", "Noesis.cli", "get-snapshot", "5", "767404840"], stdout=PIPE)
    (output, err) = process.communicate()
    assert output == b'[{"available_results":["pose"],"date_time":767404840,"snapshot_id":767404840}]\n\n'


def test_api_get_user_snapshot_result_pose(create_api_and_cli):
    process = Popen(["python", "-m", "Noesis.cli", "get-result", "5", "767404840", "pose"], stdout=PIPE)
    (output, err) = process.communicate()
    assert output == b'["testAPI"]\n\n'