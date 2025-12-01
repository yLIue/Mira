import sys
from module import *
from bin import *

# initGlobal
PATH = '\\'.join(__file__.split('\\')[:-1]) + '\\'
debug.setLocalPath(PATH)

# 可选,清除debug的文件夹
# debug.cleanDebug()

# global
LOCAL_PATH = debug.DebugPath(PATH)
DIRECTORY_PATH = f'{LOCAL_PATH}etc\\directories.ini'
DIRECTORY = {}
CONFIG = {}
COMMANDS = {}
FUNCTION_DICT = {
    'config': Config
}


def loadConfig() -> None:
    global CONFIG, DIRECTORY, COMMANDS
    try:
        DIRECTORY = IniProcess.load(DIRECTORY_PATH)
    except FileNotFoundError:
        InitMira(LOCAL_PATH)
        DIRECTORY = IniProcess.load(DIRECTORY_PATH)
    CONFIG = IniProcess.load(DIRECTORY['etc']['configFile'])
    COMMANDS = IniProcess.load(DIRECTORY['etc']['commandsFile'])

    debug.log()
    debug.logOk('读出配置文件')
    debug.log(f'directory: {DIRECTORY}', 'OUTPUT')
    debug.log(f'config: {CONFIG}', 'OUTPUT')
    debug.log(f'commands: {COMMANDS}', 'OUTPUT')
    debug.log()


def resolveArgs(_args):
    if not len(_args):
        Error.NoArgs()
        return

    _command = getCommand(_args[0], list(COMMANDS.keys()))
    FUNCTION_DICT[_command](_args[1:], {
        'commands': COMMANDS[_command],
        'config': CONFIG,
        'directory': DIRECTORY
    })


def main() -> None:
    loadConfig()
    resolveArgs(sys.argv[1:])


if __name__ == '__main__':
    main()
