import json
from flask import Flask, jsonify
from Haruspex.saver.data_base import DataBase
app = Flask(__name__)

data_base = None


def run_api_server(host, port, database_url):
    global data_base
    data_base = DataBase(database_url)
    app.run(host, port, threaded=True)


@app.route('/users', methods=['GET'])
def get_users():
    users = data_base.get_users()
    user_list = []
    for user in users:
        user_list.append({'user_id': user['user_id'], 'user_name': user['user_name']})
    return jsonify(user_list)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_base.get_user(user_id)
    return jsonify(user)


@app.route('/users/<user_id>/snapshots', methods=['GET'])
def get_snapshots(user_id):
    list_of_snapshots = []
    snapshots_of_user = data_base.get_user_snapshots(user_id)
    for snapshot in snapshots_of_user:
        list_of_snapshots.append({'snapshot_id': snapshot['timestamp']})
    return jsonify(list_of_snapshots)


@app.route('/users/<user_id>/snapshots/<snapshot_id>', methods=['GET'])
def get_snapshot(user_id, snapshot_id):
    snapshot_res = []
    snapshot = data_base.get_snapshot_by_id(user_id, snapshot_id)
    snapshot_res.append({'snapshot_id': snapshot[0]['timestamp']})
    snapshot_res.append({'date_time': snapshot[0]['timestamp']})
    snapshot_res.append({'available_results': snapshot[0]['results']})
    return jsonify(snapshot_res)