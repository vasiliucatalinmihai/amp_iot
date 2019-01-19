
import RPi.GPIO


class GpioPins:

    BOARD_MODE = RPi.GPIO.BCM

    I2C_BUS = 3
    # SDA GPIO23 (16), SCL GPIO24(18)
    # /boot/config.txt dtoverlay=i2c-gpio,i2c_gpio_sda=23,i2c_gpio_scl=24, bus=3

    ENCODER_A_PIN = 17
    ENCODER_B_PIN = 27

    POWER_BTN_PIN = 7
    MUTE_BTN_PIN = 12
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
