
import time

from amp_iot.src.driver import Key
from amp_iot.src.driver import Preamp
from amp_iot.src.model import Light
from amp_iot.src.lib.storage import Storage


class KeyAudio:

    CONTROL_VOLUME = 0
    CONTROL_BASS = 1
    CONTROL_TREBLE = 2
    CONTROL_MIDDLE = 3

    CONTROL_MAX = 4

    TIME_TO_RESET_TO_VOLUME = 3

    def __init__(
        self,
        storage_adapter: Storage,
        preamp_driver: Preamp,
        light_model: Light
    ):
        self._storage_adapter = storage_adapter
        self._preamp_driver = preamp_driver
        self._light_model = light_model

        self.MAX_VOL_STEP = self._storage_adapter.get_config('max_vol_step')
        self._is_active = 1
        self._last_volume_value = 1
        self._control = {
            'control': self.CONTROL_VOLUME,
            'timestamp': time.time()
        }

    def key_observer(self, event):
        if not self.is_active():
            return

        if event.action_type == Key.ENCODER_VALUE:
            self._change_preamp(event.value)
            self._control['timestamp'] = time.time()
            return

        if event.action_type == Key.ENCODER_BTN:
            if event.value == Key.RELEASED:
                self._change_control()
            return

        if event.action_type == Key.MUTE_BTN:
            if event.value == Key.RELEASED:
                self._change_input()
            return

    def _change_control(self):
        self._control['control'] += 1
        if self._control['control'] >= self.CONTROL_MAX:
            self._control['control'] = self.CONTROL_VOLUME

        self._control['timestamp'] = time.time()

    def _get_control(self):
        if (time.time() - self._control['timestamp']) > self.TIME_TO_RESET_TO_VOLUME:
            self._control['control'] = self.CONTROL_VOLUME

        return self._control['control']

    def is_active(self):
        return self._is_active

    def activate(self):
        self._is_active = 1

    def deactivate(self):
        self._is_active = 0

    def _change_preamp(self, value):
        value = self._limit_volume_value(value)

        if self._get_control() == self.CONTROL_VOLUME:
            self._change_volume(value)
        elif self._get_control() == self.CONTROL_BASS:
            self._change_bass(value)
        elif self._get_control() == self.CONTROL_TREBLE:
            self._change_treble(value)
        elif self._get_control() == self.CONTROL_MIDDLE:
            self._change_middle(value)

    def _change_volume(self, value):
        value = self._preamp_driver.getMainVolume() + value
        self._preamp_driver.setMainVolume(value, 1)

        self._light_model.change_volume(self._preamp_driver.getMainVolume())

    def _change_bass(self, value):
        value = self._preamp_driver.getBass() + value
        self._preamp_driver.setBass(value, 1)

        self._light_model.change_bass(self._preamp_driver.getBass())

    def _change_treble(self, value):
        value = self._preamp_driver.getTreble() + value
        self._preamp_driver.setTreble(value, 1)

        self._light_model.change_treble(self._preamp_driver.getTreble())

    def _change_middle(self, value):
        value = self._preamp_driver.getMiddle() + value
        self._preamp_driver.setMiddle(value, 1)

        self._light_model.change_middle(self._preamp_driver.getMiddle())

    def _change_input(self):
        current_input = self._preamp_driver.getMainSource()

        if current_input == 2:
            self._preamp_driver.setMainSource(4)

        if current_input == 4:
            self._preamp_driver.setMainSource(2)

        return self

    def _limit_volume_value(self, value):
        if value > 0:
            if value > (self._last_volume_value + 3):
                value = self._last_volume_value + 3

            if value > self.MAX_VOL_STEP:
                value = self.MAX_VOL_STEP

            return int(value)

        if value < (self._last_volume_value - 3):
            value = self._last_volume_value - 3

        if value < (self.MAX_VOL_STEP * -1):
            value = (self.MAX_VOL_STEP * -1)

        return int(value)
