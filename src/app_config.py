

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
                'mopidy/audio_option': {
                    'controller': 'amp_iot.src.amp.controller.mopidy.MopidyController',
                    'action': 'audio_option'
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
                    'amp_iot.src.amp.driver.power_led.PowerLed': 'InvokableFactory',
                    'amp_iot.src.amp.driver.key.Key': 'InvokableFactory',
                    'amp_iot.src.amp.driver.led_strip.LedStrip': 'InvokableFactory',
                    'amp_iot.src.amp.driver.mcp3008.Mcp3008': 'InvokableFactory',
                    'amp_iot.src.amp.driver.amplifier.Amplifier': 'InvokableFactory',
                },
                'ConfigurableFactory': {

                    # controllers
                    'amp_iot.src.amp.controller.lcd.LcdController': ['amp_iot.src.amp.model.lcd.Lcd'],
                    'amp_iot.src.amp.controller.power.PowerController': ['amp_iot.src.amp.model.power.Power'],
                    'amp_iot.src.amp.controller.audio.AudioController': ['amp_iot.src.amp.model.audio.Audio'],
                    'amp_iot.src.amp.controller.mopidy.MopidyController': [
                        'amp_iot.src.amp.model.audio.Audio',
                        'amp_iot.src.amp.model.light.light_controller.LightController',
                        'amp_iot.src.lib.storage.Storage',
                    ],

                    # models
                    'amp_iot.src.amp.model.lcd.Lcd': [],
                    'amp_iot.src.amp.model.audio.Audio': [
                        'amp_iot.src.amp.driver.preamp.Preamp',
                        'amp_iot.src.lib.audio_map.AudioMap',
                        'amp_iot.src.amp.driver.power_led.PowerLed',
                        'amp_iot.src.amp.driver.amplifier.Amplifier',
                    ],
                    'amp_iot.src.amp.model.power.Power': [
                        'amp_iot.src.amp.driver.power.Power',
                        'amp_iot.src.amp.driver.power_led.PowerLed',
                        'amp_iot.src.amp.driver.preamp.Preamp',
                        'amp_iot.src.amp.driver.amplifier.Amplifier',
                    ],
                    'amp_iot.src.amp.model.key.audio.KeyAudio': [
                        'amp_iot.src.lib.storage.Storage',
                        'amp_iot.src.amp.driver.preamp.Preamp',
                        'amp_iot.src.amp.model.light.light.Light'
                    ],
                    'amp_iot.src.amp.model.light.effect.LightEffect': [
                        'amp_iot.src.lib.storage.Storage',
                        'amp_iot.src.amp.driver.led_strip.LedStrip'
                    ],
                    'amp_iot.src.amp.model.light.light_controller.LightController': [
                        'amp_iot.src.lib.storage.Storage',
                        'amp_iot.src.amp.driver.led_strip.LedStrip',
                        'amp_iot.src.amp.driver.spectrum.Spectrum',
                    ],
                    'amp_iot.src.amp.model.light.light.Light': [
                        'amp_iot.src.lib.storage.Storage',
                        'amp_iot.src.amp.model.light.light_controller.LightController'
                    ],

                    # drivers
                    'amp_iot.src.amp.driver.preamp.Preamp': ['amp_iot.src.amp.driver.preamp_data.PreampData'],
                    'amp_iot.src.amp.driver.preamp_data.PreampData': ['amp_iot.src.lib.storage.Storage'],
                    'amp_iot.src.amp.driver.spectrum.Spectrum': ['amp_iot.src.amp.driver.mcp3008.Mcp3008'],
                }
            },
            'listeners': {
                'key_change_event': {
                    'amp_iot.src.amp.model.key.audio.KeyAudio': 'key_observer',
                    'amp_iot.src.amp.model.power.Power': 'key_observer',
                },
            }
        }
