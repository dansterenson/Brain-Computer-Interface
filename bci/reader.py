import struct


class Reader:
    def __init__(self, path_of_sample):
        self.file = open(path_of_sample, 'rb')
        self.user = self.get_new_user()

    def get_new_user(self):
        user_format = 'QQIc'
        size = struct.calcsize(user_format)
        user_in_bytes = self.file.read(size)
        user_id, name_in_bits, birth_date, gender = struct.unpack('QIIc', user_in_bytes)
        user_name = name_in_bits.decode()
        gender = gender.decode()
        return User(user_id, user_name, birth_date, gender)

    def get_user_snapshot(self):
        # timestamp, translation, rotation size
        ttr_size = 'Q3d4d'
        size = struct.calcsize(ttr_size)
        ttr_in_bytes = self.file.read(size)
        timestamp, translation, rotation = struct.unpack('Q3d4d', ttr_in_bytes)

        img_height_width = 'II'
        size = struct.calcsize(img_height_width)
        img_in_bytes = self.file.read(size)
        img_height, img_width = struct.unpack('II', img_in_bytes)

        BGR_values = self.file.read(img_height * img_width * 3)

        depth_height_width = 'II'
        size = struct.calcsize(depth_height_width)
        depth_in_bytes = self.file.read(size)
        depth_height, depth_width = struct.unpack('II', depth_in_bytes)

        depth_val_size = f'{depth_height} * {depth_width}f'
        size = struct.calcsize(depth_val_size)
        depth_vals_bytes = self.file.read(size)
        depth_vals = struct.unpack(f'{depth_height} * {depth_width}f', depth_vals_bytes)

        # hunger, thirst, exhaustion happiness size
        hteh_size = '4f'
        size = struct.calcsize(hteh_size)
        hteh_in_bytes = self.file.read(size)
        hunger, thirst, exhaustion, happiness = struct.unpack('4f', hteh_in_bytes)

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