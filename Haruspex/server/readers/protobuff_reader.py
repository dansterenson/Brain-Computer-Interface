import struct
from readers.haruspex_pb2 import User as protoUser
from readers.haruspex_pb2 import Snapshot as protoSnapshot
import gzip
from .abstract_reader import AbstractReader


def reader_unpack(file_to_read, bytes_format):
    size = struct.calcsize(bytes_format)
    n_bytes = file_to_read.read(size)
    return struct.unpack(bytes_format, n_bytes)


def read_msg_from_file(file):
    len_msg = file.read(struct.calcsize('I'))
    file.offset = struct.calcsize('I')
    return file.read(struct.unpack('I', len_msg)[0])


class ProtoReader(AbstractReader):
    def __init__(self, path_of_sample):
        self.file = gzip.open(path_of_sample, 'rb')

    def get_new_user(self):
        user_from_file = read_msg_from_file(self.file)
        user_from_proto = protoUser()
        user_from_proto.ParseFromString(user_from_file)

        if user_from_proto.gender == 1:
            gender = 'f'
        elif user_from_proto.gender == 0:
            gender = 'm'
        else:
            gender = 'o'

        return protoUser(user_from_proto.user_id, user_from_proto.username, user_from_proto.birthday, gender)

    def get_next_snapshot(self):
        snapshot = protoSnapshot()
        snapshot.ParseFromString(read_msg_from_file(self.file))
        datetime = snapshot.datetime
        translation = (snapshot.pose.translation.x, snapshot.pose.translation.y, snapshot.pose.translation.z)
        rotation = (snapshot.pose.rotation.x, snapshot.pose.rotation.y, snapshot.pose.rotation.z, snapshot.pose.rotation.w)
        color_image = (snapshot.color_image.width, snapshot.color_image.height, snapshot.color_image.data)
        depth_image = (snapshot.depth_image.width, snapshot.depth_image.height, snapshot.depth_image.data)
        feelings = (snapshot.feelings.hunger,
                    snapshot.feelings.thirst,
                    snapshot.feelings.exhaustion,
                    snapshot.feelings.happiness)
        return Snapshot(datetime, translation, rotation, color_image, depth_image, *feelings)
