import requests
from ..readers import Reader
from ..readers import protobuf_pb2


def upload_sample(address, file_path, reader_type='ProtoReader'):
    host, port = address
    reader = Reader(file_path, reader_type)

    with reader as r:
        for snapshot in r:
            user = r.user
            combined = protobuf_pb2.Combined(user=user, snapshot=snapshot).SerializeToString()
            requests.post(f'http://{host}:{port}/upload_snapshot', data=combined)

