

class lcd:

    STAND_BY = 'stand_by'
    LOADING = 'loading'
    AUDIO_SETUP = 'audio_setup'
    PLAYING = 'playing'

    VARIOUS_ACTION = 'smart_home_action'

    def __init__(self):
        _states = [
            self.STAND_BY, self.LOADING, self.AUDIO_SETUP, self.PLAYING,
            self.VARIOUS_ACTION
        ]
        self._state = self.STAND_BY


    def render(self):
        pass