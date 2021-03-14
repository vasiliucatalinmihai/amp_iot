
import time
import threading
import random

from amp_iot.src.lib.storage import Storage
from amp_iot.src.driver import LedStrip
from amp_iot.src.driver import Spectrum


class LightEffect:

    Lock = threading.Lock()

    def __init__(
        self,
        storage_adapter: Storage,
        led_strip_driver: LedStrip,
        preamp_spectrum: Spectrum
    ):
        self._storage_adapter = storage_adapter
        self._led_strip_driver = led_strip_driver
        self._preamp_spectrum = preamp_spectrum

        self._encoder_mode_default = self._storage_adapter.get_config('default_lights_encoder')
        self._low_mode_default = self._storage_adapter.get_config('default_lights_low')

        self._encoder_mode = self._encoder_mode_default
        self._low_mode = self._low_mode_default

        self._blank_data = []
        for i in range(0, 16):
            self._blank_data.append((0, 0, 0))

    def _is_mode_changed(self, mode, strip):
        if strip == LedStrip.ENCODER_STRIP:
            return not mode == self._encoder_mode
        elif strip == LedStrip.LOW_STRIP:
            return not mode == self._low_mode

        return False

    def _add_data_to_strip(self, data, strip, flush=False):
        self.Lock.acquire()

        if strip == LedStrip.ENCODER_STRIP:
            self._led_strip_driver.set_encoder(data, flush)
        elif strip == LedStrip.LOW_STRIP:
            self._led_strip_driver.set_low(data, flush)

        self.Lock.release()

    def _set_pixel(self, pixel, color, strip):
        self.Lock.acquire()

        if strip == LedStrip.ENCODER_STRIP:
            self._led_strip_driver.set_encoder_pixel(pixel, color[0], color[1], color[2])
        elif strip == LedStrip.LOW_STRIP:
            self._led_strip_driver.set_low_pixel(pixel, color[0], color[1], color[2])

        self.Lock.release()

    def bar(self, strip, color, value, max_value=100, min_value=0):
        value = self.map_bar(value, max_value, min_value)
        data = self._blank_data.copy()

        for i in range(0, 16):
            if i <= value:
                data[i] = color
            else:
                data[i] = (0, 0, 0)

        self._add_data_to_strip(data, strip, False)

    def bar_empty(self, strip, color, value, max_value=100, min_value=0):
        value = self.map_bar(value, max_value, min_value)
        data = self._blank_data.copy()

        for i in range(0, 16):
            if i == int(value):
                data[i] = color
            else:
                data[i] = (0, 0, 0)

        self._add_data_to_strip(data, strip, False)

    # map value on bar height
    @staticmethod
    def map_bar(value, max_value, min_value):
        out_max = 16
        out_min = 1
        return (value - min_value) * (out_max - out_min) / (max_value - min_value) + out_min

    def vumeter(self, strip, mode):
        while not self._is_mode_changed(mode, strip):
            data = self._blank_data.copy()
            for i in range(0, 16):
                data[i] = (0, 0, 100)
                time.sleep(0.21)
                if self._is_mode_changed(mode, strip):
                    return
                self._add_data_to_strip(data, strip)

    def no_effect(self, strip, mode):
        data = self._blank_data.copy()
        self._add_data_to_strip(data, strip)
        while not self._is_mode_changed(mode, strip):
            time.sleep(0.5)
            if self._is_mode_changed(mode, strip):
                return

    def random(self, strip, mode):
        while not self._is_mode_changed(mode, strip):
            data = self._blank_data.copy()
            for i in range(0, random.randint(0, 15)):
                data[random.randint(0, 15)] = (random.randint(0, 205), random.randint(0, 205), random.randint(0, 205))
                time.sleep(random.randint(0, 10) / 1000)
                if self._is_mode_changed(mode, strip):
                    return
                self._add_data_to_strip(data, strip)

    def slide(self, strip, mode):
        on_pixels = [
            (1, 0, 2), (5, 0, 10), (10, 0, 30), (20, 0, 50), (40, 0, 90), (60, 0, 150), (80, 0, 200),
            (80, 0, 200), (60, 0, 150), (40, 0, 90), (20, 0, 50), (10, 0, 30), (5, 0, 10), (1, 0, 2),
        ]

        while not self._is_mode_changed(mode, strip):

            for i in range(0, 15 + len(on_pixels)):
                data = self._blank_data.copy()
                for j in range(0, len(on_pixels)):
                    if 0 <= (i - j) <= 15:
                        data[i - j] = on_pixels[j]
                time.sleep(0.2)
                self._add_data_to_strip(data, strip)
                if self._is_mode_changed(mode, strip):
                    return

            for k in range(0, 15 + len(on_pixels)):
                i = 15 - k
                data = self._blank_data.copy()
                for j in range(0, len(on_pixels)):
                    if 0 <= (i + j) <= 15:
                        data[i + j] = on_pixels[j]
                time.sleep(0.2)
                self._add_data_to_strip(data, strip)
                if self._is_mode_changed(mode, strip):
                    return

    def pulse_purple(self, strip, mode):
        self.pulse(strip, mode, (100, 10, 200))

    def pulse_red(self, strip, mode):
        self.pulse(strip, mode, (200, 0, 0))

    def pulse_green(self, strip, mode):
        self.pulse(strip, mode, (0, 200, 0))

    def pulse_blue(self, strip, mode):
        self.pulse(strip, mode, (0, 0, 200))

    def pulse(self, strip, mode, color):
        data = self._blank_data.copy()
        steps = 100

        while not self._is_mode_changed(mode, strip):

            for step in range(0, steps):
                for i in range(0, 16):
                    data[i] = self.dim_color(color, step, steps)

                time.sleep(0.01)
                self._add_data_to_strip(data, strip)
                if self._is_mode_changed(mode, strip):
                    return

            time.sleep(1)

            for step2 in range(0, steps):
                step = steps - step2
                for i in range(0, 16):
                    data[i] = self.dim_color(color, step, steps)

                time.sleep(0.01)
                self._add_data_to_strip(data, strip)
                if self._is_mode_changed(mode, strip):
                    return

            time.sleep(0.4)

    @staticmethod
    def dim_color(color, step, steps):
        red = (color[0] / steps) * step
        green = (color[1] / steps) * step
        blue = (color[2] / steps) * step

        return int(red), int(green), int(blue)

    def mopidy_set(self, strip, mode):
        data = self._blank_data.copy()
        self._add_data_to_strip(data, strip, True)

        self._set_pixel(0, (0, 200, 0), strip)
        self._set_pixel(15, (0, 200, 0), strip)
        time.sleep(0.2)

        self._set_pixel(0, (0, 200, 0), strip)
        self._set_pixel(1, (0, 200, 0), strip)
        self._set_pixel(14, (0, 200, 0), strip)
        self._set_pixel(15, (0, 200, 0), strip)
        time.sleep(0.3)

        self._set_pixel(0, (0, 200, 0), strip)
        self._set_pixel(1, (0, 0, 0), strip)
        self._set_pixel(14, (0, 0, 0), strip)
        self._set_pixel(15, (0, 200, 0), strip)
        time.sleep(0.2)

        self._set_pixel(0, (0, 0, 0), strip)
        self._set_pixel(15, (0, 0, 0), strip)
        time.sleep(0.2)

        self._low_mode = self._low_mode_default
