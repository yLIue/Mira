import repoPath
from datetime import datetime
from module import debug, LogFile, Head
from debugtools import Color


def Log(_args: list[str]):
    debug.log(f'调用Log函数,args: {_args}')
    _commits = LogFile(repoPath.root).all()
    index = True
    show = False
    showHash = Head(repoPath.root).load()
    for _commit in _commits:
        if _commit["hash"] == showHash:
            show = True
        if _commit['type'] == 'reset':
            show = False
            showHash = _commit['hash']
            continue

        if not show:
            continue
        if not index:
            print()
        _time = datetime.fromtimestamp(int(_commit["time"])).strftime('%Y %m %d %H:%M:%S')
        print(Color.yellow(f'commit {_commit["hash"]}'))
        print(f'操作人: {_commit["user"]} {_commit["email"]}')
        print(f'时间: {_time}')
        print()
        print(f'\t{_commit["msg"]}')
        index = False
