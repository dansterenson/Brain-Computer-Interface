from pathlib import Path


class SaveData:
    def __init__(self, *args):
        path = '/'.join(str(arg) for arg in args)
        self.dir = Path(path)
        self.dir.mkdir(parents=True, exist_ok=True)

    def save_to_file(self, file_name, data, w_format='wb'):
        file_path = self.dir/file_name
        with open(file_path, w_format) as file:
            file.write(data)
        return str(file_path)
