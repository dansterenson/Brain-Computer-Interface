from pathlib import Path


class LoadSaveData:
    def __init__(self, *args):
        path = '/'.join(str(arg) for arg in args)
        self.dir = Path(path)
        self.dir.mkdir(parents=True, exist_ok=True)

    def load_file_path(self, file_name):
        return self.dir/file_name

    def save_to_file(self, file_name, data, w_format='wb'):
        file_path = self.dir/file_name
        with open(file_path, w_format) as file:
            file.write(data)
