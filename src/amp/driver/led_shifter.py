
from amp_iot.src.amp.driver.abstract_shifter import AbstractShifter


class LedShifter(AbstractShifter):

    # pin positions
    _btn_led_power_blue_pos = 0
    _btn_led_power_amber_pos = 1
    _btn_led_mute_blue_pos = 2
    _btn_led_mute_amber_pos = 3
    _power_relay_1 = 4
    _power_relay_2 = 5

    # shifter control pins
    LATCH_PIN = 1
    DATA_PIN = 2
    CLOCK_PIN = 3
    DATA_LENGTH = 8
    DELAY = 0

    def __init__(self):
        super(LedShifter, self).__init__(self.LATCH_PIN, self.DATA_PIN, self.CLOCK_PIN, self.DATA_LENGTH, self.DELAY)

    def set_power_led_blue(self):
        self.set_bit(self._btn_led_power_blue_pos)
        self.clear_bit(self._btn_led_power_amber_pos)
        self.send_data()

    def set_power_led_amber(self):
        self.set_bit(self._btn_led_power_amber_pos)
        self.clear_bit(self._btn_led_power_blue_pos)
        self.send_data()

    def set_power_led_off(self):
        self.clear_bit(self._btn_led_power_amber_pos)
        self.clear_bit(self._btn_led_power_blue_pos)
        self.send_data()

    def set_mute_led_blue(self):
        self.set_bit(self._btn_led_mute_blue_pos)
        self.clear_bit(self._btn_led_power_amber_pos)
        self.send_data()

    def set_mute_led_amber(self):
        self.set_bit(self._btn_led_mute_amber_pos)
        self.clear_bit(self._btn_led_mute_blue_pos)
        self.send_data()

    def set_mute_led_off(self):
        self.clear_bit(self._btn_led_mute_amber_pos)
        self.clear_bit(self._btn_led_mute_blue_pos)
        self.send_data()

    def set_power_relay_on(self):
        self.set_bit(self._power_relay_1)
        self.set_data()

    def set_power_relay_off(self):
        self.clear_bit(self._power_relay_1)
        self.set_data()