from ..data_base import DataBase
from .utils.logger import create_logger


class Saver:
    def __init__(self, data_base_url):
        self.db = DataBase(data_base_url)

    def save(self, topic_name, data):
        #logger = create_logger("saver")
        user = data['user_info']
        self.db.save_user(user)
        snapshot_data = data['data']
        self.db.save_snapshot(user, data['timestamp'], snapshot_data, topic_name)
        #logger.info('Saver saved parsed data to db')




