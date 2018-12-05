
from amp_iot.src.amp.driver.power import Power as PowerDriver
from amp_iot.src.amp.driver.led_shifter import LedShifter as LedDriver


class Power:

    def __init__(
            self,
            power_driver: PowerDriver,
            led_driver: LedDriver
    ):
        self._power_driver = power_driver
        self._led_driver = led_driver
        self._power_state = False

    def get_power(self):
        return self._power_state

    def power_on(self):
        self._power_driver.additional_power_on()
        self._power_driver.amp_power_on()

        self._led_driver.set_power_led_blue()

    def power_off(self):
        self._power_driver.additional_power_off()
        self._power_driver.additional_power_off()

        self._led_driver.set_power_led_amber()



