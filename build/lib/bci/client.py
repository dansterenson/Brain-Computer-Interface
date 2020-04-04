
from .utils import Connection
from .utils import Hello
from .utils import Config


def upload_snapshot(address, reader):
    ip_address, port = address.split(":")
    user = reader.user
    hello = Hello(user)
    serial = hello.serialize()

    for snapshot in reader:
        with Connection.connect(ip_address, int(port)) as connection:
            connection.send_message(serial)
            config = Config.deserialize(connection.receive_message())
            snapshot = snapshot.serialize(config.fields)
            connection.send(snapshot)


