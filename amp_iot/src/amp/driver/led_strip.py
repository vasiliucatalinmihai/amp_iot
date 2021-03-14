
import time
import board
import neopixel


class LedStrip:

    ENCODER_STRIP = 0
    LOW_STRIP = 1

    # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
    # NeoPixels must be connected to D10, D12, D18 or D21 to work.
    pixel_pin = board.D18

    # The number of NeoPixels
    num_pixels = 32

    # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
    # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
    color_order = neopixel.GRB

    _encoder_pixels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    _pixel_data = list()
    _last_pixel_data = list()

    def __init__(self):
        self._pixels = neopixel.NeoPixel(
            self.pixel_pin,
            self.num_pixels,
            brightness=0.2,
            auto_write=False,
            pixel_order=self.color_order
        )

        for pixel in range(0, self.num_pixels):
            self._pixel_data.append((0, 0, 0))

        self.flush(True)

    def set_brightness(self, brightness):
        self._pixels.brightness = brightness

        return self

    def set_encoder_pixel(self, pixel, r, g, b):
        self._pixel_data[self._encoder_pixels[pixel]] = (r, g, b)

        return self

    def flush(self, force=False):
        if force is False and (self._pixel_data == self._last_pixel_data):
            return self

        for pixel in range(0, self.num_pixels):
            self._pixels[pixel] = self._pixel_data[pixel]

        self._pixels.show()
        self._last_pixel_data = self._pixel_data.copy()

        return self

    def set_encoder(self, data, flush=False):
        for pixel in range(0, 16):
            self._pixel_data[self._encoder_pixels[pixel]] = data[pixel]

        if flush:
            self.flush()

        return self