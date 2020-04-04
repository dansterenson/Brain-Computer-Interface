import json

from readers.haruspex_pb2 import Combined as CombinedProto
from flask import request
from flask import Flask, make_response
from .msg_queue import MessageQueue
from Haruspex.utils.load_save_data import LoadSaveData

app = Flask(__name__)
mq_url = None
publish_func = None


def json_for_publish(user, snapshot):
    translation = (snapshot.pose.translation.x,
                   snapshot.pose.translation.y,
                   snapshot.pose.translation.z)

    rotation = (snapshot.pose.rotation.x,
                snapshot.pose.rotation.y,
                snapshot.pose.rotation.z,
                snapshot.pose.rotation.w)

    color_w, color_h, color_d = (snapshot.color_image.width,
                                 snapshot.color_image.height,
                                 snapshot.color_image.data)

    depth_w, depth_h, depth_d = (snapshot.depth_image.width,
                                 snapshot.depth_image.height,
                                 snapshot.depth_image.data)

    feelings = (snapshot.feelings.hunger,
                snapshot.feelings.thirst,
                snapshot.feelings.exhaustion,
                snapshot.feelings.happiness)

    color_created_path = LoadSaveData(user.user_id, snapshot.datetime, 'color_image')
    depth_created_path = LoadSaveData(user.user_id, snapshot.datetime, 'depth_image')

    color_created_path.save_to_file('color_image_data', color_d)
    depth_created_path.save_to_file('depth_image_data', str(depth_d).encode())

    j_data = json.dumps({
        'user_id': user.user_id,
        'user_name': user.username,
        'birthday': user.birthday,
        'gender': user.gender,
        'timestamp': snapshot.datetime,
        'translation': translation,
        'rotation': rotation,
        'color_image': [color_w, color_h, str(color_created_path).join('/color_image_data')],
        'depth_image': [depth_w, depth_h, str(depth_created_path).join('/depth_image_data')],
        'feelings': feelings})
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
