
from amp_iot.src.lib.storage import Storage

from amp_iot.src.amp.driver.led_strip import LedStrip
from amp_iot.src.amp.model.light.light_controller import LightController


class Light:

    def __init__(
        self,
        storage_adapter: Storage,
        light_controller: LightController
    ):
        self._storage_adapter = storage_adapter
        self._light_controller = light_controller

        self._effects = self._storage_adapter.get_config('light_effect')

        self._encoder_mode_default = self._storage_adapter.get_config('default_lights_encoder')
        self._low_mode_default = self._storage_adapter.get_config('default_lights_low')

        self._encoder_mode = self._encoder_mode_default
        self._low_mode = self._low_mode_default

    def change_volume(self, value):
        self._light_controller.change_volume(value)

    def change_bass(self, value):
        self._light_controller.change_bass(value)

    def change_treble(self, value):
        self._light_controller.change_treble(value)

    def change_middle(self, value):
        self._light_controller.change_middle(value)

    def change_encoder_mode(self, mode):
        if mode not in self._effects.keys():
            self._encoder_mode = self._encoder_mode_default
        else:
            self._encoder_mode = mode

        self._light_controller.change_encoder_mode(self._encoder_mode)

        return self

    def change_low_mode(self, mode):
        if mode not in self._effects.keys():
            self._low_mode = self._low_mode_default
        else:
            self._low_mode = mode

        self._light_controller.change_low_mode(self._low_mode)

        return self
