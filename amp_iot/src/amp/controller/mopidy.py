
from amp_iot.src.lib.framework.abstract_controller import AbstractController
from amp_iot.src.amp.model.audio import Audio
from amp_iot.src.amp.model.light.light_controller import LightController
from amp_iot.src.lib.storage import Storage


class MopidyController(AbstractController):

    def __init__(
            self,
            audio_model: Audio,
            light_controller: LightController,
            storage: Storage
    ):
        self._audio_model = audio_model
        self._light_controller = light_controller
        self._storage_adapter = storage

    def audio_option_action(self):
        method_name = self.get_param('method_name')
        args = self.get_param('args')
        ret = self._audio_model.process_external_call(method_name, args)

        if method_name[0:3] == 'set':
            self._light_controller.change_low_mode('mopidy_set')

        return ret
