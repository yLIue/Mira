import hashlib
import os
import repoPath
from .Path import Path


def getHash(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def writeBlob(_data: bytes) -> str:
    _hash = getHash(_data)
    _dir = _hash[:2]
    _file = _hash[2:]
    try:
        os.mkdir(repoPath.objects / _dir)
    except FileExistsError:
        pass
    with open(repoPath.objects / _dir / _file, 'wb') as f:
        f.write(_data)
    return _hash


def toPath(_path: str | Path) -> Path:
    if isinstance(_path, Path):
        return _path
    return Path(_path)
