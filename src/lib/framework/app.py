import logging

from src.lib.framework.listener import Listener
from src.lib.framework.object_manager import ObjectManager
from src.lib.framework.router import Router

logging.getLogger().setLevel(logging.DEBUG)


class App:

    APP_NAME = "none"
    USE_THREADS_FOR_DISPATCH = True


    app_config = {
        'object_manager': {},
        'router': {},
        'listeners': {},
    }

    object_manager = ObjectManager(app_config['object_manager'])
    router = Router(app_config['router'])
    listener = Listener(app_config['listeners'])

    @classmethod
    def get_router(cls) -> Router:
        return cls.router

    @classmethod
    def get_object_manager(cls) -> ObjectManager:
        return cls.object_manager

    @classmethod
    def get_listener(cls) -> Listener:
        return cls.listener

    @classmethod
    def dispatch(cls, event, args):
        if cls.USE_THREADS_FOR_DISPATCH:
            cls.listener.dispatch(cls.get_object_manager(), event, args)

            return

        listeners = cls.listener.get_listeners(event)

        if not listeners:
            return

        event = type('event', (object,), args)

        for class_name in listeners.keys():
            try:
                listener = cls.object_manager.get(class_name)
            except Exception as ex:
                logging.exception(str(ex))
                continue

            action_name = listeners[class_name]

            if hasattr(listener, action_name) and callable(getattr(listener, action_name)):
                action = getattr(listener, action_name)

                action(event)

    @classmethod
    def run(cls, request):
        try:
            cls.router.validate_request(request)
        except Exception as ex:
            return cls.APP_NAME + '---' + str(ex)

        controller_name = cls.router.get_controller(request)
        action_name = cls.router.get_action(request)

        try:
            controller = cls.object_manager.get(controller_name)
        except Exception as ex:
            return cls.APP_NAME + '---' + str(ex)

        if hasattr(controller, action_name) and callable(getattr(controller, action_name)):
            controller.set_params(cls.router.get_params(request))
            action = getattr(controller, action_name)

            try:
                response = action()
            except Exception as ex:
                return cls.APP_NAME + '---' + str(ex)

            return response

        return 'Controller ' + controller_name + ' has no action ' + action_name
