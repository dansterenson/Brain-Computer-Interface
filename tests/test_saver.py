
import mongomock
import pytest
from Noesis.saver import Saver
import json
from mock import patch, MagicMock


def test_saver():

    with patch("pymongo.MongoClient", MagicMock(return_value=mongomock.MongoClient())):
        s = Saver('mongodb://127.0.0.1:67676')
    data = json.dumps({'_id': 5, })
    s.save('pose', data)
    #captured = capsys.readouterr()
    #assert "Save to db success" in captured.out
    #assert "Saving to DB failed" not in captured.out