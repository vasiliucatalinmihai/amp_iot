
from time import sleep

import RPi.GPIO as GPIO

from src.driver import GpioPins


class CCB:

    CCB_DELAY = 0.0001
    _CCB_SEND = 1
    _CCB_RECEIVE = 0

    _data_out_pin = GpioPins.CCB_DATA_OUT_PIN
    _clock_pin = GpioPins.CCB_CLOCK_PIN
    _data_in_pin = GpioPins.CCB_DATA_IN_PIN
    _chip_enable_pin = GpioPins.CCB_CHIP_ENABLE_PIN

    def __init__(self):
        GPIO.setmode(GpioPins.BOARD_MODE)
        GPIO.setup(self._clock_pin, GPIO.OUT)
        GPIO.setup(self._data_out_pin, GPIO.OUT)
        GPIO.setup(self._chip_enable_pin, GPIO.OUT)

        GPIO.setup(self._data_in_pin, GPIO.IN)

        GPIO.output(self._data_in_pin, GPIO.HIGH)

        GPIO.output(self._data_out_pin, GPIO.LOW)
        GPIO.output(self._clock_pin, GPIO.LOW)  # Clock - rest - low

        # Paranoia: cycle CE to "flush" de bus
        GPIO.output(self._chip_enable_pin, GPIO.HIGH)
        sleep(self.CCB_DELAY)
        GPIO.output(self._chip_enable_pin, GPIO.LOW)
        sleep(self.CCB_DELAY)

    @staticmethod
    def _bit_read(value, pos):
        return (value >> pos) & 0x01

    @staticmethod
    def _bit_write(value, bit, bit_value):
        if bit_value:
            value |= 1 << bit
        else:
            value &= ~ 1 << bit

    def _write_byte(self, data):

        for i in range(0, 7):
            GPIO.output(self._data_out_pin, self._bit_read(data, i))
            GPIO.output(self._clock_pin, GPIO.HIGH)
            sleep(self.CCB_DELAY)
            GPIO.output(self._clock_pin, GPIO.LOW)
            sleep(self.CCB_DELAY)

    def read_byte(self):
        data = 0
        # Receive one byte from the CCB bus (MSB first)

        for i in range(7, 0):
            GPIO.output(self._clock_pin, GPIO.HIGH)
            sleep(self.CCB_DELAY)

            self._bit_write(data, i, GPIO.input(self._data_in_pin))
            GPIO.output(self._clock_pin, GPIO.LOW)
            sleep(self.CCB_DELAY)
        return data

    # The universal send/receive function
    def ccb(self, address, data, data_length, mode):
        # Send the address, with the nibbles swapped (required by the CCB protocol to support 4-bit addresses)
        self._write_byte((address >> 4) | (address << 4))

        # Enter the data transfer mode
        GPIO.output(self._clock_pin, GPIO.LOW)
        GPIO.output(self._chip_enable_pin, GPIO.HIGH)
        sleep(self.CCB_DELAY)

        if mode == self._CCB_SEND:
            # Send data
            # Note: as CCB devices usually reads registers data from MSB to LSB, the buffer is read from left to right
            for i in range(0, data_length):
                self._write_byte(data[i])
                GPIO.output(self._data_out_pin, GPIO.LOW)
        if mode == self._CCB_RECEIVE:
            # Receive data
            for i in range(0, data_length):
                data[i] = self.read_byte()

        GPIO.output(self._chip_enable_pin, GPIO.LOW)
        sleep(self.CCB_DELAY)

    # *********************************************************
    #                     data_in_state()
    #  Return the state of the DI pin
    #  Some CCB devices uses the DO pin for other functions
    #  when the data bus is idle.  This method makes reading
    #  it easier
    # *********************************************************
    def data_in_state(self):
        return GPIO.input(self._data_in_pin)

    # ********************************************************
    #                     write()
    #  Send dataLength (up to 127) bytes via CCB bus
    # Note: the contents of the input buffer is send
    # backwards (from the rightmost to the leftmost byte),
    # so the order of the data bytes must be the opposite
    # as the one shown on the device's datasheets
    # ********************************************************
    def write(self, address, data, data_length):
        self.ccb(address, data, data_length, self._CCB_SEND)

    # ******************************************************
    #                      read()
    #  receive dataLength (up to 127) bytes via CCB bus
    # ******************************************************
    def read(self, address, data, data_length):
        self.ccb(address, data, data_length, self._CCB_RECEIVE)
