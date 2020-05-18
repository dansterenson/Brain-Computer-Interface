import requests
from ..readers import Reader
from ..readers import protobuf_pb2
#import logging

#logging.basicConfig(filename='./log_files/client.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def upload_sample(address, file_path, reader_type='ProtoReader'):
    host, port = address
    reader = Reader(file_path, reader_type)

    with reader as r:
        for snapshot in r:
            user = r.user
            #logging.debug(f'Read Snapshot from user:\n {user}')
            combined = protobuf_pb2.Combined(user=user, snapshot=snapshot).SerializeToString()
            #logging.debug('Uploading data to server')
            requests.post(f'http://{host}:{port}/upload_snapshot', data=combined)

