from . import add_to_parser_list
from .main_parser import MainParser


@add_to_parser_list("pose")
class ParsePose(MainParser):
    @classmethod
    def parse(cls, data):
        return {'translation': data['translation'], 'rotation': data['rotation']}