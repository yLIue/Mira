import time
import miraPath
from module import toPath, IniFile


class LogFile:
    def __init__(self, _rope):
        self.root = _rope
        self.filePath = toPath(_rope) / 'logs' / 'HEAD'
        self.hash = self.loadNextHash()

    def add(self, _hash, _newHash, _type, _msg):
        userInfo = IniFile(miraPath.configIni).load()["user"]
        _commit = f'{_hash} {_newHash} {userInfo["name"]} <{userInfo["email"]}> {int(time.time())}\t{_type}: {_msg}\n'
        self.save(_commit)

    def loadMsg(self, _hash):
        _msg = ''
        try:
            with open(self.filePath, 'r', encoding='utf-8') as f:
                for line in f.readlines()[::-1]:
                    datas = line.split(' ')
                    if datas[1] == _hash:
                        _msg = datas[-1][:-1]
                        break
        except FileNotFoundError:
            pass
        return _msg

    def loadNextHash(self):
        _hash = ''
        try:
            with open(self.filePath, 'r', encoding='utf-8') as f:
                _hash = f.readlines()[-1][41:81]
        except FileNotFoundError:
            _hash = '0' * 40
        return _hash

    def save(self, _commit):
        with open(self.filePath, 'a', encoding='utf-8') as f:
            f.write(_commit)

    def all(self):
        _list = []
        try:
            with open(self.filePath, 'r', encoding='utf-8') as f:
                for line in f.readlines()[::-1]:
                    datas = line.split(' ')
                    _commit = {
                        'type': datas[4].split('\t')[1][:-1],
                        'hash': datas[1],
                        'user': datas[2],
                        'email': datas[3],
                        'time': datas[4].split('\t')[0],
                        'msg': datas[-1][:-1]
                    }
                    _list.append(_commit)

        except FileNotFoundError:
            pass
        return _list
