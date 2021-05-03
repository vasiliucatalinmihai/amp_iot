
from src.app import AmpApp
from src.lib.framework.server import Server


class AmplifierMain:

    def __init__(self):
        self._application = AmpApp

        self._object_manager = self._application.get_object_manager()
        self._config = self._object_manager.get('src.lib.storage.Storage')

        # self._key_driver = self._object_manager.get('amp_iot.src.driver.key.Key')
        #
        # self._app_server = Server(
        #     self._application,
        #     self._config.get_config('amplifier_client')['host'],
        #     self._config.get_config('amplifier_client')['port'],
        #     True
        # )

        pre = self._object_manager.get('src.driver.tda7419_data.Tda7419Data')
        spec = self._object_manager.get('src.driver.spectrum.Spectrum')


    # def run(self):
    #     self._app_server.start()
    #     self._key_driver.start()
