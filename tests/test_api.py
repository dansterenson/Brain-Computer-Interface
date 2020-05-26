import pytest
import mongomock
import pytest
from Noesis.saver import Saver
import json
from mock import patch, MagicMock
import requests
from Noesis.api import run_api_server
from multiprocessing import Process
import multiprocessing, logging
import threading
import time

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
def create_api():
    with patch("pymongo.MongoClient", MagicMock(return_value=mongomock.MongoClient())):
        s = Saver('mongodb://127.0.0.1:1234')

        s.save('pose', data1)
        s.save('pose', data2)
        s.save('pose', data3)
        host = '127.0.0.1'
        port = 5000
        server = threading.Thread(target=run_api_server, args=(host, port, 'mongodb://127.0.0.1:1234'))
        server.daemon = True
        server.start()
        time.sleep(2)


def test_api_users(create_api):

    response = requests.get('http://127.0.0.1:5000/users')
    assert response.content == b'[{"user_id":5,"user_name":"Dan Sterenson"},{"user_id":7,"user_name":"Dan Gittik"}]\n'
    assert response.status_code == 200


def test_api_get_user(create_api):
    response = requests.get('http://127.0.0.1:5000/users/5')
    assert response.content == b'[{"birthday":767404800,"gender":"m","user_id":5,"user_name":"Dan Sterenson"}]\n'
    assert response.status_code == 200


def test_api_get_user_snapshots(create_api):
    response = requests.get('http://127.0.0.1:5000/users/5/snapshots')
    assert response.content == b'[{"datetime":767404840,"snapshot_id":767404840},{"datetime":767404841,"snapshot_id":767404841}]\n'
    assert response.status_code == 200


def test_api_get_user_snapshot_results(create_api):
    response = requests.get('http://127.0.0.1:5000/users/5/snapshots/767404840')
    assert response.content == b'[{"available_results":["pose"],"date_time":767404840,"snapshot_id":767404840}]\n'
    assert response.status_code == 200


def test_api_get_user_snapshot_result_pose(create_api):
    response = requests.get('http://127.0.0.1:5000/users/5/snapshots/767404840/pose')
    assert response.content == b'["testAPI"]\n'
    assert response.status_code == 200