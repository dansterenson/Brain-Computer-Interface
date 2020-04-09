from . import add_to_parser_list
from .main_parser import MainParser


@add_to_parser_list("feelings")
class ParseFeelings(MainParser):
    @classmethod
    def parse(cls, data):
        user_info = cls.user_info_data(data, 'feelings')
        return {'user_info': user_info,
                'timestamp': data['timestamp'],
                'data:': {data['feelings']}}