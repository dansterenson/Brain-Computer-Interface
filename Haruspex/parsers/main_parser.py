import pathlib
import datetime as dt


class MainParser:

    @classmethod
    def parse(cls, data):
        raise NotImplemented

    @classmethod
    def user_info_data(cls, data):
        return {'user_id': data['user_id'],
                'user_name': data['user_name'],
                'birthday': data['birthday'],
                'gender': data['gender']}