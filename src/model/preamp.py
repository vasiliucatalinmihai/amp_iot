from src.model import Model

class Preamp(Model):

    data = {
        'volume': 0,
        'bass': 0,
        'treble': 0,
        'balance': 0,
        'loudness' : 0,
        'gain': 0,
        'input': 0
    }

    def __init__(self):
        super().__init__()
