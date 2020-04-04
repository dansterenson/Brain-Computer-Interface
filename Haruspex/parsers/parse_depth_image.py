import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from Haruspex.parsers import MainParser
from Haruspex.parsers import AddParser

from PIL import Image
import pathlib


@AddParser.add_to_parser_list("depth_image")
class ParseDepthImage(MainParser):
    @classmethod
    def parse(cls, data):
        depth_img_width, depth_img_height, depth_img_path = data['depth_image']
        data_path = pathlib.Path(depth_img_path)
        parsed_path = data_path.parent / 'parsed_depth_image.jpg'
        with open(data_path, 'rb') as file:
            data_in_bytes = file.read()
        image_size = (depth_img_width, depth_img_height)
        image = Image.frombytes('F', image_size, data_in_bytes)
        plt.imsave(parsed_path, image, cmap=cm.Spectral)
        return {'width': depth_img_width,
                'height': depth_img_height,
                'parsed_path': str(parsed_path)}

