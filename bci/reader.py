import struct

def read_snapshot(file_to_read, bytes_format):
    size = struct.calcsize(bytes_format)
    n_bytes = file_to_read.read(size)
    return struct.unpack(bytes_format, n_bytes)


class Reader:
    def __init__(self, path_of_sample):
        self.file = open(path_of_sample, 'rb')
        self.user = self.get_new_user()

    def get_new_user(self):
        user_id, user_name_length = read_snapshot(self.file, 'QI')
        user_name_bytes = read_snapshot(self.file, '%ds' % user_name_length)
        user_name = user_name_bytes[0].decode()
        user_b_date, user_gender_bytes = read_snapshot(self.file, 'Ic')
        user_gender = user_gender_bytes.decode()
        return User(user_id, user_name, user_b_date, user_gender)

    def get_user_snapshot(self):
        # timestamp, translation, rotation size
        timestamp, translation, rotation = read_snapshot(self.file, 'Q3d4d')

        # img height and width
        img_height, img_width = read_snapshot(self.file, 'II')

        # BRG values
        BGR_values = self.file.read(img_height * img_width * 3)

        # img depth height and width
        depth_height, depth_width = read_snapshot(self.file, 'II')

        # img depth vals
        depth_vals = read_snapshot(self.file, f'{depth_height} * {depth_width}f')


        # hunger, thirst, exhaustion happiness size
        hunger, thirst, exhaustion, happiness = read_snapshot(self.file, '4f')
        return

    def __next__(self):
        return self.get_user_snapshot()

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


if __name__ == '__main__':
    reader = Reader('/home/user/downloads/sample.mind')
    print(reader.user)
    for snapshot in reader:
        print(snapshot)