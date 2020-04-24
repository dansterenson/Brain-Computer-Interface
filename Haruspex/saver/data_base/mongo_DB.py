import pymongo


class MongoDB:
    def __init__(self, mongo_url):
        client = pymongo.MongoClient(mongo_url)
        self.db = client.db

    def save_user(self, data):
        user_id = data['user_id']
        self.db['users'].update_one({'user_id': user_id},
                                    {'$set': data},
                                    upsert=True)

    def save_snapshot(self, user, timestamp, snapshot):
        user_id = user['user_id']
        snapshot['user_id'] = user_id
        snapshot['timestamp'] = timestamp
        self.db['snapshots'].update_one({'user_id': user_id, 'timestamp': timestamp, 'results': snapshot['results']},
                                        {'$set': snapshot},
                                        upsert=True)

    def get_users(self):
        return list(self.db["users"].find({}, {'_id': 0}))

    def get_user(self, user_id):
        return list(self.db["users"].find({'user_id': int(user_id)}, {'_id': 0}))

    def get_user_snapshots(self, user_id):
        return list(self.db["snapshots"].find({'user_id': int(user_id)}))

    def get_snapshot_by_id(self, user_id, snapshot_id):
        return list(self.db['snapshots'].find({"user_id": int(user_id), "timestamp": int(snapshot_id)}))

    def get_snapshot_by_result(self, user_id, snapshot_id, result_name):
        return list(self.db['snapshots'].find({"user_id": int(user_id), "timestamp": int(snapshot_id), "results": result_name}))

