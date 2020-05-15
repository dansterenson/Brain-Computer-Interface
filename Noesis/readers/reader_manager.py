import pkgutil
from os.path import dirname
from importlib import import_module


class Reader:
    def __init__(self, file_path, reader_type):
        self.supported_readers = {}
        self.load_all_readers()
        self.reader_type = self.get_reader(reader_type)(file_path)

    def __enter__(self):
        self.user = self.reader_type.get_new_user()
        return self

    def __next__(self):
        return self.reader_type.get_next_snapshot()

    def __exit__(self, x, y, z):
        self.reader_type.file.close()

    def __iter__(self):
        return self

    def load_all_readers(self):
        pwd = dirname(__file__)
        for (_, name, _) in pkgutil.iter_modules([pwd]):
            if name.endswith('_reader'):
                module = import_module('Noesis.readers' + '.' + name)
                for name_attr in dir(module):
                    if name_attr.endswith("Reader"):
                        self.supported_readers[name_attr] = getattr(module, name_attr)

    def get_reader(self, reader_type):
        try:
            return self.supported_readers[reader_type]

        except Exception as e:
            print(f"unable to find the readertype given as an input {reader_type}")
