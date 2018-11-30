
from amp_iot.src.app.amp_client import AmpClient
from amp_iot.src.lib.audio_map import AudioMap


class Audio:

    AUDIO_PROCESS_PATH = 'audio/process'

    def __init__(self, audio_map: AudioMap, amp_client: AmpClient):
        self._audio_map = audio_map
        self._amp_client = amp_client

    def send_to_amp(self, method_name, args):
        audio_request = dict()
        function_definition = self._audio_map.getFunc(method_name)
        audio_request['name'] = function_definition['name']
        params = dict()
        param_count = 0
        for param in function_definition['params']:
            params[param_count] = dict()
            params[param_count]['name'] = param
            params[param_count]['value'] = int(args[param_count])
            param_count += 1

        audio_request['params'] = params

        request_data = {'audio_request': audio_request}

        return self._amp_client.send(self.AUDIO_PROCESS_PATH, request_data)
