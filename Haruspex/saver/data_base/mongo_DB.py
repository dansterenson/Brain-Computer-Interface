import pymongo


class MongoDB:
    def __init__(self, mongo_url):
        client = pymongo.MongoClient(mongo_url)
        self.db = client.db

    def save_user(self, data):
        user_id = data['user_info']['user_id']
        self.db['users'].update_one({'user_id': user_id},
                                    {'$set': data},
                                    upsert=True)

    def save_snapshot(self, data):
        user_id = data['user_info']['user_id']
        timestamp = data['timestamp']
        self.db['users'].update_one({'user_id': user_id, 'timestamp': timestamp},
                                    {'$set': data})

    def get_users(self):
        self.db.get_users()

    def get_user(self, user_id):
        self.db.get_user(user_id)

    def get_user_snapshots(self, user_id):
        self.db.get_user_snapshots(user_id)

    def get_snapshots(self, user_id, snapshot_id):
        self.db.get_snapshots(user_id, snapshot_id)
