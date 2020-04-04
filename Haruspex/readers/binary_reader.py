import os
import struct
from Haruspex.utils import Snapshot
from Haruspex.utils import User
from .abstract_reader import AbstractReader


def reader_unpack(file_to_read, bytes_format):
    size = struct.calcsize(bytes_format)
    n_bytes = file_to_read.read(size)
    return struct.unpack(bytes_format, n_bytes)


class BinaryReader(AbstractReader):
    def __init__(self, path_of_sample):
        self.file = open(path_of_sample, 'rb')
        self.user = None

    def get_new_user(self):
        user_id, user_name_length = reader_unpack(self.file, 'QI')
        user_name_bytes = reader_unpack(self.file, '%ds' % user_name_length)
        user_name = user_name_bytes[0].decode()
        user_b_date, user_gender_bytes = reader_unpack(self.file, 'Ic')
        user_gender = user_gender_bytes.decode()
        return User(user_id, user_name, user_b_date, user_gender)

    def get_next_snapshot(self):
        # timestamp, translation, rotation size
        timestamp, = reader_unpack(self.file, 'Q')
        translation = reader_unpack(self.file, '3d')
        rotation = reader_unpack(self.file, '4d')
        # img height and width
        img_height, img_width = reader_unpack(self.file, 'II')

        # BRG values
        BGR_values = self.file.read(img_height * img_width * 3)

        # img depth height and width
        depth_height, depth_width = reader_unpack(self.file, 'II')

        # img depth vals
        depth_vals = reader_unpack(self.file, f'{depth_height * depth_width}f')

        # hunger, thirst, exhaustion happiness size
        hunger, thirst, exhaustion, happiness = reader_unpack(self.file, '4f')
        return Snapshot(timestamp, translation, rotation,
                        (img_width, img_height, BGR_values),
                        (depth_width, depth_height, depth_vals),
                        hunger, thirst, exhaustion, happiness)
