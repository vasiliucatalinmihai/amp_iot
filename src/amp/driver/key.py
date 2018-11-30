
import RPi.GPIO as GPIO
import threading
from time import sleep
from amp_iot.src.amp.driver.encoder import Encoder


# key driver, include encoder
class Key(Encoder):

    POWER_BTN = 'POWER_BTN'
    MUTE_BTN = 'MUTE_BTN'
    ENCODER_BTN = 'ENCODER_BTN'
    ENCODER_VALUE = 'ENCODER_VALUE'

    _power_btn_pin = 1
    _mute_btn_pin = 2
    _encoder_btn_pin = 3

    _pin_status_action_map = {
        0: 'RELEASED',
        1: 'PRESSED'
    }

    def __init__(self):
        self._pin_key_map = {
            self._power_btn_pin: self.POWER_BTN,
            self._mute_btn_pin: self.MUTE_BTN,
            self._encoder_btn_pin: self.ENCODER_BTN,
        }

        self._key_status = {
            self.POWER_BTN: '',
            self.MUTE_BTN: '',
            self.ENCODER_BTN: '',
        }
        self._key_changed = ''

        super(Key, self).__init__()
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self._power_btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._mute_btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._encoder_btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(self._power_btn_pin, GPIO.BOTH, callback=self._process_key_press, bouncetime=500)
        GPIO.add_event_detect(self._mute_btn_pin, GPIO.BOTH, callback=self._process_key_press, bouncetime=500)
        GPIO.add_event_detect(self._encoder_btn_pin, GPIO.BOTH, callback=self._process_key_press, bouncetime=500)

        self._readThread = threading.Thread(target=self.read, args=())
        self._is_alive = 0

    # key interrupt
    def _process_key_press(self, pin):
        pin_status = int(GPIO.input(pin))

        self._key_status[self._pin_key_map[pin]] = self._pin_status_action_map[pin_status]
        self._key_changed = self._pin_key_map[pin]

    # read key, encoder changes thread
    def read(self):
        while self._is_alive:
            sleep(0.2)
            self.LockRotary.acquire()
            new_counter = self.rotary_counter
            self.rotary_counter = 0
            self.LockRotary.release()

            if new_counter != 0:
                self._dispatch(self.ENCODER_VALUE, new_counter * abs(new_counter))

            if self._key_changed != '':
                self._dispatch(self._key_changed, self._key_status[self._key_changed])
                self._key_changed = ''

    # listen thread, wait for key event and send it to listeners(app client +)
    def _dispatch(self, action_type, value):
        print(action_type)
        print(value)

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
