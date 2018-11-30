
from amp_iot.src.lib.framework.abstract_controller import AbstractController
from amp_iot.src.amp.driver.power import Power
from amp_iot.src.amp.driver.led_shifter import LedShifter


class PowerController(AbstractController):

    def __init__(
            self,
            power_driver: Power,
            led_driver: LedShifter
    ):
        self._power_driver = power_driver
        self._led_driver = led_driver

    def power_on_action(self):
        self._power_driver.additional_power_on()
        self._power_driver.amp_power_on()

        self._led_driver.set_power_led_blue()

    def power_off_action(self):
        self._power_driver.additional_power_off()
        self._power_driver.additional_power_off()

        self._led_driver.set_power_led_amber()
