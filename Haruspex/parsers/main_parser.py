import pathlib
import datetime as dt


class MainParser:

    def __init__(self):
        pass

    @classmethod
    def save_to_file(cls, name_of_file, user, snapshot, data_dir):
        datetime = dt.datetime.fromtimestamp(snapshot.timestamp/1000.0)

        #change format
        dt_format = datetime.strftime('%Y-%m-%d_%H-%M-%S-%f')

        # get only 5 digits for microseconds
        choped_datetime = dt_format[:-1]

        new_dir = pathlib.Path() / data_dir / str(user.id) / choped_datetime
        new_dir.mkdir(parents=True, exist_ok=True)
        return new_dir / name_of_file

    @classmethod
    def parse(cls, data):
        raise NotImplemented

