from amp_iot.src.amp.driver.power_led import PowerLed

l=PowerLed()


from amp_iot.src.amp.driver.key import Key

k=Key()
k.start()


#
from amp_iot.src.amp.main import AmplifierMain

amp = AmplifierMain()

amp.run()

from amp_iot.src.amp.driver.power_led import PowerLed
p = PowerLed()
p.set_red_on()

from amp_iot.src.amp.driver.power import Power
p=Power()


import sounddevice as sd

duration = 10  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = indata
    print (int(volume_norm))

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)