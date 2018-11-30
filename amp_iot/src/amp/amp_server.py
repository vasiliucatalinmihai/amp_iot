from amp_iot.src.lib.jsonsocket import Server
from amp_iot.src.lib.framework.app import App

import logging
import threading


class AmpServer:

    USE_THREADING = 1

    def __init__(self):

        self.__application = App()
        storage = self.__application.get_object_manager().get('amp_iot.src.lib.storage.Storage')

        self._host = storage.get_config('amp_server')['host']
        self._port = storage.get_config('amp_server')['port']

        self._isAlive = False

        if self.USE_THREADING:
            self._listenThread = threading.Thread(target=self._listen, args=())
            logging.getLogger().setLevel(logging.ERROR)
            self._lock = threading.Lock()

    def start(self):
        self._isAlive = True

        if self.USE_THREADING:
            self._listenThread.daemon = True
            self._listenThread.start()
        else:
            self._listen_no_thread()

    def stop(self):
        self._isAlive = False

    def _listen_no_thread(self):
        server = Server(self._host, self._port)

        while self._isAlive:
            server.accept()
            data = server.recv()
            logging.debug(data)
            response = self.__application.run(data)
            logging.debug(response)
            server.send(response)

        server.close()

    def _listen(self):
        server = Server(self._host, self._port)

        while self._isAlive:
            self._lock.acquire()
            server.accept()
            data = server.recv()
            logging.debug(data)
            response = self.__application.run(data)
            logging.debug(response)
            server.send(response)
            self._lock.release()

        server.close()

    def __del__(self):
        self._isAlive = False
