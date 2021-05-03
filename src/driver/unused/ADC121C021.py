# ADC121C021
# This code is designed to work with the ADC121C021_I2CADC I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Analog-Digital-Converters?sku=ADC121C021_I2CADC#tabs-0-product_tabset-2
# http://www.ti.com/lit/ds/symlink/adc121c021.pdf

import time

import smbus


class ADC121C021:

    def __init__(self):
        # Get I2C bus
        self._bus = smbus.SMBus(1)
        # ADC121C021 address, 0x50(80)
        self._bus_address = 0x50
        # Select configuration register, 0x02(02)
        # 		0x20(32)	Automatic conversion mode enabled
        self._bus.write_byte_data(self._bus_address, 0x02, 0x20)
        time.sleep(0.5)

    def read(self):
        # ADC121C021 address, 0x50(80)
        # Read data back from 0x00(00), 2 bytes
        # raw_adc MSB, raw_adc LSB
        data = self._bus.read_i2c_block_data(self._bus_address, 0x00, 2)

        # Convert the data to 12-bits
        raw_adc = (data[0] & 0x0F) * 256 + data[1]
        return raw_adc

    def print(self):
        raw_adc = self.read()
        # Output data to screen
        print("Digital Value of Analog Input : ") + str(raw_adc)
