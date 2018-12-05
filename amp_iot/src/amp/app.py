
from amp_iot.src.lib.framework.object_manager import ObjectManager
from amp_iot.src.lib.framework.router import Router
from amp_iot.src.lib.framework.app import App
from amp_iot.src.lib.framework.listener import Listener

from amp_iot.src.amp.app_config import ApplicationConfig


class AmpApp(App):
    APP_NAME = 'amplifier'

    app_config = ApplicationConfig.get_application_config()

    object_manager = ObjectManager(app_config['object_manager'])
    router = Router(app_config['router'])
    listener = Listener(app_config['listeners'])
