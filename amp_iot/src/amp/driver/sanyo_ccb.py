
import RPi.GPIO as GPIO
from time import sleep


# Sanyo CCB bus protocol
# http://docplayer.net/34226119-Ccb-computer-control-bus.html
# https://github.com/avtehnik/rpi-sanyo-ccb/blob/master/fm_control.c
class SanyoCCB:

    _delay = 1
    _address = 0b00000000

    def __init__(self, clock_pin, data_pin, cip_pin):
        self._clock_pin = clock_pin
        self._data_pin = data_pin
        self._cip_pin = cip_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._clock_pin, GPIO.OUT)
        GPIO.setup(self._data_pin, GPIO.OUT)
        GPIO.setup(self._cip_pin, GPIO.OUT)

        GPIO.output(self._clock_pin, GPIO.LOW)
        GPIO.output(self._data_pin, GPIO.LOW)
        GPIO.output(self._cip_pin, GPIO.LOW)

    def _tick_clock(self):
        GPIO.output(self._clock_pin, GPIO.HIGH)
        sleep(self._delay)
        GPIO.output(self._clock_pin, GPIO.LOW)

    def _send_address(self, address):
        GPIO.output(self._cip_pin, GPIO.LOW)
        for i in range(0, 7):
            if address & (1 <<i) > 0:
                GPIO.output(self._data_pin, GPIO.HIGH)
            else:
                GPIO.output(self._data_pin, GPIO.LOW)
            sleep(self._delay)

            self._tick_clock()

    def _send_data(self, data, size):
        GPIO.output(self._cip_pin, GPIO.HIGH)

        for i in range(0, size):
            if data & (1 << i) > 0:
                sleep(self._delay)
                GPIO.output(self._data_pin, GPIO.HIGH)
            else:
                GPIO.output(self._data_pin, GPIO.LOW)

            self._tick_clock()

        sleep(self._delay)
        GPIO.output(self._cip_pin, GPIO.LOW)

    def send(self, data):
        self._send_address(self._address)
        size = len(data)
        self._send_data(data, size)


