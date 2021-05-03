
import RPi.GPIO as GPIO

from src.driver.gpio_pins import GpioPins


class Amplifier:

    MUTE_PIN = GpioPins.AMP_MUTE_PIN
    muted = False

    def __init__(self):
        GPIO.setmode(GpioPins.BOARD_MODE)
        GPIO.setup(self.MUTE_PIN, GPIO.OUT)

        self.unmute()

    def mute(self):
        GPIO.output(self.MUTE_PIN, GPIO.LOW)
        self.muted = True

        return self

    def unmute(self):
        GPIO.output(self.MUTE_PIN, GPIO.HIGH)
        self.muted = False

        return self

    def is_muted(self):
        return self.muted