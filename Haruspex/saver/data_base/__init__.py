import pkgutil
from os.path import dirname
from importlib import import_module
from .data_base import DataBase

supported_dbs = {}

pwd = dirname(__file__)
for (_, name, _) in pkgutil.iter_modules([pwd]):
    if name.startswith('parse_'):
        import_module('parsers' + '.' + name)

        #for key, db in module.__dict__.items():
        #    if isinstance(db, type) and db.__name__.endswith("DB"):
        #        supported_dbs[db.prefix] =