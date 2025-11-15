import os
from debugtools import Debug

# debug
debug = Debug('Mira', True)
debug.logSet(_fillFunc=True)
debug.showDebugLog()
debug.cleanDebug()
# global
PATH = '\\'.join(__file__.split('\\')[:-1]) + '\\'
LOCAL_PATH = debug.DebugPath(PATH)


def initMira():
    try:
        os.mkdir(LOCAL_PATH + 'config')
        with open(LOCAL_PATH + 'config\\user.cfg', 'w') as f:
            f.write('userName:default\nuserEmail:default@mira.com')
        debug.logOk('初始化成功')
    except FileExistsError:
        debug.logError('初始化失败:配置文件存在')


def readConfig() -> dict:
    with open(LOCAL_PATH + 'config\\user.cfg', 'r') as f:
        _infos = {}
        for _item in f.readlines():
            _itemInfo = _item.split('\n')[0].split(':')
            _infos[_itemInfo[0]] = _itemInfo[1]
        debug.logOk(f'读取配置文件成功:{_infos}')
        return _infos


def main() -> None:
    initMira()
    readConfig()


if __name__ == '__main__':
    main()
