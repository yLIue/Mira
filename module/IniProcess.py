from .Debug import debug


def save(_path: str, _data: dict) -> None:
    try:
        with open(_path, 'w', encoding='utf-8') as f:
            for title, dictKey in _data.items():
                f.write(f'[{title}]\n')
                for key, value in dictKey.items():
                    f.write(f'\t{key} = {value}\n')
                f.write('\n')
        debug.log()
        debug.logOk('保存配置文件成功')
        debug.log(f'path: {_path}', 'OUTPUT')
        debug.log(f'dict: {_data}', 'OUTPUT')
        debug.log()
    except FileNotFoundError:
        debug.logError(f'保存配置文件失败 path: {_path}')
        # raise FileNotFoundError


def load(_path: str) -> dict:
    _data = {}
    title = None
    try:
        with open(_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split('\n')[0]
                if line.startswith('[') and line.endswith(']'):
                    title = line[1:-1]
                    _data[title] = {}
                if '=' in line and title is not None:
                    listKey = line.split('=')
                    key = listKey[0].strip()
                    value = listKey[1].strip()
                    if value.startswith('[') and line.endswith(']'):
                        value = loadList(value[1:-1])
                    _data[title][key] = value
        return _data
    except FileNotFoundError:
        debug.logError(f'读取配置文件失败 path: {_path}')
        raise FileNotFoundError


def loadList(_str: str) -> list:
    _list = []
    _strs = _str.split(',')
    if len(_strs) == 0:
        return _list
    for _item in _strs:
        if _item.startswith("'") and _item.endswith("'"):
            _list.append(_item[1:-1])
    return _list
