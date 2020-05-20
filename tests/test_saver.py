import json
import pytest
from Noesis.saver import Saver
import json
import pathlib
from pymongo import MongoClient


def test_saver(mongodb, monkeypatch):
    collection = mongomock.MongoClient().db.collection

    monkeypatch.setattr(saver['mongodb'], '__init__', mockinit)

    s = Saver('mongodb://127.0.0.1:27017')
    data = json.dumps({'_id': 5, })
    s.save('pose', data)
    captured = capsys.readouterr()
    assert "Save to db success" in captured.out
    assert "Saving to DB failed" not in captured.out