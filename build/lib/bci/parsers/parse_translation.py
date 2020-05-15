from Noesis.parsers import AddParser
from Noesis.parsers import MainParser
import json


@AddParser.add_to_parser_list("translation")
class ParseTranslation(MainParser):
    @staticmethod
    def parse(parser):
        path_string = parser.save_to_file('translation.json')
        x, y, z = parser.snapshot.translation
        with open(path_string, 'w') as f:
            json_format = {'x': x, 'y': y, 'z': z}
            json.dump(json_format, f)