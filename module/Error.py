from .Debug import debug


def NoArgs():
    _func = debug.getFunc(1)
    debug.log()
    debug.logError('没有任何指令', _func)
    debug.log()
    print('没有任何参数')


def NoFindCommand(_command, _commands):
    _func = debug.getFunc(1)
    debug.log()
    debug.logError(f'命令解析失败: 无法识别', _func)
    debug.log(f'command: {_command}', 'OUTPUT', _func)
    debug.log(f'commands: {_commands}', 'OUTPUT', _func)
    debug.log()
    print(f"无法识别的命令 '{_command}'")


def NotMira():
    _func = debug.getFunc(1)
    debug.logError('不存在mira仓库', _func)
    print('致命错误: 不是一个 mira 仓库')


def AddArgError():
    print('致命错误: add 参数有误')
    print("'mira add <单个文件>'")


def NotFindFile(_file):
    print(f'致命错误: 文件 {_file} 不存在')
