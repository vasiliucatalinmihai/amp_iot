
from src.lib.framework import ObjectManager
from src.lib.framework import Router
from src.lib.framework.app import App
from src.lib.framework import Listener

from src.app_config import ApplicationConfig


class AmpApp(App):
    APP_NAME = 'amplifier'

    app_config = ApplicationConfig.get_application_config()

    object_manager = ObjectManager(app_config['object_manager'])
    router = Router(app_config['router'])
    listener = Listener(app_config['listeners'])
