
from amp_iot.src.app import AmpApp
from amp_iot.src.lib.framework.server import Server


class AmplifierMain:

    def __init__(self):
        self._application = AmpApp

        self._object_manager = self._application.get_object_manager()
        self._config = self._object_manager.get('amp_iot.src.lib.storage.Storage')

        power_model = self._object_manager.get('amp_iot.src.amp.model.power.Power')
        power_model.power_on(False)

        self._key_driver = self._object_manager.get('amp_iot.src.amp.driver.key.Key')

        self._app_server = Server(
            self._application,
            self._config.get_config('amplifier_client')['host'],
            self._config.get_config('amplifier_client')['port'],
            True
        )

    def run(self):
        self._app_server.start()
        self._key_driver.start()
