from .mongo_DB import MongoDB
from urllib.parse import urlparse
import pymongo

supported_db = {'mongodb': MongoDB}

def get_db(url):
    parsed_url = urlparse(url)
    for scheme in supported_db.keys():
        if parsed_url.scheme == scheme:
            found_mq = supported_db[scheme]
            return found_mq
    raise ValueError(f'url is invalid: {url}')


class DataBase:
    def __init__(self, data_base_url):
        self.db = get_db(data_base_url)

    def save_user(self, user):
        self.db.save_user(user)

    def save_snapshot(self, snapshots):
        self.db.save_snapshot(snapshots)

    def get_users(self):
        self.db.get_users()

    def get_user(self, user_id):
        self.db.get_user(user_id)

    def get_user_snapshots(self, user_id):
        self.db.get_user_snapshots(user_id)

    def get_snapshots(self, user_id, snapshot_id):
        self.db.get_snapshots(user_id, snapshot_id)

