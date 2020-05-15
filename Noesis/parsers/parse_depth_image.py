import matplotlib.cm as cm
import matplotlib.pyplot as plt
from .parser_manager import user_info_data
from PIL import Image
import pathlib
import matplotlib.cm as cmap


def parse(data):
    depth_img_width, depth_img_height, depth_img_path = data['depth_image']
    data_path = pathlib.Path(depth_img_path)
    parsed_path = data_path.parent / 'parsed_depth_image.jpg'
    with open(data_path, 'rb') as file:
        data_in_bytes = file.read()
    image_size = (depth_img_width, depth_img_height)
    image = Image.frombytes('F', image_size, data_in_bytes)
    plt.imsave(parsed_path, image, cmap=cmap.get_cmap("RdGy"))
    user_info = user_info_data(data)
    return {'user_info': user_info,
            'timestamp': data['timestamp'],
            'result_name': 'depth_image',
            'data': {'width': depth_img_width,
                     'height': depth_img_height,
                     'parsed_path': str(parsed_path)}}

