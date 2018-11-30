
from amp_iot.src.lib.jsonsocket import Client


class AmpClient:

    def __init__(self, storage, client: Client):
        self._storage = storage
        self._host = self._storage.get_config('amp_server')['host']
        self._port = self._storage.get_config('amp_server')['port']
        self._client = client

    def send(self, path, request_data):
        self._client.connect(self._host, self._port)
        self._client.send({'path': path, 'data': request_data})
        response = self._client.recv()
        self._client.close()

        return response
