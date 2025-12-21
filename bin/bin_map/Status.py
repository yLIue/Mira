import repoPath
from module import debug, getCommitFiles, Maps, Head, LogFile, isMira
from debugtools import Color


def Status(_args: list[str]):
    debug.log(f'调用map.Status函数,args: {_args}')
    if not isMira():
        return
    _commitHash = Head(repoPath.root).load()
    if _commitHash == '0' * 40:
        print('当前没有提交记录\n(创建/复制文件并使用 "mira add" 来跟踪)\n(提交文件并使用 "mira commit -m" 来提交)')
        return
    _commitMsg = LogFile(repoPath.root).loadMsg(_commitHash)
    _commitFiles = getCommitFiles(_commitHash)

    print(Color.yellow(f'commit [{_commitHash[:7]}] ') + _commitMsg)
    print()
    _mapFiles = Maps(repoPath.root).files()

    commitIng = []
    delete = []
    untracked = []

    for _path, _hash in _mapFiles.items():
        if _path not in _commitFiles:
            delete.append(_path)
            continue
        commitIng.append(_path)

    for file in _commitFiles:
        if file not in _mapFiles:
            untracked.append(file)
    printCommitIng(commitIng)
    printDelete(delete)
    printUntracked(untracked)


def printDelete(_list):
    if len(_list) == 0:
        return
    print('失效的映射:\n(使用 "mira map remove <映射标记>..." 来移除标记)')
    for _file in _list:
        print(Color.red(f'\t{"delete:":12}{_file}'))
    print()


def printCommitIng(_list):
    if len(_list) == 0:
        print('当前没有映射记录\n')
        return
    print('映射的文件:')
    for _file in _list:
        print(Color.green(f'\t{_file}'))
    print()


def printUntracked(_list):
    if len(_list) == 0:
        return
    print(
        '未映射的文件:\n(使用 "mira map add <映射标记> <文件> <目标路径> <映射文件名>..." 添加映射关系)')
    for _path in _list:
        print(f'\t{Color.red(_path)}')
    print()
