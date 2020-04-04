import socket
import contextlib
import struct


class Connection:
    def __init__(self, socket_obj):
        self.socket = socket_obj

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.socket.close()


    @classmethod
    @contextlib.contextmanager
    def connect(cls, given_ip_add, given_port):
        try:
            sock = socket.socket()
            sock.connect((given_ip_add, given_port))
            yield Connection(sock)
        finally:
            pass

    def __repr__(self):
        sending_add = self.socket.getsockname()
        s_ip_address = sending_add[0]
        s_port = sending_add[1]
        rec_add = self.socket.getpeername()
        r_ip_address = rec_add[0]
        r_port = rec_add[1]
        return f"<Connection from {s_ip_address}:{s_port} to {r_ip_address}:{r_port}>"

    def send(self, data):
        self.socket.sendall(data)

    def send_message(self, message_in_bytes):
        len_msg = struct.pack('I', len(message_in_bytes))
        self.socket.sendall(len_msg)
        self.send(message_in_bytes)

    def receive(self, size):
        data = bytearray()
        while len(data) < size:
            mes = self.socket.recv(size - len(data))
            if not mes:
                raise Exception
            data.extend(mes)
        return bytes(data)

    def receive_message(self):
        print("1")
        (msg_size, ) = struct.unpack('I', self.receive(struct.calcsize('I')))
        print("2")
        return self.receive(msg_size)
