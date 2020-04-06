from . import add_to_parser_list
from .main_parser import MainParser


@add_to_parser_list("feelings")
class ParseFeelings(MainParser):
    @classmethod
    def parse(cls, data):
        return {'feelings': data['feelings']}