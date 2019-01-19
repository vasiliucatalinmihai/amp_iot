
import RPi.GPIO as GPIO

from amp_iot.src.amp.driver.gpio_pins import GpioPins


class PowerLed:

    BLUE_LED_PIN = GpioPins.BLUE_LED_PIN
    RED_LED_PIN = GpioPins.RED_LED_PIN

    def __init__(self):
        GPIO.setmode(GpioPins.BOARD_MODE)
        GPIO.setup(self.BLUE_LED_PIN, GPIO.OUT)
        GPIO.setup(self.RED_LED_PIN, GPIO.OUT)

        GPIO.output(self.BLUE_LED_PIN, GPIO.LOW)
        GPIO.output(self.RED_LED_PIN, GPIO.LOW)

    def set_blue_on(self):
        GPIO.output(self.BLUE_LED_PIN, GPIO.HIGH)

        return self

    def set_red_on(self):
        GPIO.output(self.RED_LED_PIN, GPIO.HIGH)

        return self

    def set_led_off(self):
        GPIO.output(self.BLUE_LED_PIN, GPIO.LOW)
        GPIO.output(self.RED_LED_PIN, GPIO.LOW)

        return self
