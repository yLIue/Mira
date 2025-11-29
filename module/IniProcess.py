from debugtools import *


class IniProcess:
    def __init__(self, _filePath):
        self.path = _filePath
        self.status = self.init()
        self.debug = Debug('IniProcess')

    def init(self) -> bool:
        try:
            with open(self.path, 'a+', encoding='utf-8'):
                pass
            return True
        except FileNotFoundError:
            self.debug.logError('初始化失败')
            return False
        except FileExistsError:
            return True

    def save(self, _data: dict) -> None:
        if not self.status:
            return
        with open(self.path, 'a', encoding='utf-8') as f:
            for title, dictKey in _data.items():
                f.write(f'[{title}]\n')
                for key, value in dictKey.items():
                    f.write(f'\t{key} = {value}\n')
                f.write('\n')

    def load(self):
        if not self.status:
            return
        _data = {}
        title = None
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split('\n')[0]
                if line.startswith('[') and line.endswith(']'):
                    title = line[1:-1]
                    _data[title] = {}
                if '=' in line and title is not None:
                    listKey = line.split('=')
                    key = listKey[0].strip()
                    value = listKey[1].strip()
                    _data[title][key] = value
        return _data
