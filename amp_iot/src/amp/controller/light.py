
from amp_iot.src.lib.framework.abstract_controller import AbstractController


class LightController(AbstractController):

    def set_btn_action(self):
        btn = self.get_param('btn')
        color = self.get_param('color')