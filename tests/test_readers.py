import pytest
from Noesis.readers.protobuff_reader import ProtoReader
import pathlib

file_path = pathlib.Path(__file__).absolute().parent / "data/test_file.mind.gz"


@pytest.fixture
def parse_data():
    return ProtoReader(file_path)


def test_user_parsing(parse_data):
    user = parse_data.get_new_user()
    assert user.user_id == 5
    assert user.username == 'Dan Sterenson'
    assert user.birthday == 767404800
    assert user.gender == 0

    snapshot = parse_data.get_next_snapshot()
    assert snapshot.datetime == 1575446887339
    assert snapshot.pose.translation.x == 0.4873843491077423
    assert snapshot.pose.translation.y == 0.007090016733855009
    assert snapshot.pose.translation.z == -1.1306129693984985
    assert snapshot.pose.rotation.x == -0.10888676356214629
    assert snapshot.pose.rotation.y == -0.26755994585035286
    assert snapshot.pose.rotation.z == -0.021271118915446748
    assert snapshot.pose.rotation.w == 0.9571326384559261
    assert snapshot.depth_image.width == 224
    assert snapshot.depth_image.height == 172
    assert snapshot.color_image.width == 1920
    assert snapshot.color_image.height == 1080
    assert snapshot.color_image.data == b''
    assert snapshot.feelings.hunger == 0.0
    assert snapshot.feelings.thirst == 0.0
    assert snapshot.feelings.happiness == 0.0
    assert snapshot.feelings.exhaustion == 0.0
