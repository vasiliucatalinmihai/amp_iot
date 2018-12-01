
from amp_iot.src.lib.framework.abstract_controller import AbstractController
from amp_iot.src.app.model.audio import Audio


class MopidyController(AbstractController):

    def __init__(self, audio_model: Audio):
        self._audio_model = audio_model

    def audio_option_action(self):
        method_name = self.get_param('method_name')
        args = self.get_param('args')
        self._audio_model.send_to_amp(method_name, args)
