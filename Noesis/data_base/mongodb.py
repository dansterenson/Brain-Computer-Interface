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

    def save_snapshot(self, user, timestamp, snapshot, parser_name):
        user_id = user['user_id']
        self.db['snapshots'].insert({'user_id': user_id, 'timestamp': timestamp, 'parser_type': parser_name})

        self.db['snapshots'].update_one({'user_id': user_id, 'timestamp': timestamp, 'parser_type': parser_name},
                                        {'$set': {"parsed_data": snapshot}},
                                        upsert=True)

    def get_users(self):
        return list(self.db["users"].find({}, {'_id': 0}))

    def get_user(self, user_id):
        return list(self.db["users"].find({'user_id': int(user_id)},
                                          {'_id': 0}))

    def get_user_snapshots(self, user_id):
        return list(self.db["snapshots"].find({'user_id': int(user_id)},
                                              {'_id': 0}))

    def get_snapshot_by_id(self, user_id, snapshot_id):
        return list(self.db['snapshots'].find({"user_id": int(user_id),
                                               "timestamp": int(snapshot_id)},
                                              {'_id': 0}))

    def get_snapshot_by_result(self, user_id, snapshot_id, result_name):
        return list(self.db['snapshots'].find({"user_id": int(user_id),
                                               "timestamp": int(snapshot_id),
                                               "parser_type": result_name},
                                              {'_id': 0}))

    def get_user_feelings(self, user_id):
        res_list = []
        snapshots = list(self.db['snapshots'].find({"user_id": int(user_id), "parser_type": "feelings"}, {'_id': 0}))
        for snap in snapshots:
            res_list.append({'timestamp': snap['timestamp'], 'feelings_at_timestamp': snap['parsed_data']})
        return res_list
