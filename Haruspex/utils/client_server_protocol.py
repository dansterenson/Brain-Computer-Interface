from ..readers.haruspex_pb2 import User
from ..readers.haruspex_pb2 import Snapshot


def serialize(message):
    serialized_data = message.SerializeToString()
    return serialized_data


def deserialized_user(message):
    user = User()
    return user.ParseFromString(message)


def deserialized_snapshot(message):
    snapshot = Snapshot()
    return snapshot.ParseFromString(message)