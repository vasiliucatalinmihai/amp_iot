import logging
import threading

from src.lib.jsonsocket import AbstractServer


class Server:

    def __init__(
            self,
            application,
            host,
            port,
            use_threading=1
    ):

        self.__application = application
        self._host = host
        self._port = port
        self._use_threading = use_threading

        self._isAlive = False

        if self._use_threading:
            self._listenThread = threading.Thread(target=self._listen, args=())
            logging.getLogger().setLevel(logging.ERROR)
            self._lock = threading.Lock()

    def start(self):
        self._isAlive = True

        if self._use_threading:
            self._listenThread.daemon = True
            self._listenThread.start()
        else:
            self._listen_no_thread()

    def stop(self):
        self._isAlive = False

    def _listen_no_thread(self):
        server = AbstractServer(self._host, self._port)

        while self._isAlive:
            server.accept()
            data = server.recv()
            logging.debug(data)
            response = self.__application.run(data)
            logging.debug(response)
            server.send(response)

        server.close()

    def _listen(self):
        server = AbstractServer(self._host, self._port)

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
