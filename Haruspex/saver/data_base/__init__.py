import pkgutil
from os.path import dirname
from importlib import import_module
from .data_base import DataBase

supported_dbs = {}

pwd = dirname(__file__)
for (_, name, _) in pkgutil.iter_modules([pwd]):
    if name.endswith('_DB'):
        import_module('saver.data_base' + '.' + name)
