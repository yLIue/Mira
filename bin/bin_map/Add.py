import repoPath
from module import debug, LogFile, getCommitFiles, Maps


def Add(_args: list[str]):
    debug.log(f'调用map.Add函数,args: {_args}')
    if len(_args) < 3:
        print('参数错误')
        return
    maps = Maps(repoPath.root)
    _commitFiles = getCommitFiles(LogFile(repoPath.root).hash)
    _tag = _args[0]
    _file = _args[1]
    maps.add(_tag, _file, _commitFiles[_file], _args[2], _args[3])
    debug.logOk(f'map add {_tag} {_file}')
