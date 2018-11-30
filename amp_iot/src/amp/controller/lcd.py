

from amp_iot.src.lib.framework.abstract_controller import AbstractController


class LcdController(AbstractController):

    def __init__(self, lcd):
        self._lcd = lcd

    def display_action(self):
        action_type = self.get_param('type')
        data = self.get_param('data', False)

        if action_type == 'icon':
            return self._lcd.set_icon(data)
        else:
            return self._lcd.set_text(data)
