from flask import request
from flask import Flask, make_response
from ..readers.protobuf_pb2 import Combined as CombinedProto
from .utils.msg_publish import json_for_publish

app = Flask(__name__)


@app.route('/upload_snapshot', methods=['POST'])
def load():
    combined_from_proto = CombinedProto()
    combined_from_proto.ParseFromString(request.data)
    message_to_mq = json_for_publish(combined_from_proto.user, combined_from_proto.snapshot)
    app.config["PUBLISH_FUNC"](message_to_mq)
    return make_response('ok', 200)


def run_server(ip_address, port, publish_function):
    app.config["PUBLISH_FUNC"] = publish_function
    app.run(ip_address, port, threaded=True)