import struct
from ..reader import User


def read_unpack(file_to_read, bytes_format):
    size = struct.calcsize(bytes_format)
    n_bytes = file_to_read.read(size)
    return struct.unpack(bytes_format, n_bytes)

class Hello:
    def __init__(self, user):
        self.user = user

    def __repr__(self):
        return f"user {self.user.id}: {self.user.name}, born {self.user.birth_date} ({self.user.gender})"

    def serialize(self):
        s = struct.Struct(f'QI{len(self.user.name)}sIc')
        return s.pack(self.user.id, self.user.name.encoder(), self.user.birth_date, self.user.gender.encode())

    @classmethod
    def deserialize(cls, file_to_read):
         user_id, user_name_length = read_unpack(file_to_read, 'QI')
         user_name_bytes = read_unpack(file_to_read, '%ds' % user_name_length)
         user_name = user_name_bytes[0].decode()
         user_b_date, user_gender_bytes = read_unpack(file_to_read, 'Ic')
         user_gender = user_gender_bytes.decode()
         user = User(user_id, user_name, user_b_date, user_gender)
         return Hello(user)


class Config:
    def __init__(self, fields):
         self.fields = fields

    def serialize(self):
        fields_in_bytes = []

        # The number of fields supported (a uint32)
        fields_formats = "I"

        for field in self.fields:
            fields_formats = fields_formats + ("I%ds" % len(field))
            fields_in_bytes.append(field)
        s = struct.Struct(fields_formats)
        return s.pack(fields_in_bytes)

    @classmethod
    def deserialize(cls, file_to_read):
        i = 0
        list_of_fields = []
        num_fields = read_unpack(file_to_read, 'I')[0]
        while i <= num_fields:
            field_size = read_unpack(file_to_read, 'I')[0]
            field = read_unpack(file_to_read, "%ds" % field_size)
            list_of_fields.append(field)
            i += 1

        return Config(list_of_fields)

class Snapshot:
    def __init__(self, timestamp, translation, rotation, img, depth_img, hunger, thirst, exhaustion, happiness):
        self.timestamp = timestamp
        self.translation = translation
        self.rotation = rotation
        self.img = img
        self.depth_img = depth_img
        self.feelings =  hunger, thirst, exhaustion, happiness

    def serialize(self, fields):
        not_requested3 = (0, 0, 0)
        not_requested4 = (0, 0, 0, 0)
        not_requested_img = (0, 0, b'')

        for field in fields:
            if field == 'translation':
                translation = self.translation
            else:
                translation = not_requested3

            if field == 'rotation':
                rotation = self.rotation
            else:
                rotation = not_requested4

            if field == 'color image':
                img_width, img_height, img_val = self.img
            else:
                img_width, img_height, img_val = not_requested_img

            if field == 'depth image':
                depth_width, depth_height, depth_val = self.depth_img
            else:
                depth_width, depth_height, depth_val = not_requested_img

            if field == 'feelings':
                feelings = self.feelings
            else:
                feelings = not_requested4

            list_param = [self.timestamp, *translation, *rotation, img_width, img_height]
            if img_height > 0 and img_width > 0:
                list_param.append(img_val)
            list_param.append(depth_width)
            list_param.append(depth_height)
            if depth_height > 0 and depth_width > 0:
                list_param.append(depth_val)
            list_param.append(*feelings)

            s = struct.Struct(f'Q3d4dII{len(img_val)}sII{depth_val}ffff')
            return s.pack(list_param)


    @classmethod
    def deserialize(cls, file_to_read):
        timestamp, tran0, trans1, trans2, trans3, rot1, rot2, rot3, rot4, imgw, imgh = \
        read_unpack(file_to_read, 'Q3d4dII')

        translation = (trans1, trans2, trans3)
        rotation = (rot1, rot2, rot3, rot4)
        rgb_vals = read_unpack(file_to_read, f'{3*imgw*imgh}s')
        color_img = (imgw, imgh, rgb_vals)

        depth_w, depth_h = read_unpack(file_to_read, 'II')
        depth_vals = read_unpack(file_to_read, f'{depth_w*depth_h}f')
        depth_image = (depth_w, depth_h, depth_vals)

        feelings = read_unpack(file_to_read, 'ffff')

        return Snapshot(timestamp, translation, rotation, color_img, depth_vals, feelings)