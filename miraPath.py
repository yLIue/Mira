from module import debug


class Path:
    def __init__(self, _path: str) -> None:
        self.path = _path

    def __str__(self):
        return self.path

    def __truediv__(self, _path: str):
        return Path(self.path + '\\' + _path)

    def __fspath__(self) -> str:
        return self.path


miraPath_path = '\\'.join(__file__.split('\\')[:-1]) + '\\'
debug.setLocalPath(miraPath_path)
# debug.cleanDebug()

root = Path(debug.DebugPath())
etcDir = root / 'etc'
configIni = etcDir / 'config.ini'
