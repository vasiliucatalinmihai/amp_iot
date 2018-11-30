import RPi.GPIO as GPIO
import threading


# rotary encoder implementation
class Encoder:
    
    # encoder pins
    _encoder_a_pin = 11
    _encoder_b_pin = 13

    # tick counter
    rotary_counter = 0

    # encoder pin state
    _current_a = 1
    _current_b = 1

    # create lock for rotary switch
    LockRotary = threading.Lock()

    # * main construct
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._encoder_a_pin, GPIO.IN)
        GPIO.setup(self._encoder_b_pin, GPIO.IN)
        # setup callback thread for the A and B encoder 
        GPIO.add_event_detect(self._encoder_a_pin, GPIO.RISING, callback=self.rotary_interrupt)
        GPIO.add_event_detect(self._encoder_b_pin, GPIO.RISING, callback=self.rotary_interrupt)

    # Rotary encoder interrupt:
    def rotary_interrupt(self, encoder_pin):
        switch_a = GPIO.input(self._encoder_a_pin)
        switch_b = GPIO.input(self._encoder_b_pin)
        # now check if state of A or B has changed
        # if not that means that bouncing caused it
        if self._current_a == switch_a and self._current_b == switch_b:
            return

        self._current_a = switch_a
        self._current_b = switch_b

        # Both one active? Yes - end of sequence
        if switch_a and switch_b:
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
