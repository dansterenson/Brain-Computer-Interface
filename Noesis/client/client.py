import gzip
import requests
from ..readers import Reader
from ..readers import protobuf_pb2
from .utils.logger import create_logger


def upload_sample(address, file_path, reader_type='ProtoReader'):
    logger = create_logger("client")
    host, port = address
    reader = Reader(file_path, reader_type)
    snapshots_num = 0

    with reader as r:
        for snapshot in r:
            user = r.user
            #with gzip.open('test_file.mind.gz', 'wb') as f:
            #    user1 = user.SerializeToString()
            #    snapshot1 = snapshot.SerializeToString()
            #    f.write(len(user1).to_bytes(4, 'little') + user1 + len(snapshot1).to_bytes(4, 'little') + snapshot1)
            combined = protobuf_pb2.Combined(user=user, snapshot=snapshot).SerializeToString()
            requests.post(f'http://{host}:{port}/upload_snapshot', data=combined)
            snapshots_num += 1
            logger.info(f'Uploaded user: {user}\n snapshot number: {snapshots_num}')
            logger.debug(f'Uploaded snapshot: {snapshot}')
        print(f"all {snapshots_num} snapshots of user_id: {user.user_id} were uploaded")
