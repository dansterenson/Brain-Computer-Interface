import json

from readers.haruspex_pb2 import Combined as CombinedProto
from flask import request
from flask import Flask, make_response
from .msg_queue import MessageQueue
from Haruspex.utils.load_save_data import SaveData

app = Flask(__name__)
mq_url = None
publish_func = None


class UserWrapper:
    def __init__(self, user):

        self.user_id = user.user_id
        self.username = user.username
        self.birthday = user.birthday
        if user.gender == 1:
            self.gender = 'f'
        elif user.gender == 0:
            self.gender = 'm'
        else:
            self.gender = 'o'


class SnapshotWrapper:
    def __init__(self, snapshot):

        self.timestamp = snapshot.datetime

        self.translation = (snapshot.pose.translation.x,
                            snapshot.pose.translation.y,
                            snapshot.pose.translation.z)

        self.rotation = (snapshot.pose.rotation.x,
                         snapshot.pose.rotation.y,
                         snapshot.pose.rotation.z,
                         snapshot.pose.rotation.w)

        self.color_image = (snapshot.color_image.width,
                            snapshot.color_image.height,
                            snapshot.color_image.data)

        self.depth_image = (snapshot.depth_image.width,
                            snapshot.depth_image.height,
                            snapshot.depth_image.data)

        self.feelings = (snapshot.feelings.hunger,
                         snapshot.feelings.thirst,
                         snapshot.feelings.exhaustion,
                         snapshot.feelings.happiness)


def json_for_publish(user, snapshot):

    wrapped_user = UserWrapper(user)
    wrapped_snapshot = SnapshotWrapper(snapshot)
    color_width, color_height, color_data = wrapped_snapshot.color_image
    depth_width, depth_height, depth_data = wrapped_snapshot.depth_image

    color_data_obj = SaveData(wrapped_user.user_id, snapshot.datetime, 'color_image')
    depth_data_obj = SaveData(wrapped_user.user_id, snapshot.datetime, 'depth_image')

    color_created_path = color_data_obj.save_to_file('color_image_data', color_data)
    depth_created_path = depth_data_obj.save_to_file('depth_image_data', str(depth_data).encode())

    j_data = json.dumps({
        'user_id': wrapped_user.user_id,
        'user_name': wrapped_user.username,
        'birthday': wrapped_user.birthday,
        'gender': wrapped_user.gender,
        'timestamp': wrapped_snapshot.timestamp,
        'translation': wrapped_snapshot.translation,
        'rotation': wrapped_snapshot.rotation,
        'color_image': [color_width, color_height, color_created_path],
        'depth_image': [depth_width, depth_height, depth_created_path],
        'feelings': wrapped_snapshot.feelings})
    return j_data


def publish_function(message_to_publish):
    mq = MessageQueue(mq_url)
    mq.exchange_declaration('snapshots')
    mq.queue_publish('snapshots', '', message_to_publish)


@app.route('/upload_snapshot', methods=['POST'])
def load():
    combined_from_proto = CombinedProto()
    combined_from_proto.ParseFromString(request.data)
    message_to_mq = json_for_publish(combined_from_proto.user, combined_from_proto.snapshot)
    publish_function(message_to_mq)
    return make_response('ok', 200)


def run_server(ip_address, port, url='rabbitmq://localhost:5672', publish=publish_function):
    global mq_url
    global publish_func
    mq_url = url
    publish_func = publish
    app.run(ip_address, port, threaded=True)
