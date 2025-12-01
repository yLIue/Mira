from .Debug import debug


def NoArgs():
    _func = debug.getFunc(1)
    debug.log()
    debug.logError('没有任何指令',_func)
    debug.log()
    print()
    print('没有任何参数')
