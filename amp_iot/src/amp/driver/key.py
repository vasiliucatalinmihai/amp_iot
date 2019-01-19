
import RPi.GPIO as GPIO
import threading
from time import sleep
import datetime
import queue

from amp_iot.src.amp.driver.encoder import Encoder
from amp_iot.src.amp.app import AmpApp
from amp_iot.src.amp.driver.gpio_pins import GpioPins


# key driver, include encoder
class Key(Encoder):

    POWER_BTN = 'POWER_BTN'
    MUTE_BTN = 'MUTE_BTN'
    ENCODER_BTN = 'ENCODER_BTN'
    ENCODER_VALUE = 'ENCODER_VALUE'

    LONG_RELEASE = 'LONG_RELEASE'
    RELEASED = 'RELEASE'
    PRESSED = 'PRESSED'

    _power_btn_pin = GpioPins.POWER_BTN_PIN
    _mute_btn_pin = GpioPins.MUTE_BTN_PIN
    _encoder_btn_pin = GpioPins.ENCODER_BTN_PIN

    KEY_CHANGE_EVENT = 'key_change_event'

    def __init__(self):
        self._pin_key_map = {
            self._power_btn_pin: self.POWER_BTN,
            self._mute_btn_pin: self.MUTE_BTN,
            self._encoder_btn_pin: self.ENCODER_BTN,
        }

        self._pin_status_action_map = {
            2: self.LONG_RELEASE,
            1: self.RELEASED,
            0: self.PRESSED
        }

        self._key_status = {
            self.POWER_BTN:     '',
            self.MUTE_BTN:      '',
            self.ENCODER_BTN:   '',
        }
        self._key_changed = ''

        super().__init__()
        GPIO.setmode(GpioPins.BOARD_MODE)

        GPIO.setup(self._power_btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._mute_btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._encoder_btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(self._power_btn_pin, GPIO.BOTH, callback=self._process_key_press, bouncetime=50)
        GPIO.add_event_detect(self._mute_btn_pin, GPIO.BOTH, callback=self._process_key_press, bouncetime=50)
        GPIO.add_event_detect(self._encoder_btn_pin, GPIO.BOTH, callback=self._process_key_press, bouncetime=50)

        self._readThread = threading.Thread(target=self.read, args=())
        self._is_alive = 0

    # key interrupt
    def _process_key_press(self, pin):
        pin_status = int(GPIO.input(pin))

        self._key_status[self._pin_key_map[pin]] = self._pin_status_action_map[pin_status]
        self._key_changed = self._pin_key_map[pin]

    @staticmethod
    def millis():
        dt = datetime.now()
        ms = (dt.day * 24 * 60 * 60 + dt.second) * 1000 + dt.microsecond / 1000.0
        return ms

    # read key, encoder changes thread
    def read(self):
        while self._is_alive:
            # sleep(0.05)
            # self.LockRotary.acquire()
            new_counter = self.rotary_counter
            self.rotary_counter = 0
            # self.LockRotary.release()

            if new_counter != 0:
                self._dispatch(self.ENCODER_VALUE, new_counter * abs(new_counter))

            if self._key_changed != '':
                print(self._key_status[self._key_changed])
                self._dispatch(self._key_changed, self._key_status[self._key_changed])
                self._key_changed = ''

    # listen thread, wait for key event and send it to listeners(app client +)
    def _dispatch(self, action_type, value):
        AmpApp.dispatch(self.KEY_CHANGE_EVENT, {'action_type': action_type, 'value': value})

        return self

    # * threading loop start
    def start(self):
        self._is_alive = 1
        self._readThread.start()

    # stop read loop
    def stop(self):
        self._is_alive = 0

    # is read thread running
    def is_alive(self):
        return self._is_alive

        # destruct
    def __del__(self):
        self.stop()
        GPIO.cleanup()
