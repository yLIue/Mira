import sys
import traceback
import miraPath
import miraInfo
import miraPrint
from module import *
from bin import *


# 函数注册器
RegisterFunction = {
    'config': Config,
    'status': Status,
    'add': Add,
    'init': Init,
    'commit': Commit,
    'look': Look,
    'log': Log,
    'map': Map,
    'reset': Reset
}


def initMira():
    try:
        os.mkdir(miraPath.etc)
        _configIni = IniFile(miraPath.configIni)
        _configDict = {
            'info': {
                'version': miraInfo.version
            },
            'user': {
                'name': miraInfo.defaultUser,
                'email': miraInfo.defaultEmail
            }
        }
        _configIni.save(_configDict)
        debug.logOk('mira初始化成功')
    except FileExistsError:
        debug.logError('初始化失败 文件已经存在')


def resolveArgs(_args):
    if not len(_args):
        miraPrint.noCommand()
        return
    _command = getCommand(_args[0], list(RegisterFunction.keys()))
    try:
        RegisterFunction[_command](_args[1:])
    except KeyError:
        Error.NoFindCommand(_args[0], list(RegisterFunction.keys()))


def main() -> None:
    try:
        initMira()
        resolveArgs(sys.argv[1:])
    except Exception:
        debug.logError(f'异常!!! {traceback.format_exc()}')


if __name__ == '__main__':
    main()
