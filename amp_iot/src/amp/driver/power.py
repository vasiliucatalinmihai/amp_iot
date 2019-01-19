
import RPi.GPIO as GPIO

from amp_iot.src.amp.driver.gpio_pins import GpioPins


class Power:

    RELAY_AMP_POWER_PIN = GpioPins.RELAY_AMP_POWER_PIN
    RELAY_ADDITIONAL_POWER_PIN = GpioPins.RELAY_ADDITIONAL_POWER_PIN

    def __init__(self):
        GPIO.setmode(GpioPins.BOARD_MODE)
        GPIO.setup(self.RELAY_AMP_POWER_PIN, GPIO.OUT)
        GPIO.setup(self.RELAY_ADDITIONAL_POWER_PIN, GPIO.OUT)

        GPIO.output(self.RELAY_AMP_POWER_PIN, GPIO.HIGH)
        GPIO.output(self.RELAY_ADDITIONAL_POWER_PIN, GPIO.HIGH)

    def power_on(self):
        self.amp_power_on()
        self.additional_power_on()

        return self

    def power_off(self):
        self.amp_power_off()
        self.additional_power_off()

        return self

    def amp_power_on(self):
        GPIO.output(self.RELAY_AMP_POWER_PIN, GPIO.HIGH)

        return self

    def amp_power_off(self):
        GPIO.output(self.RELAY_AMP_POWER_PIN, GPIO.LOW)

        return self

    def additional_power_on(self):
        GPIO.output(self.RELAY_ADDITIONAL_POWER_PIN, GPIO.HIGH)

        return self

    def additional_power_off(self):
        GPIO.output(self.RELAY_ADDITIONAL_POWER_PIN, GPIO.LOW)

        return self

    def __del__(self):
        GPIO.cleanup()
