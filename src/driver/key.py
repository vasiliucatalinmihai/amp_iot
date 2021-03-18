
import RPi.GPIO as GPIO
import threading
from time import sleep
import datetime
import queue

from src.driver import Encoder
from src.app import AmpApp
from src.driver import GpioPins


# key driver, include encoder
class Key(Encoder):

    BTN_0 = 'BTN_0'
    BTN_1 = 'BTN_1'
    BTN_2 = 'BTN_2'
    BTN_3 = 'BTN_3'
    ENCODER_BTN = 'ENCODER_BTN'

    ENCODER_VALUE = 'ENCODER_VALUE'

    LONG_RELEASE = 'LONG_RELEASE'
    RELEASED = 'RELEASE'
    PRESSED = 'PRESSED'

    _power_btn_pin = GpioPins.POWER_BTN_PIN
    _mute_btn_pin = GpioPins.MUTE_BTN_PIN

    _btn_0_pin = GpioPins.BTN_0_PIN
    _btn_1_pin = GpioPins.BTN_1_PIN
    _btn_2_pin = GpioPins.BTN_2_PIN
    _btn_3_pin = GpioPins.BTN_3_PIN
    _encoder_btn_pin = GpioPins.ENCODER_BTN_PIN

    KEY_CHANGE_EVENT = 'key_change_event'

    def __init__(self):
        self._pin_key_map = {
            self._btn_0_pin: self.BTN_0,
            self._btn_1_pin: self.BTN_1,
            self._btn_2_pin: self.BTN_2,
            self._btn_3_pin: self.BTN_3,
            self._encoder_btn_pin: self.ENCODER_BTN,
        }

        self._pin_status_action_map = {
            2: self.LONG_RELEASE,
            1: self.RELEASED,
            0: self.PRESSED
        }

        self._key_status = {
            self.BTN_0:      '',
            self.BTN_1:      '',
            self.BTN_2:      '',
            self.BTN_3:      '',
            self.ENCODER_BTN:   '',
        }
        self._key_changed = ''

        super().__init__()
        GPIO.setmode(GpioPins.BOARD_MODE)

        GPIO.setup(self._btn_0_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._btn_1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._btn_2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._btn_3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._encoder_btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(self._btn_0_pin, GPIO.BOTH, callback=self._process_key_press, bouncetime=50)
        GPIO.add_event_detect(self._btn_1_pin, GPIO.BOTH, callback=self._process_key_press, bouncetime=50)
        GPIO.add_event_detect(self._btn_2_pin, GPIO.BOTH, callback=self._process_key_press, bouncetime=50)
        GPIO.add_event_detect(self._btn_3_pin, GPIO.BOTH, callback=self._process_key_press, bouncetime=50)
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
