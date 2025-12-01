from module import debug, Error, getCommand, IniProcess


def Init(_args: list[str], _data: dict) -> None:
    debug.log(f'调用config函数,args: {_args}')
