import repoPath


def getCommitFiles(_commitHash, _prefix=''):
    files = {}
    if _commitHash == '0'*40:
        return files
    with open(repoPath.objects / _commitHash[:2] / _commitHash[2:], 'rb') as f:
        _data = f.read()
        _head = 0

        while _head < len(_data):
            _nextHead = _data.index(b'\0', _head)
            _header = _data[_head:_nextHead].decode()
            mode, fileName = _header.split(' ', 1)
            _hash = _data[_nextHead + 1:_nextHead + 21].hex()
            _path = f"{_prefix}{fileName}"
            if mode == 'dir':
                otherFiles = getCommitFiles(_hash, _path+'\\')
                files.update(otherFiles)
            else:
                files[_path] = _hash
            _head = _nextHead + 21

        return files
