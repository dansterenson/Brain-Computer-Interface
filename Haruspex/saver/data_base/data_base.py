from .mongo_DB import MongoDB
from urllib.parse import urlparse
import pymongo

supported_db = {'mongodb': MongoDB}

def get_db(url):
    parsed_url = urlparse(url)
    for scheme in supported_db.keys():
        if parsed_url.scheme == scheme:
            found_db = supported_db[scheme]
            return found_db
    raise ValueError(f'url is invalid: {url}')


class DataBase:
    def __init__(self, data_base_url):
        db = get_db(data_base_url)
        self.db = db(data_base_url)

    def save_user(self, user):
        self.db.save_user(user)

    def save_snapshot(self, user, timestamp, snapshot):
        self.db.save_snapshot(user, timestamp, snapshot)

    def get_users(self):
        return self.db.get_users()

    def get_user(self, user_id):
        return self.db.get_user(user_id)

    def get_user_snapshots(self, user_id):
        return self.db.get_user_snapshots(user_id)

    def get_snapshot_by_id(self, user_id, snapshot_id):
        return self.db.get_snapshot_by_id(user_id, snapshot_id)

