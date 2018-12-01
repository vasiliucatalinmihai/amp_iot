

class ApplicationConfig:

    @staticmethod
    def get_application_config():
        return {
            'router': {
                'mopidy/audio_option': {
                    'controller': 'amp_iot.src.app.controller.mopidy.MopidyController',
                    'action': 'audio_option'
                },
            },
            'object_manager': {
                'alias': {

                },
                'singleton': {

                },
                'factories': {
                    'amplifier_client': 'amp_iot.src.app.client_factory.ClientFactory',
                    'application_client': 'amp_iot.src.app.client_factory.ClientFactory',

                    # lib
                    'amp_iot.src.lib.storage.Storage': 'InvokableFactory',
                    'amp_iot.src.lib.audio_map.AudioMap': 'InvokableFactory',

                    # model
                },
                'ConfigurableFactory': {

                    # controller
                    'amp_iot.src.app.controller.mopidy.Mopidy': ['amp_iot.src.app.model.audio.Audio'],
                    # model
                    'amp_iot.src.app.model.audio.Audio': [
                        'amp_iot.src.lib.audio_map.AudioMap',
                        'amp_iot.src.app.amp_client.AmpClient'
                    ],

                }
            },
            'listeners': {
                'action': {
                    'class': 'method',
                    'class2:': 'method'
                },
            }
        }
