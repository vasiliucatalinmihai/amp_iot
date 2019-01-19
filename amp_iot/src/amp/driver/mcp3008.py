
import RPi.GPIO as GPIO

from amp_iot.src.amp.driver.gpio_pins import GpioPins


class Mcp3008:

    SPI_CLOCK_PIN = GpioPins.MCP3008_SPI_CLOCK_PIN
    SPI_MISO_PIN = GpioPins.MCP3008_SPI_MISO_PIN
    SPI_MOSI_PIN = GpioPins.MCP3008_SPI_MOSI_PIN
    SPI_CS_PIN = GpioPins.MCP3008_SPI_CS_PIN

    def __init__(self):

        GPIO.setmode(GpioPins.BOARD_MODE)
        GPIO.setup(self.SPI_MOSI_PIN, GPIO.OUT)
        GPIO.setup(self.SPI_MISO_PIN, GPIO.IN)
        GPIO.setup(self.SPI_CLOCK_PIN, GPIO.OUT)
        GPIO.setup(self.SPI_CS_PIN, GPIO.OUT)

    # read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    def read_adc(self, channel):
        if (channel > 7) or (channel < 0):
            return -1
        GPIO.output(self.SPI_CS_PIN, GPIO.HIGH)

        GPIO.output(self.SPI_CLOCK_PIN, GPIO.LOW)  # start clock low
        GPIO.output(self.SPI_CS_PIN, GPIO.LOW)  # bring CS low

        # command_out = channel
        # command_out |= 0x18  # start bit + single-ended bit
        # command_out <<= 3  # we only need to send 5 bits here

        command_out = 0x3 << 6
        command_out |= channel << 3

        for i in range(5):
            # print(command_out & 0x80)
            if command_out & 0x80:
                print('HIGH')
                GPIO.output(self.SPI_MOSI_PIN, GPIO.HIGH)
            else:
                print('LOW')
                GPIO.output(self.SPI_MOSI_PIN, GPIO.LOW)
            command_out <<= 1
            GPIO.output(self.SPI_CLOCK_PIN, GPIO.HIGH)
            GPIO.output(self.SPI_CLOCK_PIN, GPIO.LOW)

        value = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
            GPIO.output(self.SPI_CLOCK_PIN, GPIO.HIGH)
            GPIO.output(self.SPI_CLOCK_PIN, GPIO.LOW)
            value <<= 1
            print(GPIO.input(self.SPI_MISO_PIN))
            if GPIO.input(self.SPI_MISO_PIN):
                value |= 0x1

        GPIO.output(self.SPI_CS_PIN, GPIO.HIGH)

        value >>= 1  # first bit is 'null' so drop it
        return value
