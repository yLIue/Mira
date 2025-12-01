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
