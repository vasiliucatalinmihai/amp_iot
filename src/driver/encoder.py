import threading

import RPi.GPIO as GPIO

from src.driver.gpio_pins import GpioPins

# rotary encoder implementation
class Encoder:
    
    # encoder pins
    _encoder_a_pin = GpioPins.ENCODER_A_PIN
    _encoder_b_pin = GpioPins.ENCODER_B_PIN

    # tick counter
    rotary_counter = 0

    # encoder pin state
    _last_a = 1
    _last_b = 1

    # create lock for rotary switch
    LockRotary = threading.Lock()

    # * main construct
    def __init__(self):
        GPIO.setmode(GpioPins.BOARD_MODE)
        GPIO.setup(self._encoder_a_pin, GPIO.IN)
        GPIO.setup(self._encoder_b_pin, GPIO.IN)
        # setup callback thread for the A and B encoder 
        GPIO.add_event_detect(self._encoder_a_pin, GPIO.RISING, callback=self.rotary_interrupt)
        GPIO.add_event_detect(self._encoder_b_pin, GPIO.RISING, callback=self.rotary_interrupt)

    # Rotary encoder interrupt:
    def rotary_interrupt(self, encoder_pin):
        current_a = GPIO.input(self._encoder_a_pin)
        current_b = GPIO.input(self._encoder_b_pin)
        # now check if state of A or B has changed
        # if not that means that bouncing caused it
        if self._last_a == current_a and self._last_b == current_b:
            return

        self._last_a = current_a
        self._last_b = current_b

        # Both one active? Yes - end of sequence
        if current_a and current_b:
            self.LockRotary.acquire()
            if encoder_pin == self._encoder_a_pin:
                self.rotary_counter += 1
            else:
                self.rotary_counter -= 1
            self.LockRotary.release()
            return

    # destruct
    def __del__(self):
        GPIO.cleanup()
