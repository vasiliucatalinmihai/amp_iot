
from amp_iot.src.amp.driver.power import Power as PowerDriver
from amp_iot.src.amp.driver.power_led import PowerLed as PowerLedDriver
from amp_iot.src.amp.driver.preamp import Preamp as PreampDriver
from amp_iot.src.amp.driver.amplifier import Amplifier as AmpDriver
from amp_iot.src.amp.driver.key import Key

import time


class Power:

    def __init__(
            self,
            power_driver: PowerDriver,
            led_driver: PowerLedDriver,
            preamp_driver: PreampDriver,
            amp_driver : AmpDriver
    ):
        self._power_driver = power_driver
        self._led_driver = led_driver
        self._preamp_driver = preamp_driver
        self._amp_driver = amp_driver
        self._power_state = False

    def get_power(self):
        return self._power_state

    def power_on(self, preamp_init=True):
        self._power_driver.additional_power_on()
        time.sleep(0.3)

        if preamp_init:
            self._preamp_driver.init()

        self._preamp_driver.setSoftMute(1)
        self._amp_driver.mute()
        time.sleep(0.3)

        self._power_driver.amp_power_on()
        self._preamp_driver.setSoftMute(0)
        self._amp_driver.unmute()

        time.sleep(0.3)

        self._led_driver.set_led_off()

        self._led_driver.set_blue_on()

        self._power_state = True

    def power_off(self):
        self._preamp_driver.setSoftMute(1)
        self._amp_driver.mute()

        time.sleep(0.2)
        self._power_driver.amp_power_off()
        time.sleep(0.3)

        self._power_driver.additional_power_off()

        self._led_driver.set_led_off()

        self._led_driver.set_red_on()

        self._power_state = False

    def key_observer(self, event):
        if event.action_type == Key.POWER_BTN:
            if event.value == Key.RELEASED:
                if self._power_state:
                    self.power_off()
                else:
                    self.power_on()



