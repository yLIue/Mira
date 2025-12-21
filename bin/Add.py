import os
import repoPath
from module import debug, writeBlob, Staging, isMira, Error


def Add(_args: list[str]):
    debug.log(f'调用Add函数,args: {_args}')
    if not isMira():
        return
    if len(_args) != 1:
        Error.AddArgError()
        return
    _file = _args[0]
    if _file == '.':
        debug.log(f'add all')
        for root, dirs, files in os.walk('.'):
            if '.mira' in root or not files:
                continue
            for file in files:
                _path = f'{root}\\{file}'
                addStaging(_path[2:])
                debug.logOk(f'add {file}')
        return
    addStaging(_file)


def addStaging(_file):
    _path = f'{repoPath.workRoot}\\{_file}'
    _staging = Staging(repoPath.root)
    try:
        with open(_path, 'rb') as f:
            byteData = f.read()
            _hash = writeBlob(byteData)
            _staging.add(_file, _hash)
        debug.logOk(f'add {_file}')
    except FileNotFoundError:
        try:
            _staging.delete(_file)
            debug.logOk(f'del {_file}')
        except KeyError:
            Error.NotFindFile(_file)
