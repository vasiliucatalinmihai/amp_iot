
import RPi.GPIO as GPIO
import threading
import time

from src.driver.ads1110 import Ads1110
from src.driver import GpioPins


class Spectrum:

    USE_THREAD = False
    DATA_LOCK = threading.Lock()

    CLOCK_BAND_PIN = GpioPins.SPECTRUM_CLOCK_BAND_PIN

    KEY_62_HZ = 0
    KEY_157_HZ = 1
    KEY_396_HZ = 2
    KEY_1_0_KHZ = 3
    KEY_2_51_KHZ = 4
    KEY_6_34_KHZ = 5
    KEY_15_KHZ = 6

    def __init__(self, adc_driver: Ads1110):
        self._adc_driver = adc_driver

        GPIO.setmode(GpioPins.BOARD_MODE)
        GPIO.setup(self.CLOCK_BAND_PIN, GPIO.OUT)
        GPIO.output(self.CLOCK_BAND_PIN, GPIO.LOW)

        self._data = dict()
        self._data[self.KEY_62_HZ] = 0
        self._data[self.KEY_157_HZ] = 0
        self._data[self.KEY_396_HZ] = 0
        self._data[self.KEY_1_0_KHZ] = 0
        self._data[self.KEY_2_51_KHZ] = 0
        self._data[self.KEY_6_34_KHZ] = 0
        self._data[self.KEY_15_KHZ] = 0

        if self.USE_THREAD:
            self._read_thread = threading.Thread(target=self._thread_read, args=())
            self._read_thread.start()

    def _read(self):

        for key in self._data.keys():
            GPIO.output(self.CLOCK_BAND_PIN, GPIO.LOW)
            GPIO.output(self.CLOCK_BAND_PIN, GPIO.HIGH)
            time.sleep(0.0001)
            self._data[key] = self._adc_driver.read()
        time.sleep(0.01)

    def _thread_read(self):
        while True:
            self.DATA_LOCK.acquire()
            self._read()
            self.DATA_LOCK.release()

    def get_amplitude(self, freq):
        if not self.USE_THREAD:
            self. _read()

        print(self._data)
        return self._data[freq]
