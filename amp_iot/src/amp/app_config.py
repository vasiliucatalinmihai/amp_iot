

class ApplicationConfig:

    @staticmethod
    def get_application_config():
        return {
            'router': {
                'power/power_on': {
                    'controller': 'amp_iot.src.amp.controller.power.PowerController',
                    'action': 'power_on'
                },
                'power/power_off': {
                    'controller': 'amp_iot.src.amp.controller.power.PowerController',
                    'action': 'power_off'
                },

                'audio/process': {
                    'controller': 'amp_iot.src.amp.controller.audio.AudioController',
                    'action': 'process'
                },
                'lcd/display': {
                    'controller': 'amp_iot.src.amp.controller.lcd.LcdController',
                    'action': 'display'
                },
            },
            'object_manager': {
                'alias': {

                },
                'singleton': {

                },
                'factories': {
                    'amplifier_client': 'amp_iot.src.amp.client_factory.ClientFactory',
                    'application_client': 'amp_iot.src.amp.client_factory.ClientFactory',

                    # lib
                    'amp_iot.src.lib.storage.Storage': 'InvokableFactory',
                    'amp_iot.src.lib.audio_map.AudioMap': 'InvokableFactory',

                    # drivers
                    'amp_iot.src.amp.driver.power.Power': 'InvokableFactory',
                    'amp_iot.src.amp.driver.led_shifter.LedShifter': 'InvokableFactory',
                },
                'ConfigurableFactory': {

                    # controllers
                    'amp_iot.src.amp.controller.lcd.LcdController': ['amp_iot.src.amp.model.lcd.Lcd'],
                    'amp_iot.src.amp.controller.power.PowerController': [
                        'amp_iot.src.lib.storage.Storage',
                        'amp_iot.src.amp.driver.led_shifter.LedShifter'
                    ],
                    'amp_iot.src.amp.controller.audio.AudioController': ['amp_iot.src.amp.model.audio.Audio'],

                    # models
                    'amp_iot.src.amp.model.lcd.Lcd': [],
                    'amp_iot.src.amp.model.audio.Audio': [
                        'amp_iot.src.amp.driver.preamp.Preamp',
                        'amp_iot.src.lib.audio_map.AudioMap'

                    ],

                    # drivers
                    'amp_iot.src.amp.driver.preamp.Preamp': ['amp_iot.src.amp.driver.preamp_data.PreampData'],
                    'amp_iot.src.amp.driver.preamp_data.PreampData': ['amp_iot.src.lib.storage.Storage'],
                }
            },
            'listeners': {
                'event_test': {
                    'amp_iot.src.amp.model.lcd.Lcd': 'method',
                    'amp_iot.src.amp.model.audio.Audio': 'method'
                },
            }
        }
