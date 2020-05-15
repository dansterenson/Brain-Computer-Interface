import struct
from .protobuf_pb2 import User as protoUser
from .protobuf_pb2 import Snapshot as protoSnapshot
import gzip
from .reader_abstract import ReaderAbstract


def reader_unpack(file_to_read, bytes_format):
    size = struct.calcsize(bytes_format)
    n_bytes = file_to_read.read(size)
    return struct.unpack(bytes_format, n_bytes)


def read_msg_from_file(file):
    len_msg = file.read(struct.calcsize('I'))
    file.offset = struct.calcsize('I')
    return file.read(struct.unpack('I', len_msg)[0])


class ProtoReader(ReaderAbstract):
    def __init__(self, path_of_sample):
        self.file = gzip.open(path_of_sample, 'rb')

    def get_new_user(self):
        user_from_file = read_msg_from_file(self.file)
        user_from_proto = protoUser()
        user_from_proto.ParseFromString(user_from_file)
        return user_from_proto

    def get_next_snapshot(self):
        snapshot_from_file = read_msg_from_file(self.file)
        snapshot_from_proto = protoSnapshot()
        snapshot_from_proto.ParseFromString(snapshot_from_file)
        return snapshot_from_proto
