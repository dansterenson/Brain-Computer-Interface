from . import add_to_parser_list
from .main_parser import MainParser
from PIL import Image
import pathlib


@add_to_parser_list("color_image")
class ParseColorImage(MainParser):
    @classmethod
    def parse(cls, data):
        color_img_width, color_img_height, color_img_path = data['color_image']
        data_path = pathlib.Path(color_img_path)
        parsed_path = data_path.parent / 'parsed_color_image.jpg'
        with open(data_path, 'rb') as file:
            data_in_bytes = file.read()
        image_size = (color_img_width, color_img_height)
        image = Image.frombytes('RGB', image_size, data_in_bytes)
        image.save(parsed_path)
        user_info = cls.user_info_data(data)
        return {'user_info': user_info,
                'timestamp': data['timestamp'],
                'results': 'color_image',
                'data': {'width': color_img_width,
                         'height': color_img_height,
                         'parsed_path': str(parsed_path)}}

