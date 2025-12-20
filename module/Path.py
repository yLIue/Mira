class Path:
    def __init__(self, _path: str) -> None:
        self.path = _path

    def __str__(self):
        return self.path

    def __truediv__(self, _path: str):
        return Path(self.path + '\\' + _path)

    def __fspath__(self) -> str:
        return self.path
