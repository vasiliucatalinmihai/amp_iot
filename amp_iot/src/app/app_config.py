

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

                },
                'factories': {
                    'amp_iot.src.lib.storage.Storage': 'InvokableFactory',
                    'amp_iot.src.lib.jsonsocket.Client': 'InvokableFactory',
                },
                'ConfigurableFactory': {
                    'amp_iot.src.app.amp_client.AmpClient': ['amp_iot.src.lib.storage.Storage', 'amp_iot.src.lib.jsonsocket.Client'],

                }
            },
            'listeners': {
                'action': {
                    'class': 'method',
                    'class2:': 'method'
                },
            }
        }
