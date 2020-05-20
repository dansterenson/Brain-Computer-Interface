import pytest
from Noesis.parsers import run_parser
import pathlib
import json


def test_feelings_parser():
    message_path = str(pathlib.Path('data/test_data.json').absolute())
    with open(message_path, 'r') as file:
        data = json.load(file)
    parsed_result = run_parser('feelings', data)
    assert parsed_result is not None
    assert parsed_result['result_name'] == 'feelings'
    assert parsed_result['data']['hunger'] == 0.1
    assert parsed_result['data']['thirst'] == 0.2
    assert parsed_result['data']['exhaustion'] == 0.3
    assert parsed_result['data']['happiness'] == 0.4


def test_pose_parser():
    path_to_message = str(pathlib.Path(
        'tests/resources/example-message.json').absolute())
    message = json.load(open(path_to_message, 'r'))
    parsed_result = json.loads(run_parser('pose', message))
    assert parsed_result is not None
    assert parsed_result['pose']['translation']['x'] == parsed_result['pose']['translation']['y']
    assert parsed_result['pose']['translation']['z'] == 0.5
    assert parsed_result['pose']['rotation']['w'] == 0.4