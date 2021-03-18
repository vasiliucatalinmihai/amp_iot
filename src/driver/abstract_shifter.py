import RPi.GPIO as GPIO
from time import sleep

from src.driver import GpioPins


# shift register 74HC595
class AbstractShifter:
    
    # * main construct
    def __init__(self, latch_pin, data_pin, clock_pin, data_lenght=8, delay=0):
        self.delay = delay
        self._data_length = data_lenght

        # pin definition
        self._latch_pin = latch_pin
        self._data_pin = data_pin
        self._clock_pin = clock_pin
        self._setup_board()
        # data to send
        self._data = 0b00000000

    # set data to shifter
    # @param data int - data for shifter
    def set_data(self, data):
        self._data = data
        return self

    # get data from shifter
    def get_data(self):
        return self._data

    # clear data on shifter
    def clear_data(self, value=0):
        self._data = value  # 0b00000000
        return self

    # * set a bit (1)
    # @param pos bit position
    def set_bit(self, pos):
        self._data |= 1 << pos
        return self

    # * clear a bit (0)
    def clear_bit(self, pos):
        if self._data:
            self._data &= ~(1 << pos)
        return self

    # * send data to shifter
    def send_data(self):
        # print 'send'
        GPIO.output(self._latch_pin, GPIO.LOW)
        GPIO.output(self._data_pin, GPIO.LOW)
        GPIO.output(self._clock_pin, GPIO.LOW)
        for i in range(self._data_length):
            # print(self._data & (1 << i))
            sleep(self.delay)
            GPIO.output(self._clock_pin, GPIO.LOW)
            if self._data & (1 << i):
                GPIO.output(self._data_pin, GPIO.HIGH)
            else:
                GPIO.output(self._data_pin, GPIO.LOW)
            GPIO.output(self._clock_pin, GPIO.HIGH)
            GPIO.output(self._data_pin, GPIO.LOW)

        GPIO.output(self._clock_pin, GPIO.LOW)
        GPIO.output(self._latch_pin, GPIO.HIGH)
        return self
    
    # * chip setup    
    def _setup_board(self):
        GPIO.setmode(GpioPins.BOARD_MODE)
        GPIO.setup(self._data_pin, GPIO.OUT)
        GPIO.setup(self._clock_pin, GPIO.OUT)
        GPIO.setup(self._latch_pin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()
