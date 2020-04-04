from .add_parser import AddParser
from .main_parser import MainParser


@AddParser.add_to_parser_list("feelings")
class ParsePose(MainParser):
    @classmethod
    def parse(cls, data):
        return {'feelings': data['feelings']}