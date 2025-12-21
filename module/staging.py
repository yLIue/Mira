from module import Path, toPath


class Staging:
    def __init__(self, _rope: str | Path):
        self.root = _rope
        self.filePath = toPath(_rope) / 'staging'
        self.table = self.load()

    def add(self, _filePath: str, _hash: str) -> None:
        self.table[_filePath] = _hash
        self.save()

    def all(self) -> dict:
        return self.table

    def save(self) -> None:
        with open(self.filePath, 'w', encoding='utf-8') as f:
            for _file, _hash in self.table.items():
                f.write(f'{_file} = {_hash}\n')

    def delete(self, _path: str) -> None:
        self.table.pop(_path)
        self.save()

    def load(self) -> dict:
        _dict = {}
        try:
            with open(self.filePath, 'r', encoding='utf-8') as f:
                _lines = f.readlines()
                for _line in _lines:
                    _table = _line.split('=')
                    _file = _table[0].strip()
                    _hash = _table[1].strip()
                    _dict[_file] = _hash
        except FileNotFoundError:
            pass
        return _dict

    def reset(self, _table: dict) -> None:
        self.table = _table
        self.save()
