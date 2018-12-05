
from amp_iot.src.lib.framework.abstract_controller import AbstractController
from amp_iot.src.amp.model.power import Power


class PowerController(AbstractController):

    def __init__(
            self,
            power_model: Power,
    ):
        self._power_model = power_model

    def power_on_action(self):
        self._power_model.power_on()

    def power_off_action(self):
        self._power_model.power_off()

    def power_state(self):
        return self._power_model.get_power()
