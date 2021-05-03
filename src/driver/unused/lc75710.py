import RPi.GPIO as GPIO

from src.driver import GpioPins


class Lc75710Low:

    ADDRESS            = 0b11100110    # /**< Chip address (B11100110) */
    LC75710_DIGITS     = 10    # /**< Number of digits for a given implementation */
    LC75710_DRAM_SIZE  = 64    # /**< Size of the internal DCRAM */

    # / *Modes of operation * /
    NO_MDATA_NOR_ADATA     = 0x0     # /**< Command does not affect MDATA nor ADATA */
    ADATA_ONLY             = 0x1     # /**< Command does affect ADATA only */
    MDATA_ONLY             = 0x2     # /**< Command does affect MDATA only */
    MDATA_AND_ADATA        = 0x3     # /**< Command does affect both ADATA and MDATA */

    LC75710_CGRAM_SIZE = 8       # /**< The size of the CGRAM (characters) */
    DEASPLAY_POWER_OFF = 1
    DEASPLAY_POWER_ON = 0

    _data_out_pin = GpioPins.CCB_DATA_OUT_PIN
    _clock_pin = GpioPins.CCB_CLOCK_PIN
    _data_in_pin = GpioPins.CCB_DATA_IN_PIN
    _chip_enable_pin = GpioPins.CCB_CHIP_ENABLE_PIN

    def __init__(self):
        GPIO.setmode(GpioPins.BOARD_MODE)
        # Hardware pin initialization and chip reset state initialization

        GPIO.setup(self._clock_pin, GPIO.OUT)
        GPIO.setup(self._data_out_pin, GPIO.OUT)
        GPIO.setup(self._chip_enable_pin, GPIO.OUT)

        GPIO.setup(self._data_in_pin, GPIO.IN)

        # /* Initial output states */
        GPIO.output(self._clock_pin, GPIO.LOW)
        GPIO.output(self._data_out_pin, GPIO.LOW)
        GPIO.output(self._chip_enable_pin, GPIO.LOW)

        # After power up the display shall be initialized, otherwise registers contain garbage data

        # /* Reset Function, as described in the datasheet */
        self.lc75710_blink(self.MDATA_AND_ADATA, 0, 0xFFFF)

        for i in range(0, 64):
            # /* Initialize DCRAM with spaces */
            self.lc75710_dcram_write(i, 0x20)

        self.lc75710_set_ac_address(0, 0)
        self.lc75710_grid_register_load(10)
        self.lc75710_intensity(128)

        # /* Turn the display ON */
        # self.lc75710_on_off(MDATA_AND_ADATA, true, 0xFFFF)

    def lc75710_write_low(self, data, bits_count):

        j = 0

        for i in range(0, bits_count):
            if j >= 8:
                j = 0
                data += 1

            if (data >> j) & 0x1:
                GPIO.output(self._data_out_pin, GPIO.HIGH)
            else:
                GPIO.output(self._data_out_pin, GPIO.LOW)

            j += 1
            GPIO.output(self._clock_pin, GPIO.HIGH)
            GPIO.output(self._clock_pin, GPIO.LOW)

    def lc75710_select(self):
        GPIO.output(self._chip_enable_pin, GPIO.LOW)
        # /* Address goes out first... */
        buf = self.ADDRESS
        self.lc75710_write_low(buf, 8)

        # /* Then data follows after, CE goes high */
        GPIO.output(self._chip_enable_pin, GPIO.HIGH)

    def lc75710_deselect(self):

        GPIO.output(self._chip_enable_pin, GPIO.LOW)

        # /* wait long enough for the command to complete (at least 18us for most commands) */
        # _delay_us(25)

    # /**
    #  * @brief
    #  *   This function writes the serial data (low-level) to the chip.
    #  *   The datasheet specifies about 0.5us delay between the edges of inputs.
    #  *   In any case, it has been tested that delays are not needed between calls,
    #  *   and this due to the particularly "slow" access to pins that the Arduino library operates.
    #  *   This note is left for a future bare-metal implementation.
    #  *
    #  * @param data the 24-bit data to be sent over the serial line
    #  */

    def lc75710_write(self, data):
        self.lc75710_select()

        self.lc75710_write_low(data, 24)

        self.lc75710_deselect()

    # /**
    #  *   Send a Display blink command to the chip.
    #  *
    #  * @param operation the affected display memory, 0..3, see constants
    #  * @param period    the blink period, 0..7, 0.1 seconds to 1.0 seconds
    #  * @param digits    the affected digits, 0..15 bits, where every bit is a grid (i.e. a digit)
    #  */
    def lc75710_blink(self, operation, period, digits):
        # /* Instruction */
        temp = 0x5 << 21

        # /* Data that specifies the blinking operation */
        temp = temp | ((operation & 0x3) << 19)

        # /* Blink period setting */
        temp |= (period & 0x7) << 16

        # /*  Blinking digit specification */
        temp |= digits

        # /* Write to IC */
        self.lc75710_write(temp)

    # /**
    #  *   Send a Display on/off control command to the chip.
    #  *
    #  * @param operation the affected display memory, 0..3, see constants
    #  * @param mode      TRUE: selected grids on; FALSE: selected grids off
    #  * @param grids     the affected digits, 0..15 bits, where every bit is a grid (i.e. a digit)
    #  */
    def lc75710_on_off(self, operation, mode, grids):
        # /* Instruction */
        temp = 0x1 << 20

        # /* Specifies the data to be turned on or off */
        temp |= (operation & 0x3) << 17

        # /* Toggle */
        temp |= mode << 16

        # /* Grid selection */
        temp |= grids

        # /* Write to IC */
        self.lc75710_write(temp)

    # /**
    #  *   Send a Display shift control command to the chip.
    #  *
    #  * @param operation the affected display memory, 0..3, see constants
    #  * @param direction TRUE: Left Shift; FALSE: Right Shift
    #  */
    def lc75710_shift(self, operation, direction):
        # /* Instruction */
        temp = 0x2 << 20

        # /* Specifies the data to be shifted */
        temp |= (operation & 0x3) << 17

        # /* Direction */
        temp |= direction << 16

        # /* Write to IC */
        self.lc75710_write(temp)

    # /**
    #  *   Send a Grid register load command to the chip.
    #  *
    #  * @param grids The number of grids (digits), proper of the display
    #  */
    def lc75710_grid_register_load(self, grids):
        # /* Instruction */
        temp = 0x3 << 20

        # /* Specifies the amount of grids (i.e. digits) */
        temp |= (grids & 0xF) << 16

        # /* Write to IC */
        self.lc75710_write(temp)

    # /**
    #  *   Send a Set AC address command to the chip.
    #  *
    #  * @param dcram 6-bit DCRAM address
    #  * @param adram 4-bit ADRAM address
    #  */
    def lc75710_set_ac_address(self, dcram, adram):
        # /* Instruction */
        temp = 0x4 << 20

        # /* ADRAM address */
        temp |= (adram & 0xF) << 16

        # /* DCRAM address */
        temp |= (dcram & 0x3F) << 8

        # /* Write to IC */
        self.lc75710_write(temp)

    # /**
    #  *   Send a intensity adjustment command to the chip.
    #  *
    #  * @param intensity 0..240 brightness value (duty cycle)
    #  */
    def lc75710_intensity(self, intensity):
        # /* Instruction */
        temp = 0x5 << 20

        # /* ADRAM address */
        temp |= (intensity & 0xFF) << 8

        # /* Write to IC */
        self.lc75710_write(temp)

    # /**
    #  *   Send a DCRAM write command to the chip.
    #  *
    #  * @param addr 6-bit DCRAM address
    #  * @param data the 8-bit data (character code, CGROM or CGRAM)
    #  */
    def lc75710_dcram_write(self, addr, data):
        # /* Instruction */
        temp = 0x6 << 20

        # /* DCRAM address */
        temp |= (addr & 0x3F) << 8

        # /* ADRAM address */
        temp |= (data & 0xFF) << 0

        # /* Write to IC */
        self.lc75710_write(temp)

    # /**
    #  *   Send a ADRAM write command to the chip.
    #  *
    #  * @param addr 4-bit DCRAM address
    #  * @param data the 8-bit data (arbitrary dots)
    #  */
    def lc75710_adram_write(self, addr, data):
        # /* Instruction */
        temp = 0x7 << 20

        # /* DCRAM address */
        temp |= (addr & 0xF) << 16

        # /* ADRAM address */
        temp |= (data & 0xFF) << 8

        # /* Write to IC */
        self.lc75710_write(temp)

    # /**
    #  *   Send a CGRAM write command to the chip.
    #  *
    #  * @param addr 8-bit CGRAM address
    #  * @param data the 35-bit data (arbitrary dots, forming a 7x5 character)
    #  */
    def lc75710_cgram_write(self, addr, data):
        # /* Instruction */
        temp = 0x8 << 52

        # /* CGRAM address */
        temp |= (addr & 0xFF) << 40

        # /* ADRAM address */
        temp |= data

        # /* Write to IC */
        self.lc75710_select()
        self.lc75710_write_low(temp, 56)
        self.lc75710_deselect()


