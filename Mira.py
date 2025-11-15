import os
from debugtools import *
import sys

# initGlobal
PATH = '\\'.join(sys.argv[0].split('\\')[:-1]) + '\\'
# debug
debug = Debug('Mira', True)
debug.logSet(_fillFunc=True)
debug.showDebugLog()
debug.setLocalPath(PATH)
debug.cleanDebug()
# global
LOCAL_PATH = debug.DebugPath(PATH)
COMMANDS = {}


def getCommand(_command: str, _commands: dict) -> callable or None:
    listMatcher = [_matcher for _matcher in _commands.keys() if _matcher.startswith(_command)]
    if len(listMatcher) == 0:
        debug.logError(f'命令解析失败:不存在 {_command} 命令')
        print(f"无法识别的命令 '{_command}' ")
        Help()
        return None
    if len(listMatcher) > 1:
        debug.logError(f'命令解析失败:多个命令:{listMatcher}')
        print('指令冲突 冲突指令:')
        for i in listMatcher:
            print(i)
        return None
    return _commands[listMatcher[0]]


def Config():
    print('Config')


def Help():
    print('Help')


def resolveArgs(_args: list[str]):
    if not len(_args):
        debug.log('无指令')
        print('没有任何参数')
        Help()
        return
    try:
        _command = getCommand(_args[0], COMMANDS)()
    except TypeError:
        return


def initMira() -> None:
    global COMMANDS
    COMMANDS = {
        'config': Config,
        'c': Config,
        'help': Help
    }
    try:
        os.mkdir(LOCAL_PATH + 'config')
        with open(LOCAL_PATH + 'config\\user.cfg', 'w') as f:
            f.write('user.name:default\nuser.email:default@mira.com')
        debug.logOk('初始化成功')
    except FileExistsError:
        debug.logError('初始化失败:配置文件存在')


def readConfig() -> dict:
    with open(LOCAL_PATH + 'config\\user.cfg', 'r') as f:
        _infos = {}
        for _line in f.readlines():
            _listInfo = _line.split('\n')[0].split(':')
            _listTitle = _listInfo[0].split('.')
            try:
                _infos[_listTitle[0]][_listTitle[1]] = _listInfo[1]
            except KeyError:
                _dictTitle = {_listTitle[1]: _listInfo[1]}
                _infos[_listTitle[0]] = _dictTitle
        debug.logOk(f'读取配置文件成功:{_infos}')
        return _infos


def main() -> None:
    initMira()
    readConfig()
    args = sys.argv[1:]
    resolveArgs(args)


if __name__ == '__main__':
    main()
