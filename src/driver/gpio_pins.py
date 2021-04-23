
import RPi.GPIO

# /boot/config.txt
# dtoverlay=i2c-gpio,bus=4,i2c_gpio_delay_us=1,i2c_gpio_sda=23,i2c_gpio_scl=24
# This line will create an aditional i2c bus (bus 4) on GPIO 23 as SDA and GPIO 24 as SCL (GPIO 23 and 24 is defaults)
#
# Also add the following line to create i2c bus 3
# dtoverlay=i2c-gpio,bus=3,i2c_gpio_delay_us=1,i2c_gpio_sda=17,i2c_gpio_scl=27


class GpioPins:

    BOARD_MODE = RPi.GPIO.BCM

    I2C_BUS = 4

    ENCODER_A_PIN = 13
    ENCODER_B_PIN = 6

    BTN_0_PIN = 1
    BTN_1_PIN = 1
    BTN_2_PIN = 1
    BTN_3_PIN = 1
    ENCODER_BTN_PIN = 22

    MCP3008_SPI_CLOCK_PIN = 11
    MCP3008_SPI_MISO_PIN = 9
    MCP3008_SPI_MOSI_PIN = 10
    MCP3008_SPI_CS_PIN = 8      # SPI 0 cs 0

    RELAY_AMP_POWER_PIN = 20
    RELAY_ADDITIONAL_POWER_PIN = 21
    AMP_MUTE_PIN = 16

    BLUE_LED_PIN = 25
    RED_LED_PIN = 24

    SPECTRUM_CLOCK_BAND_PIN = 5

    CCB_DATA_OUT_PIN = 13
    CCB_DATA_IN_PIN = 4  # !!!! not used
    CCB_CLOCK_PIN = 19
    CCB_CHIP_ENABLE_PIN = 26
