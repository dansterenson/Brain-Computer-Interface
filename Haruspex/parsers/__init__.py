import inspect
import pkgutil
from os.path import dirname
from importlib import import_module


def add_to_parser_list(parser_name):
    def decorator(parser):
        # parser is either a class or a function
        if inspect.isclass(parser):
            parsers_dict[parser_name] = parser.parse
        elif inspect.isfunction(parser):
            parsers_dict[parser_name] = parser
        else:
            raise Exception
        return parser
    return decorator


parsers_dict = {}


pwd = dirname(__file__)
for (_, name, _) in pkgutil.iter_modules([pwd]):
    if name.startswith('parse_'):
        import_module('parsers' + '.' + name)