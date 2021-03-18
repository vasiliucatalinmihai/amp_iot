from src.driver import PowerLed

l=PowerLed()


from src.driver import Key

k=Key()
k.start()


#
from src.main import AmplifierMain

amp = AmplifierMain()

amp.run()

from src.driver import PowerLed
p = PowerLed()
p.set_red_on()

from src.driver import Power
p=Power()


import sounddevice as sd

duration = 10  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = indata
    print (int(volume_norm))

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)