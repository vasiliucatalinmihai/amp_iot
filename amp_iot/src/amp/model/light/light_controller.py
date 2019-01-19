
import threading
import time

from amp_iot.src.lib.storage import Storage
from amp_iot.src.amp.driver.led_strip import LedStrip
from amp_iot.src.amp.model.light.effect import LightEffect
from amp_iot.src.amp.driver.spectrum import Spectrum


class LightController(LightEffect):

    Lock = threading.Lock()

    def __init__(
            self,
            storage_adapter: Storage,
            led_strip_driver: LedStrip,
            preamp_spectrum: Spectrum
    ):
        super().__init__(storage_adapter, led_strip_driver, preamp_spectrum)

        self._storage_adapter = storage_adapter
        self._led_strip_driver = led_strip_driver
        self._preamp_spectrum = preamp_spectrum

        self._effects = self._storage_adapter.get_config('light_effect')
        self._effects_list_inverted = {self._effects[k]: k for k in self._effects}

        self._encoder_mode_default = self._storage_adapter.get_config('default_lights_encoder')
        self._low_mode_default = self._storage_adapter.get_config('default_lights_low')

        self._encoder_mode = self._encoder_mode_default
        self._low_mode = self._low_mode_default

        self._light_encoder_thread = threading.Thread(target=self._run_encoder, args=())
        self._light_low_thread = threading.Thread(target=self._run_low, args=())
        self._light_flush_thread = threading.Thread(target=self._run_flush, args=())

        self._is_light_encoder_thread_running = False
        self._is_light_low_thread_running = False
        self._is_light_flush_thread_running = False

        self._last_encoder_update = time.time()
        self._last_low_update = time.time()
        self._volumes_wait_after_last_update = 3

        self.start()

    def change_encoder_mode(self, mode):
        if mode not in self._effects.keys():
            self._encoder_mode = self._encoder_mode_default
        else:
            self._last_encoder_update = time.time()
            self._encoder_mode = self._effects[mode]

        return self

    def change_low_mode(self, mode):
        if mode not in self._effects.keys():
            self._low_mode = self._low_mode_default
        else:
            self._last_low_update = time.time()
            self._low_mode = self._effects[mode]

        return self

    # get effect code by name
    def get_encoder_effect(self, name):

        if name in self._effects:
            return self._effects[name]

        return self._encoder_mode_default

        # get effect code by name

    def get_low_effect(self, name):

        if name in self._effects:
            return self._effects[name]

        return self._low_mode_default

    def _run_encoder(self):
        while self._is_light_encoder_thread_running:
            time.sleep(0.1)

            if self._encoder_mode == self.get_encoder_effect('main_volume') \
                    or self._encoder_mode == self.get_encoder_effect('treble') \
                    or self._encoder_mode == self.get_encoder_effect('middle') \
                    or self._encoder_mode == self.get_encoder_effect('bass'):

                if self._last_encoder_update + self._volumes_wait_after_last_update < int(time.time()):
                    self._encoder_mode = self._encoder_mode_default
            else:
                if self._encoder_mode in self._effects_list_inverted.keys():
                    try:
                        func = getattr(self, self._effects_list_inverted[self._encoder_mode])
                        func(LedStrip.ENCODER_STRIP, self._encoder_mode)
                    except Exception as ex:
                        print(str(ex))
                        pass
                else:
                    self._encoder_mode = self._encoder_mode_default

    def _run_low(self):
        while self._is_light_low_thread_running:
            time.sleep(0.1)

            if self._low_mode == self.get_low_effect('main_volume'):
                if self._last_low_update + self._volumes_wait_after_last_update < int(time.time()):
                    self._low_mode = self._low_mode_default
            elif self._low_mode == self.get_low_effect('treble') \
                    or self._low_mode == self.get_low_effect('middle') \
                    or self._low_mode == self.get_low_effect('bass'):
                # remain if mode is treble,middle or bass
                pass
            else:
                if self._low_mode in self._effects_list_inverted.keys():
                    try:
                        func = getattr(self, self._effects_list_inverted[self._low_mode])
                        func(LedStrip.LOW_STRIP, self._low_mode)
                    except Exception as ex:
                        print(str(ex))
                        pass
                else:
                    self._low_mode = self._low_mode_default

    def _run_flush(self):
        while self._is_light_flush_thread_running:
            time.sleep(0.1)
            self.Lock.acquire()
            self._led_strip_driver.flush()
            self.Lock.release()

    # @todo split in start for every thread
    def start(self):
        self._is_light_encoder_thread_running = True
        self._light_encoder_thread.daemon = True
        self._light_encoder_thread.start()

        self._is_light_low_thread_running = True
        self._light_low_thread.daemon = True
        self._light_low_thread.start()

        self._is_light_flush_thread_running = True
        self._light_flush_thread.daemon = True
        self._light_flush_thread.start()

    def stop(self):
        self._is_light_encoder_thread_running = False
        self._is_light_low_thread_running = False
        self._is_light_flush_thread_running = False

        self._encoder_mode = 0
        self._low_mode = 0

        data = self._blank_data.copy()
        self._led_strip_driver.set_encoder(data, True)
        self._led_strip_driver.set_low(data, True)

    def change_volume(self, value):
        self.change_low_mode('main_volume')
        self.change_encoder_mode('main_volume')
        self.bar(LedStrip.LOW_STRIP, (0, 0, 200), value, 100, 0)
        self.bar_empty(LedStrip.ENCODER_STRIP, (0, 0, 200), value, 100, 0)

    def change_bass(self, value):
        self.change_low_mode('bass')
        self.change_encoder_mode('bass')
        self.bar(LedStrip.LOW_STRIP, (200, 0, 0), value, 15, -15)
        self.bar_empty(LedStrip.ENCODER_STRIP, (200, 0, 0), value, 15, -15)

    def change_treble(self, value):
        self.change_low_mode('treble')
        self.change_encoder_mode('treble')
        self.bar(LedStrip.LOW_STRIP, (0, 200, 0), value, 15, -15)
        self.bar_empty(LedStrip.ENCODER_STRIP, (0, 200, 0), value, 15, -15)

    def change_middle(self, value):
        self.change_low_mode('middle')
        self.change_encoder_mode('middle')
        self.bar(LedStrip.LOW_STRIP, (200, 200, 0), value, 15, -15)
        self.bar_empty(LedStrip.ENCODER_STRIP, (200, 200, 0), value, 15, -15)
