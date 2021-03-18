import threading
import logging


logging.getLogger().setLevel(logging.DEBUG)


class Listener:

    def __init__(self, listeners):
        self._listeners = listeners

    def get_listeners(self, event):
        if event in self._listeners.keys():
            return self._listeners[event]

    def dispatch(self, object_manager, event, args):
        listeners = self.get_listeners(event)

        if not listeners:
            return

        event = type('event', (object,), args)

        for class_name in listeners.keys():
            try:
                listener = object_manager.get(class_name)
            except Exception as ex:
                logging.exception(str(ex))
                continue

            action_name = listeners[class_name]

            if hasattr(listener, action_name) and callable(getattr(listener, action_name)):
                action = getattr(listener, action_name)

                listener.lock = threading.Lock()
                listener_thread = threading.Thread(target=action, args=(), kwargs={'event': event})

                listener.lock.acquire()
                listener_thread.start()
                listener.lock.release()

                # action(event)
