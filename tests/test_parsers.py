import pytest
from Noesis.parsers import run_parser
import pathlib
import json
from mock import patch, MagicMock


@pytest.fixture
def file_data():
    message_path = str(pathlib.Path('tests/data/test_data.json').absolute())
    with open(message_path, 'r') as file:
        data = json.load(file)
    return data

def test_feelings_parser(file_data):
    parsed_result = run_parser('feelings', file_data)
    assert parsed_result is not None
    assert parsed_result['result_name'] == 'feelings'
    assert parsed_result['data']['hunger'] == 0.1
    assert parsed_result['data']['thirst'] == 0.2
    assert parsed_result['data']['exhaustion'] == 0.3
    assert parsed_result['data']['happiness'] == 0.4


def test_pose_parser(file_data):
    parsed_result = run_parser('pose', file_data)
    assert parsed_result is not None
    assert parsed_result['result_name'] == 'pose'
    assert parsed_result['data']['translation'] == [0.1, 0.2, 0.3]
    assert parsed_result['data']['rotation'] == [0.1, 0.2, 0.3, 0.4]