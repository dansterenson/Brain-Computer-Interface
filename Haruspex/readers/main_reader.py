class Reader:
    def __init__(self, file_path, reader_type):
        self.reader_type = reader_type(file_path)

    def __enter__(self):
        self.user = self.reader_type.get_new_user()
        return self

    def __next__(self):
        return self.reader_type.get_next_snapshot()

    def __exit__(self, x, y, z):
        self.reader_type.file.close()

    def __iter__(self):
        return self
