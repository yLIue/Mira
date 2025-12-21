import repoPath
from module import debug, isMira, Maps, Error


def Remove(_args: list[str]):
    debug.log(f'调用map函数,args: {_args}')
    if not isMira():
        return
    if len(_args) == 0 or len(_args) > 1:
        Error.MapRemoveArgError()
        return
    _tag = _args[0]
    try:
        Maps(repoPath.root).delete(_tag)
        print(f'删除 {_tag}')
    except KeyError:
        Error.NotFindTag(_tag)
