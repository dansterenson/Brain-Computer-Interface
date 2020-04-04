from Haruspex.parsers import AddParser
from Haruspex.parsers import MainParser
import json


@AddParser.add_to_parser_list("translation")
class ParseTranslation(MainParser):
    @staticmethod
    def parse(user, snapshot, data_dir):
        path_string = MainParser.save_to_file('translation.json', user, snapshot, data_dir)
        x, y, z = snapshot.translation
        with open(path_string, 'w') as f:
            json_format = {'x': x, 'y': y, 'z': z}
            json.dump(json_format, f)