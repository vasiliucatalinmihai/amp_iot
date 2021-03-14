

class lcd:

    STAND_BY = 'stand_by'
    LOADING = 'loading'
    AUDIO_SETUP = 'audio_setup'
    PLAYING = 'playing'

    VARIOUS_ACTION = 'smart_home_action'

    _state = self.STAND_BY

    _states = [
        self.STAND_BY, self.LOADING, self.AUDIO_SETUP, self.PLAYING,
        self.VARIOUS_ACTION
    ]

    def __init__(self):
        self._state = self.STAND_BY


    def render(self):
        pass