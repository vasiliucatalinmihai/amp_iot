

class ApplicationConfig:

    @staticmethod
    def get_application_config():
        return {
            'router': {

            },
            'object_manager': {
                'alias': {

                },
                'singleton': {
                    'src.lib.storage.Storage': True,
                },
                'factories': {
                    # lib
                    'src.lib.storage.Storage': 'InvokableFactory',


                    # 'amplifier_client': 'amp_iot.src.amp.client_factory.ClientFactory',
                    # 'application_client': 'amp_iot.src.amp.client_factory.ClientFactory',

                    # drivers
                    'src.driver.ads1110.Ads1110': 'InvokableFactory',
                    'src.driver.led_strip.LedStrip': 'InvokableFactory',
                    'src.driver.key.Key': 'InvokableFactory',
                    'src.driver.encoder.Encoder': 'InvokableFactory',
                    'src.driver.amplifier.Amplifier': 'InvokableFactory',
                },
                'ConfigurableFactory': {
                    # drivers
                    'src.driver.tda7419_data.Tda7419Data' : ['src.lib.storage.Storage'],
                    'src.driver.tda7419.Tda7419': ['src.driver.tda7419_data.Tda7419Data'],
                    'src.driver.spectrum.Spectrum': ['src.driver.ads1110.Ads1110'],
                }
            },
            'listeners': {
                'key_change_event': {
                    # 'amp_iot.src.amp.model.key.audio.KeyAudio': 'key_observer',
                    # 'amp_iot.src.amp.model.power.Power': 'key_observer',
                },
            }
        }
