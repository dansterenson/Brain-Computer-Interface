import socket
import contextlib


class Connection:
    def __init__(self, socket_obj: socket.socket):
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

    def receive(self, size):
        recv_lst = []
        received_len = 0
        while True:
            received_bytes = self.socket.recv(size)
            if len(received_bytes) == 0:  # connection was closed
                raise Exception
            recv_lst.append(received_bytes)
            if (len(received_bytes) + received_len) >= size:
                break
            size = size - len(received_bytes)

        return b"".join(recv_lst)  # Joining byte list with python
