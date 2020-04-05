from Haruspex.parsers import AddParser
from Haruspex.parsers import MainParser
from PIL import Image
import pathlib


@AddParser.add_to_parser_list("color_image")
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
        return {'width': color_img_width,
                'height': color_img_height,
                'parsed_path': str(parsed_path)}
