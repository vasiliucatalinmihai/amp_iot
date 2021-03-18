
from src.lib.framework.client import Client


class ClientFactory:

    def __call__(self, object_manager, name):
        storage = object_manager().get('amp_iot.src.lib.storage.Storage')

        host = storage.get_config(name)['host']
        port = storage.get_config(name)['port']

        return Client(host, port)
