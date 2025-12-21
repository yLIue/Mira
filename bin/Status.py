import os
import repoPath
from module import debug, Staging, getCommitFiles, writeBlob, Head, isMira
from debugtools import Color


def Status(_args: list[str]):
    debug.log(f'调用Status函数,args: {_args}')
    if not isMira():
        return
    _commitFiles = getCommitFiles(Head(repoPath.root).load())
    if len(_commitFiles) == 0:
        print('当前没有提交\n')

    _staging = Staging(repoPath.root).all()
    staged = []
    unstaged = []
    untracked = []
    work_files = []

    for root, dirs, files in os.walk('.'):
        dirName = root.split('\\')
        if len(dirName) > 1 and dirName[1] in repoPath.miraignore:
            continue
        for file in files:
            _path = f'{root}\\{file}'
            work_files.append(_path[2:])

    for _path, _hash in _staging.items():
        workFilePath = repoPath.workRoot / _path
        if not os.path.exists(workFilePath):
            if _path in _commitFiles:
                if _commitFiles[_path] != _hash:
                    staged.append(("deleted", _path))
                else:
                    unstaged.append(("deleted", _path))
            continue

        with open(workFilePath, 'rb') as f:
            WorkFileHash = writeBlob(f.read())

        if _path not in _commitFiles:
            staged.append(("new file", _path))
        elif _commitFiles[_path] != _hash:
            staged.append(("modified", _path))
        if _hash != WorkFileHash:
            unstaged.append(("modified", _path))

    for file in work_files:
        if file not in _staging:
            untracked.append(file)
    printStaged(staged)
    printUnstaged(unstaged)
    printUntracked(untracked)
    print(f'提交(使用 "mira commit -m <注释>...")')


def printUntracked(_untracked: list):
    if len(_untracked) == 0:
        return
    print('未跟踪的文件:\n(使用 "mira add <文件>..." 将其包含在即将提交的内容中)')
    for _path in _untracked:
        print(f'\t{Color.red(_path)}')
    print()


def printStaged(_staged: list):
    if len(_staged) == 0:
        return
    print(f'将要提交的更改:')
    for _type, _path in _staged:
        _type += ':'
        print(f'\t{Color.green(f"{_type:12}{_path}")}')
    print()


def printUnstaged(_unstaged: list):
    if len(_unstaged) == 0:
        return
    print('未暂存但提交的更改')
    for _type, _path in _unstaged:
        _type += ':'
        print(f'\t{Color.red(f"{_type:12}{_path}")}')
        print()
