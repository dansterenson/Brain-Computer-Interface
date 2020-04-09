import pathlib
import datetime as dt


class MainParser:

    @classmethod
    def parse(cls, data):
        raise NotImplemented

    @classmethod
    def user_info_data(cls, data, parser_name):
        return {'parser_name': parser_name,
                'user_id': data['user_id'],
                'user_name': data['user_name'],
                'birthday': data['birthday'],
                'gender': data['gender']}