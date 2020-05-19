import struct
from .protobuf_pb2 import User as protoUser
from .protobuf_pb2 import Snapshot as protoSnapshot
import gzip
from .reader_abstract import ReaderAbstract


class ProtoReader(ReaderAbstract):
    def __init__(self, path_of_sample):
        self.file = gzip.open(path_of_sample, 'rb')

    def get_new_user(self):
        user_size = int.from_bytes(self.file.read(4), 'little')
        user_from_file = self.file.read(user_size)
        user_from_proto = protoUser()
        user_from_proto.ParseFromString(user_from_file)
        return user_from_proto

    def get_next_snapshot(self):
        snapshot_len = self.file.read(4)
        snapshot_len = int.from_bytes(snapshot_len, 'little')

        if not snapshot_len:
            raise StopIteration
        snapshot_from_file = self.file.read(snapshot_len)
        snapshot_from_proto = protoSnapshot()
        snapshot_from_proto.ParseFromString(snapshot_from_file)
        return snapshot_from_proto
