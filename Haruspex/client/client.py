from .utils import Connection
from .readers import Reader
from .readers import ProtoReader
#from .utils.client_server_protocol import serialize
import requests
from .readers import haruspex_pb2


def upload_sample(address, file_path, reader_type=ProtoReader):
    host, port = address
    reader = Reader(file_path, reader_type)

    with reader as reader:
        for snapshot in reader:
            user = reader.user  # proto1
            combined = haruspex_pb2.Combined(user=user, snapshot=snapshot).SerializeToString()
            res = requests.post(f'http://{host}:{port}/upload_snapshot', data=combined)
            x = 5
            #ith Connection.connect(host, int(port)) as connection:
            #   print("enter client")
            #   user = reader.user  # proto1
            #   #hello = Hello(user)
            #   serial = serialize(user)
            #   print(serial)
            #   print("sending hello message")
            #   connection.send_message(serial)
            #   print("hello message sent")
            #   #config_from_server = connection.receive_message()
            #   #config = Config.deserialize(config_from_server)
            #   #print("Config message received = " + str(config))
            #   #snapshot_serial = snapshot.serialize(config.fields)
            #   snapshot_serial = serialize(snapshot)
            #   print("sending snapshot message")
            #   connection.send_message(snapshot_serial)
            #   print("snapshot message sent")

