

from amp_iot.src.lib.framework.abstract_controller import AbstractController
from amp_iot.src.amp.model.audio import Audio


class AudioController(AbstractController):

    def __init__(self,  audio_model: Audio):
        self._audio_model = audio_model

    def process_action(self):
        data = self.get_param('audio_request')
        return self._audio_model.process(data)
