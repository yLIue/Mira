from .utils import *


class Head:
    def __init__(self, _rope):
        self.root = _rope
        self.filePath = toPath(_rope) / 'HEAD'

    def save(self, _hash):
        with open(self.filePath, 'w') as f:
            f.write(_hash)

    def load(self):
        _hash = '0' * 40
        try:
            with open(self.filePath, 'r') as f:
                _hash = f.read()
        except FileNotFoundError:
            pass
        return _hash
