# @rebootstr

import socket
import sys


class HTTPClient:

    def __init__(self, host='localhost'):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, 8081)
        self.sock.connect(server_address)

    def send(self, message):
        self.sock.sendall(message.encode("utf-8"))
        self.sock.close()