class Lc75710(Lc75710Low):

    pos = 0

    def __init__(self):
        super().__init__()

    def lc75710_display_hal_power(self, state):
        
        if state == self.DEASPLAY_POWER_OFF:
            self.lc75710_on_off(self.MDATA_AND_ADATA, False, 0xFFFF)
            return

        if state == self.DEASPLAY_POWER_ON:
            self.lc75710_on_off(self.MDATA_AND_ADATA, True, 0xFFFF)
            return

    def lc75710_display_hal_set_cursor(self, char):
        self.pos = self.LC75710_DIGITS - 1 - char

    def lc75710_display_hal_write_char(self, char):
        self.lc75710_dcram_write(self.pos, char)
    
    def lc75710_hal_write_extended(self, size):
        if size < self.LC75710_CGRAM_SIZE:
            self.lc75710_dcram_write(self.pos, size)

    def lc75710_hal_set_extended(self, size, data):
        tmp = 0b00000000

        if size < self.LC75710_CGRAM_SIZE:
            tmp |= data
            data += 1
            tmp |= (data << 8)
            data += 1
            tmp |= (data << 16)
            data += 1
            tmp |= (data << 24)
            data += 1
            tmp |= (data << 32)
            data += 1
            tmp |= (data << 40)
            data += 1
            tmp |= (data << 48)
            data += 1
            tmp |= (data << 56)
            self.lc75710_cgram_write(size, tmp)
