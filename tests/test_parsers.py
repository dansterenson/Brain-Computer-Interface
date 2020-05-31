import pytest
from Noesis.parsers import run_parser
import pathlib
import json
from shutil import copyfile
import os
from subprocess import Popen, PIPE
import time


@pytest.fixture
def file_data():
    message_path = str(pathlib.Path('tests/data/test_data.json').absolute())
    with open(message_path, 'r') as file:
        data = json.load(file)
    return data


#def test_parse_cli():
#    message_path = str(pathlib.Path('tests/data/test_data.json').absolute())
#    process = Popen(["python", "-m", "Noesis.parsers", "parse", "pose", message_path], stdout=PIPE)
#    (output, err) = process.communicate()
#    assert b"{'user_info': {'user_id': 5, 'user_name': 'Dan Sterenson', 'birthday': 767404800, 'gender': 0}" in output
#    assert b"'timestamp': '12345678'" in output
#    assert b"result_name': 'pose'" in output
#    assert b"'data': {'translation': [0.1, 0.2, 0.3], 'rotation': [0.1, 0.2, 0.3, 0.4]}" in output


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


def test_color_image(file_data):
    parsed_result = run_parser('color_image', file_data)
    assert parsed_result is not None
    assert parsed_result['result_name'] == 'color_image'
    assert parsed_result['data']['width'] == 1920
    assert parsed_result['data']['height'] == 1080
    assert parsed_result['data']['parsed_path'] == "tests/data/parsed_color_image.jpg"


def test_depth_image(file_data):
    parsed_result = run_parser('depth_image', file_data)
    assert parsed_result is not None
    assert parsed_result['result_name'] == 'depth_image'
    assert parsed_result['data']['width'] == 1280
    assert parsed_result['data']['height'] == 720
    assert parsed_result['data']['parsed_path'] == "tests/data/parsed_depth_image.jpg"


def test_adding_parser(file_data):
    copyfile("tests/data/parse_test_parser.py", "Noesis/parsers/parse_test_parser.py")
    parsed_result = run_parser('test_parser', file_data)
    os.remove("Noesis/parsers/parse_test_parser.py")
    assert parsed_result is not None
    assert parsed_result['result_name'] == 'test_parser'
    assert parsed_result['data'] == {'testing_adding_parser'}