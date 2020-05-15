import os
import struct
from Haruspex.utils import Snapshot
from Haruspex.utils import User


def reader_unpack(file_to_read, bytes_format):
    size = struct.calcsize(bytes_format)
    n_bytes = file_to_read.read(size)
    return struct.unpack(bytes_format, n_bytes)


class Reader:
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

    def get_user_snapshot(self):
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

    def __next__(self):
        return self.get_user_snapshot()

    def __enter__(self):
        self.user = self.get_new_user()
        return self

    def __exit__(self, x ,y, z):
        self.file.close()

    def __iter__(self):
        return self

#
# class user:
#     def __init__(self, id, name, birth_date, gender):
#         self.id = id
#         self.name = name
#         self.birth_date = birth_date
#         self.gender = gender
#
#     def __repr__(self):
#         return f"user {self.id}: {self.name}, born {self.birth_date} ({self.gender})"
#
#
# class snapshot:
#     def __init__(self, timestamp, translation, rotation, img, depth_img, hunger, thirst, exhaustion, happiness):
#         self.timestamp = timestamp
#         self.translation = translation
#         self.rotation = rotation
#         self.img = img
#         self.depth_img = depth_img
#         self.feelings = hunger, thirst, exhaustion, happiness
#
#     def __repr__(self):
#         return f"the snapshot was taken at: {self.timestamp}, " \
#                f"on a postion: {self.translation}, " \
#                f"the rotation was: {self.rotation} " \
#                f"with a color image size of {self.img[0]} over {self.img[1]}, " \
#                f"in addition another depth image of size {self.depth_img[0]} over {self.depth_img[1]} " \
#                f"with fellings of: {self.feelings}."
#
#     def serialize(self, fields):
#         not_requested3 = (0, 0, 0)
#         not_requested4 = (0, 0, 0, 0)
#         not_requested_img = (0, 0, b'')
#
#         for field in fields:
#             if field == 'translation':
#                 translation = self.translation
#             else:
#                 translation = not_requested3
#
#             if field == 'rotation':
#                 rotation = self.rotation
#             else:
#                 rotation = not_requested4
#
#             if field == 'color image':
#                 img_width, img_height, img_val = self.img
#             else:
#                 img_width, img_height, img_val = not_requested_img
#
#             if field == 'depth image':
#                 depth_width, depth_height, depth_val = self.depth_img
#             else:
#                 depth_width, depth_height, depth_val = not_requested_img
#
#             if field == 'feelings':
#                 feelings = self.feelings
#             else:
#                 feelings = not_requested4
#
#             list_param = [self.timestamp, *translation, *rotation, img_width, img_height]
#             if img_height > 0 and img_width > 0:
#                 list_param.append(img_val)
#             list_param.append(depth_width)
#             list_param.append(depth_height)
#             if depth_height > 0 and depth_width > 0:
#                 list_param.append(depth_val)
#             list_param.append(feelings)
#
#             s = struct.struct(f'qdddddddii{len(img_val)}sii{depth_val}ffff')
#             return s.pack(list_param)
#
#     @classmethod
#     def deserialize(cls, file_to_read):
#         read_bin = readbin()
#         timestamp, tran0, trans1, trans2, trans3, rot1, rot2, rot3, rot4, imgw, imgh = \
#             read_bin.read_unpack(file_to_read, 'q3d4dii')
#
#         translation = (trans1, trans2, trans3)
#         rotation = (rot1, rot2, rot3, rot4)
#         rgb_vals = read_bin.read_unpack(file_to_read, f'{3 * imgw * imgh}s')
#         color_img = (imgw, imgh, rgb_vals)
#
#         depth_w, depth_h = read_bin.read_unpack(file_to_read, 'ii')
#         depth_vals = read_bin.read_unpack(file_to_read, f'{depth_w * depth_h}f')
#         depth_image = (depth_w, depth_h, depth_vals)
#
#         feelings = read_bin.read_unpack(file_to_read, 'ffff')
#
#         return snapshot(timestamp, translation, rotation, color_img, depth_vals, feelings)
# ##