from module import Path, toPath, IniFile


class Maps:
    def __init__(self, _rope: str | Path):
        self.root = _rope
        self.filePath = toPath(_rope) / 'maps'
        self.table = self.load()

    def load(self) -> dict:
        _dict = {}
        try:
            _dict = IniFile(self.filePath).load()
        except FileNotFoundError:
            pass
        return _dict

    def add(self, _tag, _filePath, _hash, _path, _fileName):
        self.table[_tag] = {
            'file': _filePath,
            'hash': _hash,
            'path': _path,
            'fileName': _fileName,
            'status': False
        }
        self.save()

    def save(self):
        _maps = IniFile(self.filePath)
        _maps.save(self.table)

    def files(self) -> dict:
        _dict = {}
        for _item in self.table.values():
            _dict[_item['file']] = _item['hash']
        return _dict

    def onStatus(self, _file):
        self.table[_file]['status'] = True
        self.save()

    def updateFile(self, _tag, _hash):
        self.table[_tag]['hash'] = _hash
        self.save()
