#import datetime as dt
#import struct
#import threading
#from ..utils import Listener
#from ..utils import Hello
#from ..utils import Config
#from ..utils import Snapshot
#from ..parsers import AddParser
#from ..utils import LoadSaveData
#import json
#from ..utils.client_server_protocol import deserialized_snapshot
#from ..utils.client_server_protocol import deserialized_user
#
#
#_SERVER_BACKLOG = 1000
#_HEADER_FORMAT = 'QQI'
#_HEADER_SIZE = struct.calcsize(_HEADER_FORMAT)
#
#
#def _format_timestamp(timestamp):
#    datetime = dt.datetime.fromtimestamp(timestamp)
#    return f'{datetime:%Y-%m-%d_%H-%M-%S}'
#
#
#def _receive_all(connection, size):
#    chunks = []
#    while size > 0:
#        chunk = connection.recv(size)
#        if not chunk:
#            raise RuntimeError('incomplete data')
#        chunks.append(chunk)
#        size -= len(chunk)
#    return b''.join(chunks)
#
#
#def json_for_publish(user, snapshot):
#    color_w, color_h, color_d = snapshot.img
#    depth_w, depth_h, depth_d = snapshot.depth_img
#    color_created_path = LoadSaveData(user.id, snapshot.timestamp, 'color_image')
#    depth_created_path = LoadSaveData(user.id, snapshot.timestamp, 'depth_image')
#    print("COLORRRRRRRRRRRR DATAAAAAAAA")
#    print(color_d.type())
#    color_created_path.save_to_file('color_image_data', color_d)
#    depth_created_path.save_to_file('depth_image_data', depth_d)
#
#    j_data = json.dumps({
#        'user_id': user.id,
#        'user_name': user.name,
#        'birthday': user.birth_date,
#        'gender': user.gender,
#        'timestamp': snapshot.timestamp,
#        'translation': snapshot.translation,
#        'rotation': snapshot.rotation,
#        'color_image': [color_w, color_h, str(color_created_path).join('/color_image_data')],
#        'depth_image': [depth_w, depth_h, str(depth_created_path).join('/depth_image_data')],
#        'feelings': snapshot.feelings})
#    return j_data
#
#
#class Handler(threading.Thread):
#    lock = threading.Lock()
#
#    def __init__(self, connection, publish_function):
#        super().__init__()
#        self.connection = connection
#        self.publish_function = publish_function
#
#    def run(self):
#        with self.connection:
#            received_message = self.connection.receive_message()
#            #hello_obj = Hello.deserialize(received_message)
#            user = deserialized_user(received_message)
#            print("Hello " + str(user))
#            parsers_can_handles = list(AddParser.parsers_dict.keys())
#            #print("list of parsers that the server can handle " + str(parsers_can_handles))
#            #config = Config(parsers_can_handles)
#            #config_message = Config.serialize(config)
#            #print("sending config message")
#            #self.connection.send_message(config_message)
#            #print("config message sent")
#            snapshot = self.connection.receive_message()
#            snapshot = deserialized_snapshot(snapshot)
#            Handler.lock.acquire()
#            try:
#                message_to_mq = json_for_publish(user, snapshot)
#                self.publish_function(message_to_mq)
#            finally:
#                Handler.lock.release()
#            print("message sent to mq")
#
#
#def run_server(ip_address, port, publish_function=print):
#
#    with Listener(ip_address, int(port)) as listener:
#        while True:
#            print("Waiting for message")
#            connection = listener.accept()
#            print("Server connected")
#            handler = Handler(connection, publish_function)
#            handler.start()

#cur_path = os.path.dirname(__file__)
#good = 'sample.mind'
#good1 = os.path.join(cur_path, 'tmp_server')
#good2 = os.path.join(cur_path, good)
#
#if __name__ == '__main__':
#    print(os.getcwd())
#    run_server('127.0.0.1:1234', good2)
