
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

    BTN_0_PIN = 16
    BTN_1_PIN = 20
    BTN_2_PIN = 21
    ENCODER_BTN_PIN = 5

    AMP_MUTE_PIN = 12

    SPECTRUM_SAIN_PIN = 25