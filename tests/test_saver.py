import mongomock
import pytest
from Noesis.saver import Saver
import json
from mock import patch, MagicMock
from subprocess import Popen, PIPE
import pathlib

data1 = {'user_info': {
    "user_id": 5,
    "user_name": "Dan Sterenson",
    "birthday": 767404800,
    "gender": 0,
},
    'data': "testSaver",
    'timestamp': 767404840
}

data2 = {'user_info': {
    "user_id": 5,
    "user_name": "Dan Sterenson",
    "birthday": 767404800,
    "gender": 0,
},
    'data': "testSaver",
    'timestamp': 767404841
}

data3 = {'user_info': {
    "user_id": 7,
    "user_name": "Dan Gittik",
    "birthday": 76734534800,
    "gender": 0,
},
    'data': "testSaver2",
    'timestamp': 767404842
}



def test_saver(capsys):

    with patch("pymongo.MongoClient", MagicMock(return_value=mongomock.MongoClient())):
        s = Saver('mongodb://127.0.0.1:67676')

        s.save('pose', data1)
        s.save('feelings', data2)
        s.save('pose', data3)


        assert s.db.get_users() == [{'user_id': 5, 'user_name': 'Dan Sterenson', 'birthday': 767404800, 'gender': 0},
                                    {'user_id': 7, 'user_name': 'Dan Gittik', 'birthday': 76734534800, 'gender': 0}]

        assert s.db.get_user(5) == [{'user_id': 5, 'user_name': 'Dan Sterenson', 'birthday': 767404800, 'gender': 0}]
        assert s.db.get_user_snapshots(5) == [{'user_id': 5, 'timestamp': 767404840, 'parser_type': 'pose', 'parsed_data': 'testSaver'},
                                              {'user_id': 5, 'timestamp': 767404841, 'parser_type': 'feelings', 'parsed_data': 'testSaver'}]
        assert s.db.get_snapshot_by_id(5, 767404840) == [{'user_id': 5, 'timestamp': 767404840, 'parser_type': 'pose', 'parsed_data': 'testSaver'}]
        assert s.db.get_snapshot_by_result(5, 767404840, 'pose') == [{'user_id': 5, 'timestamp': 767404840, 'parser_type': 'pose', 'parsed_data': 'testSaver'}]
        assert s.db.get_snapshot_by_result(5, 767404841, 'feelings') == [{'user_id': 5, 'timestamp': 767404841, 'parser_type': 'feelings', 'parsed_data': 'testSaver'}]

