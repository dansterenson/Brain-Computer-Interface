import os
import struct


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


class User:
    def __init__(self, id, name, birth_date, gender):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.gender = gender

    def __repr__(self):
        return f"user {self.id}: {self.name}, born {self.birth_date} ({self.gender})"


class Snapshot:
    def __init__(self, timestamp, translation, rotation, img, depth_img, hunger, thirst, exhaustion, happiness):
        self.timestamp = timestamp
        self.translation = translation
        self.rotation = rotation
        self.img = img
        self.depth_img = depth_img
        self.feelings =  hunger, thirst, exhaustion, happiness

    def __repr__(self):
        return f"The snapshot was taken at: {self.timestamp}, " \
               f"on a postion: {self.translation}, " \
               f"the rotation was: {self.rotation} " \
               f"with a color image size of {self.img[0]} over {self.img[1]}, " \
               f"in addition another depth image of size {self.depth_img[0]} over {self.depth_img[1]} " \
               f"with fellings of: {self.feelings}."


if __name__ == '__main__':
    cur_path = os.path.dirname(__file__)
    good = 'sample.mind'
    good2 = os.path.join(cur_path, good)
    reader = Reader(good2)
    print(reader.user)
    for snapshot in reader:
        print(snapshot)