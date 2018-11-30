

class Listener:

    def __init__(self, listeners):
        self._listeners = listeners

    def get_listeners(self, event):
        if event in self._listeners.keys():
            return self._listeners[event]
