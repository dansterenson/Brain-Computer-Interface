from Noesis.parsers import AddParser
from Noesis.parsers import MainParser
from PIL import Image


@AddParser.add_to_parser_list("color_image")
class ParseTranslation(MainParser):
    @staticmethod
    def parse(parser):
        path_string = parser.save_to_file('color_image.jpg')
        width, height, data = parser.snapshot.color_image
        image_size = (width, height)
        created_image = Image.new('RGB', image_size)
        created_image.putdata(data)
        created_image.save(path_string)