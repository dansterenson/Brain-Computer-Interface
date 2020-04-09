from . import add_to_parser_list
from .main_parser import MainParser


@add_to_parser_list("pose")
class ParsePose(MainParser):
    @classmethod
    def parse(cls, data):
        user_info = cls.user_info_data(data, 'pose')
        return {'user_info': user_info,
                'timestamp': data['timestamp'],
                'data': {'translation': data['translation'], 'rotation': data['rotation']}}