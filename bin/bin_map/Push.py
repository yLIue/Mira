import repoPath
from module import debug, Maps, getCommitFiles, LogFile, isMira


def Push(_args: list[str]):
    debug.log(f'调用map.Push函数,args: {_args}')
    if not isMira():
        return
    if len(_args) == 0 and len(_args) > 1:
        print('传参错误')
        return
    if _args[0] == '.':
        index = True
        for tag in Maps(repoPath.root).table.keys():
            if not index:
                print()
            mapPush(tag)
            index = False
        return
    tag = _args[0]
    mapPush(tag)


def mapPush(tag):
    _commitFiles = getCommitFiles(LogFile(repoPath.root).hash)
    maps = Maps(repoPath.root)

    maps.updateFile(tag, _commitFiles[maps.table[tag]['file']])

    mapTable = maps.table

    fileData = mapTable[tag]
    fileHash = fileData['hash']
    aimPath = f'{fileData["path"]}\\{fileData["fileName"]}'
    sourcePath = repoPath.objects / fileHash[:2] / fileHash[2:]
    with open(sourcePath, 'rb') as f:
        file = f.read()
    with open(aimPath, 'wb') as f:
        f.write(file)
    print(f'{tag}.{fileData["file"]} 映射成功 [{fileHash[:7]}]\n映射路径: {aimPath}')
    maps.onStatus(tag)
    debug.logOk(f'push {tag}.{fileData["file"]}')
