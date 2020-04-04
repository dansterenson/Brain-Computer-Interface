import pathlib
import datetime as dt


class MainParser():

    def save_to_file(self, name_of_file):
        datetime = dt.datetime.fromtimestamp(self.snapshot.timestamp/1000.0)

        #change format
        dt_format = datetime.strftime('%Y-%m-%d_%H-%M-%S-%f')

        # get only 5 digits for microseconds
        choped_datetime = dt_format[:-1]

        new_dir = pathlib.Path(self.data_dir / self.user.user_id / choped_datetime)
        new_dir.mkdir()
        return new_dir / name_of_file

    @staticmethod
    def parse(parser):
        pass
