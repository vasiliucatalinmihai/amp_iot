
import smbus
import time

class Ads1110:
    busPort = 4
    i2cAddress = 0x48

    def __init__(self):
        self.bus = smbus.SMBus(self.busPort)

    def read(self):
        read = self.bus.read_i2c_block_data(self.i2cAddress, 0x00, 3)
        value = read[0] * 256 + read[1]
        return value

    def read_voltage(self, value=None):
        if value is None:
            value = self.read()

        return value * 2.048 / 32768.0

    def __str__(self):
        value = self.read()
        voltage = self.read_voltage(value)

        return "Value ->> " + str(value) + "\n" + "Voltage ->> " + str(voltage)

# adc = Ads1110()
# while True:
#     print(adc)
#     time.sleep(0.5)