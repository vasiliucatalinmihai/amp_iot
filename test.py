from amp_iot.src.driver import PowerLed

l=PowerLed()


from amp_iot.src.driver import Key

k=Key()
k.start()


#
from amp_iot.src.main import AmplifierMain

amp = AmplifierMain()

amp.run()

from amp_iot.src.driver import PowerLed
p = PowerLed()
p.set_red_on()

from amp_iot.src.driver import Power
p=Power()


import sounddevice as sd

duration = 10  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = indata
    print (int(volume_norm))

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)