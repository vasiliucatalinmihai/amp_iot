
import RPi.GPIO as GPIO

from src.driver import GpioPins


class Amplifier:

    MUTE_PIN = GpioPins.AMP_MUTE_PIN

    def __init__(self):
        GPIO.setmode(GpioPins.BOARD_MODE)
        GPIO.setup(self.MUTE_PIN, GPIO.OUT)

        GPIO.output(self.MUTE_PIN, GPIO.HIGH)

    def mute(self):
        GPIO.output(self.MUTE_PIN, GPIO.LOW)

        return self

    def unmute(self):
        GPIO.output(self.MUTE_PIN, GPIO.HIGH)

        return self
