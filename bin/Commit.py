import repoPath
from module import debug, Staging, writeBlob, LogFile, Head, isMira, Error


def Commit(_args: list[str]):
    debug.log(f'调用Commit函数,args: {_args}')
    if not isMira():
        return
    if len(_args) != 2 or _args[0] != '-m':
        Error.CommitArgError()
        return

    _dict = Staging(repoPath.root).all()
    if len(_dict) == 0:
        print('初次提交\n没有要提交的内容(创建/复制文件并使用 "mira add" 来跟踪)')
        return
    _tree = getTreeDict(_dict)
    _commitHash = getTreeByte(_tree)
    debug.logOk(f'commitHash生成成功: {_commitHash}')
    writeCommit(_commitHash, _args[1])
    Head(repoPath.root).save(_commitHash)


def getTreeDict(_data: dict) -> dict:
    _tree = {}
    for file, _hash in _data.items():
        path = file.split('\\')
        _cur = _tree
        for _p in path[:-1]:
            _cur = _cur.setdefault(_p, {})
        _cur[path[-1]] = _hash
    return _tree


def getTreeByte(_tree: dict):
    _data = b""

    for _file in sorted(_tree.keys()):
        value = _tree[_file]

        if isinstance(value, dict):
            _hashFile = getTreeByte(value)
            _data += f'dir {_file}\0'.encode()
            _data += bytes.fromhex(_hashFile)
        else:
            _data += f'file {_file}\0'.encode()
            _data += bytes.fromhex(value)

    return writeBlob(_data)


def writeCommit(_nextHash, _msg):
    HEAD = LogFile(repoPath.root)
    if HEAD.hash == _nextHash:
        debug.logError('与上次哈希一致')
        print('没有要提交的内容')
        return
    HEAD.add(HEAD.hash, _nextHash, 'commit', _msg)
    print(f'[{_nextHash[:7]}] {_msg}')
    debug.logOk('提交成功')
