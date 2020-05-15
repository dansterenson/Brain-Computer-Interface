from urllib.parse import urlparse
import pkgutil
from os.path import dirname
from importlib import import_module


class DataBase:
    def __init__(self, data_base_url):
        self.supported_db = {}
        self.load_all_db()
        self.db_type = self.get_db(data_base_url)

    def save_user(self, user):
        self.db_type.save_user(user)

    def save_snapshot(self, user, timestamp, snapshot, result_name):
        self.db_type.save_snapshot(user, timestamp, snapshot, result_name)

    def get_users(self):
        return self.db_type.get_users()

    def get_user(self, user_id):
        return self.db_type.get_user(user_id)

    def get_user_snapshots(self, user_id):
        return self.db_type.get_user_snapshots(user_id)

    def get_snapshot_by_id(self, user_id, snapshot_id):
        return self.db_type.get_snapshot_by_id(user_id, snapshot_id)

    def get_snapshot_by_result(self, user_id, snapshot_id, result_name):
        return self.db_type.get_snapshot_by_result(user_id, snapshot_id, result_name)

    def get_user_feelings(self, user_id):
        return self.db_type.get_user_feelings(user_id)

    def load_all_db(self):
        pwd = dirname(__file__)
        for (_, name, _) in pkgutil.iter_modules([pwd]):
            if name.endswith('db'):
                module = import_module('Noesis.data_base' + '.' + name)
                for name_attr in dir(module):
                    if name_attr.endswith("DB"):
                        self.supported_db[name] = getattr(module, name_attr)

    def get_db(self, url):
        parsed_url = urlparse(url)
        for scheme in self.supported_db.keys():
            if parsed_url.scheme == scheme:
                found_db = self.supported_db[scheme]
                return found_db
        raise ValueError(f'url is invalid: {url}')

