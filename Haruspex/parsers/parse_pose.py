from .add_parser import AddParser
from .main_parser import MainParser


@AddParser.add_to_parser_list("pose")
class ParsePose(MainParser):
    @classmethod
    def parse(cls, data):
        return {'translation': data['translation'], 'rotation': data['rotation']}