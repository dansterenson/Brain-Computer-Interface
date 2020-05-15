import pkgutil
from os.path import dirname
from importlib import import_module


class Parser:
    def __init__(self):
        self.supported_parsers = {}
        self.load_all_parsers()

    def load_all_parsers(self):
        pwd = dirname(__file__)
        for (_, name, _) in pkgutil.iter_modules([pwd]):
            if name.startswith('parse_'):
                module = import_module('Noesis.parsers' + '.' + name)
                for name_attr in dir(module):
                    if name_attr == "parse":
                        self.supported_parsers[name.split("_", 1)[1]] = getattr(module, name_attr)


def user_info_data(data):
    return {'user_id': data['user_id'],
            'user_name': data['user_name'],
            'birthday': data['birthday'],
            'gender': data['gender']}


def run_parser(parser_name, data):
    main_parser = Parser()
    parser = main_parser.supported_parsers[parser_name]
    if parser is not None:
        return parser(data)
    else:
        return