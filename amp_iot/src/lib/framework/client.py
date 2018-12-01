
from amp_iot.src.lib.jsonsocket import AbstractClient


class Client:

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._client = AbstractClient()

    def send(self, path, request_data):
        self._client.connect(self._host, self._port)
        self._client.send({'path': path, 'data': request_data})
        response = self._client.recv()
        self._client.close()

        return response
