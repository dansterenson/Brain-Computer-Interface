import socket
from .connection import Connection


class Listener:
    def __init__(self, host='0.0.0.0', port=0, backlog=1000, reuseaddr=True):
        self.server = None
        self.port = port
        self.host = host
        self.backlog = backlog
        self.reuseaddr = reuseaddr

    def __repr__(self):
        return f"Listener(port={self.port}, host='{self.host}', backlog={self.backlog}, reuseaddr={self.reuseaddr})"

    def accept(self):
        try:
            conn, address = self.server.accept()
            return Connection(conn)
        except Exception as e:
            return e

    def __enter__(self):
        self.start()
        return self

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.reuseaddr:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        server.listen(self.backlog)
        self.server = server

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def stop(self):
        self.server.close()

