from flask import request
from flask import Flask, make_response
from ..readers.protobuf_pb2 import Combined as CombinedProto
from .utils.msg_publish import json_for_publish
from .utils.logger import create_logger


app = Flask(__name__)


@app.route('/upload_snapshot', methods=['POST'])
def load():
    app.logger.info(f'Server received snapshot')
    app.logger.debug(f'Server received snapshot: {request.data}')
    combined_from_proto = CombinedProto()
    combined_from_proto.ParseFromString(request.data)
    message_to_mq = json_for_publish(combined_from_proto.user, combined_from_proto.snapshot)
    app.config["PUBLISH_FUNC"](message_to_mq)
    app.logger.info('snapshot was sent to publish function by the server')
    return make_response('ok', 200)


def run_server(ip_address, port, publish_function):
    app.config["PUBLISH_FUNC"] = publish_function
    app.logger.addHandler(create_logger("server"))
    app.run(ip_address, port, threaded=True)
