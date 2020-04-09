from Haruspex.server.msg_queue import MessageQueue
from .data_base import DataBase
import json


class Saver:
    def __init__(self, data_base_url):
        self.db = DataBase(data_base_url)

    def save(self, data_from_file):
        data = json.loads(data_from_file)
        user = data['user_info']
        self.db.save_user(user)
        data = data['data']
        self.db.save_snapshot(data)



        if self.db[user_id] is None:
            self.db.save_user(data)

        self.db.save_snapshot(data)









