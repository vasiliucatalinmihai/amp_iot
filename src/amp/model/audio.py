
from amp_iot.src.lib.audio_map import AudioMap
from amp_iot.src.amp.driver.preamp import Preamp


class Audio:

    def __init__(self, preamp_driver: Preamp, audio_map: AudioMap):
        self._preamp_driver = preamp_driver
        self._audio_map = audio_map

    def process(self, data):
        try:
            function_map = self._audio_map.getFunc(data['name'])
        except Exception as ex:
            return str(ex)

        return self._call_method(data, function_map)

    # call method on preamp driver
    def _call_method(self, data, function_map):
        func = getattr(self._preamp_driver, function_map['name'])
        params = dict()
        for i in data['params']:
            params[data['params'][i]['name']] = data['params'][i]['value']

        try:
            return_data = func(**params)
        except Exception as ex:
            return_data = str(ex)

        if type(return_data) == type(self._preamp_driver):
            return_data = True

        return return_data

    def method(self, event):
        print(event.param1)