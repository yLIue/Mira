import os
import repoPath
from module import debug, getCommand, Error, LogFile, Maps, getCommitFiles, isMira
from .bin_map import *
from debugtools import Color

RegisterFunction = {
    'status': Status,
    'add': Add,
    'push': Push,
    'remove': Remove
}


def Map(_args: list[str]):
    debug.log(f'调用map函数,args: {_args}')
    if not isMira():
        return
    if len(_args) == 0:
        showMap()
        return
    resolveArgs(_args)


def showMap():
    _maps = Maps(repoPath.root)
    _mapsTable = _maps.table
    if len(_mapsTable) == 0:
        print('不存在任何映射\n(使用 "mira map add <映射标记> <文件> <目标路径>..." 添加映射关系)')
        return

    _mapsFiles = _maps.files()
    _commitFiles = getCommitFiles(LogFile(repoPath.root).hash)

    commitIng = []
    modified = []
    delete = []

    for _tag, _data in _mapsTable.items():
        _hash = _data['hash']
        _path = _data['file']
        _aimPath = _data['path']
        _status = eval(_data['status'])
        if _path not in _commitFiles:
            delete.append(('delete', _tag, _path))
            continue
        if not os.path.exists(_aimPath):
            delete.append(('no path', _tag, _path))
            continue

        _commitFileHash = _commitFiles[_path]
        if _hash == _commitFileHash:
            if not _status:
                commitIng.append(('no push', _tag, _path))
            else:
                commitIng.append(('', _tag, _path))
        else:
            modified.append((_tag, _path))
    debug.log(f'commitIng: {commitIng}')
    debug.log(f'modified: {modified}')
    debug.log(f'delete: {delete}')
    printCommitIng(commitIng)
    printDelete(delete)
    printModified(modified)


def printCommitIng(_list):
    if len(_list) == 0:
        print('没有正常映射记录\n')
        return
    print('映射的文件:\n(使用 "mira map push <映射标记>..." 将其映射到对应文件夹)')
    for mode, tag, _path in _list:
        if mode == 'no push':
            mode += ':'
            print(Color.red(f'\t{mode:12}{tag:12}{_path}'))
        else:
            print(Color.green(f'\t{tag:12}{_path}'))
    print()


def printDelete(_list):
    if len(_list) == 0:
        return
    print('失效的映射:\n(使用 "mira map remove <映射标记>..." 来移除标记)')
    for mode, _tag, _file in _list:
        mode += ':'
        print(Color.red(f'\t{mode:12}{_tag:12}{_file}'))


def printModified(_list):
    if len(_list) == 0:
        return
    print(
        '变更的文件:\n(使用 "mira map push <映射标记>..." 将其映射到对应文件夹)')
    for tag, _path in _list:
        print(Color.red(f'\t{"modified:":12}{tag:12}{_path}'))
    print()


def resolveArgs(_args):
    if not len(_args):
        Error.NoArgs()
        return
    _command = getCommand(_args[0], list(RegisterFunction.keys()))
    try:
        RegisterFunction[_command](_args[1:])
    except KeyError:
        Error.NoFindCommand(f'map {_args[0]}', list(RegisterFunction.keys()))
