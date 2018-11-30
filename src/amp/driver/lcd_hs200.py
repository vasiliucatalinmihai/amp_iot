
from amp_iot.src.amp.driver.sanyo_ccb import SanyoCCB


# datasheet https://pdf1.alldatasheet.com/datasheet-pdf/view/40928/SANYO/LC75710NE.html
class Lcd(SanyoCCB):

    def __init__(self, clock_pin, data_pin, cip_pin):
        super().__init__(clock_pin, data_pin, cip_pin)

    def _get_blink(self):
        pass

    def _get_on_of(self):
        pass

    def _get_shift(self):
        pass

    def _get_register_load(self):
        pass

    def _get_ac_address(self):
        pass

    def _get_intensity_adjustment(self):
        pass

    def _get_dc_ram(self):
        pass

    def _get_ad_ram(self):
        pass

    def _get_cg_ram(self):
        pass

