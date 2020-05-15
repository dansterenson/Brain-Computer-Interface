from ..data_base import DataBase


class Saver:
    def __init__(self, data_base_url):
        self.db = DataBase(data_base_url)

    def save(self, topic_name, data):
        user = data['user_info']
        self.db.save_user(user)
        snapshot_data = data['data']
        self.db.save_snapshot(user, data['timestamp'], snapshot_data, topic_name)








