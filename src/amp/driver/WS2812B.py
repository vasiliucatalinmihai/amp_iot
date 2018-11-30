
from neopixel import *


# neopixel, WS2812B led array driver
class WS2812B:

    # LED strip configuration:
    LED_COUNT = 32  # Number of LED pixels.
    LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (800khz)
    LED_DMA = 10  # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

    _encoder_pixels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    _low_pixels = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

    def __init__(self):
        self._strip = None
        self.init_strip()

    def init_strip(self):
        # Create NeoPixel object with appropriate configuration.
        self._strip = Adafruit_NeoPixel(
            self.LED_COUNT,
            self.LED_PIN,
            self.LED_FREQ_HZ,
            self.LED_DMA,
            self.LED_INVERT,
            self.LED_BRIGHTNESS,
            self.LED_CHANNEL
        )

        self._strip.begin()

    def set_brightness(self, brightness):
        return self._strip.setBrightness(brightness)

    def set_encoder_pixel(self, pixel, r, g, b):
        return self._strip.setPixelColorRGB(self._encoder_pixels[pixel], r, g, b)

    def set_low_pixel(self, pixel, r, g, b):
        return self._strip.setPixelColorRGB(self._low_pixels[pixel], r, g, b)

    def flush_encoder(self):
        return self._strip.show()

    def flush_low(self):
        return self._strip.show()

    def set_encoder(self, data):
        for pixel in range(0, len(data)):
            self.set_encoder_pixel(self._encoder_pixels[pixel], data[pixel][0], data[pixel][1], data[pixel][2])

        self.flush_encoder()

    def set_low(self, data):
        for pixel in range(0, len(data)):
            self.set_encoder_pixel(self._low_pixels[pixel], data[pixel][0], data[pixel][1], data[pixel][2])

        self.flush_low()

