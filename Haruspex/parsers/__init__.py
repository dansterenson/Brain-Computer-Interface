import pkgutil
from os.path import dirname
from importlib import import_module
from .add_parser import AddParser
from .main_parser import MainParser
from .add_parser import run_parser

pwd = dirname(__file__)
for (_, name, _) in pkgutil.iter_modules([pwd]):
    if name.startswith('parse'):
        import_module('.' + name, package=__name__)



