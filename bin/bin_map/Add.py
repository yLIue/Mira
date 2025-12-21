import repoPath
from module import debug, getCommitFiles, Maps, isMira, Error, Head


def Add(_args: list[str]):
    debug.log(f'调用map.Add函数,args: {_args}')
    if not isMira():
        return
    if len(_args) < 3:
        Error.MapAddArgError()
        return

    if len(_args) == 4:
        _fileName = _args[3]
    else:
        _fileName = _args[1].split('\\')[-1]
    maps = Maps(repoPath.root)
    _commitFiles = getCommitFiles(Head(repoPath.root).load())
    _tag = _args[0]
    if _args[1] not in _commitFiles:
        print(f'致命错误: {_args[1]} 不存在')
        return
    if _tag in maps.table:
        print(f'致命错误: tag {_tag} 重复')
        return

    _file = _args[1]
    maps.add(_tag, _file, _commitFiles[_file], _args[2], _fileName)
    debug.logOk(f'map add {_tag} {_file}')
