from ..utils import Connection
from ..utils import Hello
from ..utils import Config
from ..readers.main_reader import Reader
from ..readers.protobuff_reader import ProtoReader
from ..utils.client_server_protocol import serialize


def upload_sample(address, file_path, reader_type=ProtoReader):
    ip_address, port = address
    reader = Reader(file_path, reader_type)

    with reader as reader:
        for snapshot in reader:
            with Connection.connect(ip_address, int(port)) as connection:
                print("enter client")
                user = reader.user
                #hello = Hello(user)
                serial = serialize(user)
                print(serial)
                print("sending hello message")
                connection.send_message(serial)
                print("hello message sent")
                #config_from_server = connection.receive_message()
                #config = Config.deserialize(config_from_server)
                #print("Config message received = " + str(config))
                #snapshot_serial = snapshot.serialize(config.fields)
                snapshot_serial = serialize(snapshot)
                print("sending snapshot message")
                connection.send_message(snapshot_serial)
                print("snapshot message sent")

