import struct
import datetime as dt


class User:
    def __init__(self, id, name, birth_date, gender):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.gender = gender

    def __repr__(self):
        return f"user {self.id}: {self.name}, born {self.birth_date} ({self.gender})"


class ReadBin:
    def __init__(self):
        self.offset = 0

    def read_unpack(self, file_to_read, bytes_format):
        size = struct.calcsize(bytes_format)
        res = struct.unpack_from(bytes_format, file_to_read, offset=self.offset)
        self.offset += size
        return res


class Hello:
    def __init__(self, user):
        self.user = user

    def __repr__(self):
        return f"user {self.user.id}: {self.user.name}, born {self.user.birth_date} ({self.user.gender})"

    def serialize(self):
        user_len = len(self.user.name)
        data = bytearray()
        data.extend(struct.pack("QI", self.user.id, user_len))
        data.extend(self.user.name.encode())
        data.extend(struct.pack('I', self.user.birth_date))
        data.extend(self.user.gender.encode())
        return bytes(data)

    @classmethod
    def deserialize(cls, file_to_read):
        read_bin = ReadBin()
        (user_id, ) = read_bin.read_unpack(file_to_read, 'Q')
        user_name_length = read_bin.read_unpack(file_to_read, 'I')[0]
        user_name_bytes = read_bin.read_unpack(file_to_read, f"{user_name_length}s")
        user_name = user_name_bytes[0].decode()
        timestamp, user_gender_bytes = read_bin.read_unpack(file_to_read, 'Ic')
        user_b_date = dt.datetime.fromtimestamp(timestamp)
        user_gender = user_gender_bytes.decode()
        user = User(user_id, user_name, user_b_date, user_gender)
        return Hello(user)


class Config:
    def __init__(self, fields):
        self.fields = fields

    def __repr__(self):
        return f"config{self.fields}"

    def serialize(self):
        data = bytearray()
        data.extend(struct.pack("I", len(self.fields)))
        for field in self.fields:
            data.extend(struct.pack("I", len(field)))
            data.extend(field.encode())
        return bytes(data)

    @classmethod
    def deserialize(cls, file_to_read):
        read_bin = ReadBin()
        (num_fields, ) = read_bin.read_unpack(file_to_read, "I")
        fields = []
        for i in range(num_fields):
            (field_size, ) = read_bin.read_unpack(file_to_read, 'I')
            field_name = read_bin.read_unpack(file_to_read, f"{field_size}s")
            fields.append(field_name[0].decode())
        return Config(fields)


class Snapshot:

    def __init__(self, timestamp, translation, rotation, img, depth_img, hunger, thirst, exhaustion, happiness):
        self.timestamp = timestamp
        self.translation = translation
        self.rotation = rotation
        self.img = img
        self.depth_img = depth_img
        self.feelings = hunger, thirst, exhaustion, happiness

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

            if field == 'color_image':
                img_width, img_height, img_val = self.img
            else:
                img_width, img_height, img_val = not_requested_img

            if field == 'depth_image':
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
            list_param.extend([depth_width])
            list_param.extend([depth_height])
            if depth_height > 0 and depth_width > 0:
                list_param.extend(depth_val)
            list_param.extend(feelings)

            s = struct.Struct(f'Q3d4dII{len(img_val)}sII{len(depth_val)}fffff')
            return s.pack(*list_param)

    @classmethod
    def deserialize(cls, file_to_read):
        read_bin = ReadBin()
        timestamp, trans1, trans2, trans3, rot1, rot2, rot3, rot4, imgw, imgh = \
            read_bin.read_unpack(file_to_read, 'Q3d4dII')

        translation = (trans1, trans2, trans3)
        rotation = (rot1, rot2, rot3, rot4)
        rgb_vals = read_bin.read_unpack(file_to_read, f'{3 * imgw * imgh}s')
        color_img = (imgw, imgh, rgb_vals)

        depth_w, depth_h = read_bin.read_unpack(file_to_read, 'II')
        depth_vals = read_bin.read_unpack(file_to_read, f'{depth_w * depth_h}f')
        depth_image = (depth_w, depth_h, depth_vals)

        feelings = read_bin.read_unpack(file_to_read, 'ffff')

        return Snapshot(timestamp, translation, rotation, color_img, depth_image, *feelings)
