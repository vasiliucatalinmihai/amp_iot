
from amp_iot.src.lib.audio_map import AudioMap
from amp_iot.src.amp.driver.preamp import Preamp
from amp_iot.src.amp.driver.led_shifter import LedShifter as LedDriver


class Audio:

    def __init__(
            self,
            preamp_driver: Preamp,
            audio_map: AudioMap,
            led_driver: LedDriver
    ):
        self._preamp_driver = preamp_driver
        self._audio_map = audio_map
        self._led_driver = led_driver

    def process_external_call(self, method_name, args):

        try:
            function_map = self._audio_map.getFunc(method_name)
        except Exception as ex:
            return str(ex)

        func = getattr(self._preamp_driver, function_map['name'])
        params = dict()
        for i in args:
            params[function_map['params'][int(i)]] = args[i]

        try:
            return_data = func(**params)
        except Exception as ex:
            return_data = str(ex)

        if type(return_data) == type(self._preamp_driver):
            return_data = True

        return return_data

    def mute(self):
        self._preamp_driver.setSoftMuteEnable(1)
        self._led_driver.set_mute_led_blue()

    def unmute(self):
        self._preamp_driver.setSoftMuteEnable(0)
        self._led_driver.set_mute_led_off()


    def method(self, event):
        print(event.param1)