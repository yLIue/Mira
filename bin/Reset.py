import os
import repoPath
from module import debug, Head, getCommitFiles, Staging, LogFile


def Reset(_args: list[str]):
    debug.log(f'调用Reset函数,args: {_args}')
    isHard = False
    if len(_args) == 0:
        return
    if len(_args) == 2:
        _hash = _args[1]
        isHard = True
    else:
        _hash = _args[0]
    _files = []

    for root, dirs, files in os.walk(repoPath.objects / _hash[:2]):
        _files = files

    matcher = [_matcher for _matcher in _files if _matcher.startswith(_hash[2:])]
    if len(matcher) == 0:
        print('无法找到这条记录')
        return
    if len(matcher) > 1:
        print('查找到多条记录')
        return
    _commitHash = _hash[:2] + matcher[0]
    staging = Staging(repoPath.root)
    staging.reset(getCommitFiles(_commitHash))
    _Head = Head(repoPath.root)
    _hashIng = _Head.load()
    if isHard:
        for root, dirs, files in os.walk('.'):
            dirName = root.split('\\')
            if len(dirName) > 1 and dirName[1] in repoPath.miraignore:
                continue
            for file in files:
                _path = f'{root}\\{file}'[2:]
                if _path not in staging.all():
                    os.remove(_path)
                    print(f'删除文件 {file}')
            if root != '.' and not os.listdir(root):
                os.rmdir(root)
                print(f'删除文件夹 {root}')

        for _path, _fileHash in staging.all().items():
            sourcePath = repoPath.objects / _fileHash[:2] / _fileHash[2:]
            aimPath = repoPath.workRoot / _path
            with open(sourcePath, 'rb') as f:
                _data = f.read()
            with open(aimPath, 'wb') as f:
                f.write(_data)
            print(f'重写文件 {_path}')
        print()
    _Head.save(_commitHash)
    LogFile(repoPath.root).add(_hashIng, _commitHash, 'reset', f'moving to {_commitHash}')
    print(f'回退成功')
