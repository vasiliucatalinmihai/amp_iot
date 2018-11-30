

class AbstractController:

    _params = {}

    def set_params(self, params):
        self._params = params

        return self

    def get_params(self):
        return self._params

    def get_param(self, key, value=False):
        if key in self._params.keys():
            value = self._params[key]

        return value
