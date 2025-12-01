from module import debug, Error, getCommand, IniProcess


def Config(_args: list[str], _data: dict) -> None:
    debug.log(f'调用config函数,args: {_args}')

    _commands = _data['commands']
    _config = _data['config']
    _path = _data['directory']['etc']['configFile']

    if len(_args) == 0:
        Error.NoArgs()
    if len(_args) == 3:
        _command = getCommand(_args[0], _commands['long'])
        if _command is None:
            Error.NoFindCommand(_args[0], _commands['long'])
            return
        if _command == '--global':
            [_title, _key] = _args[1].split('.')
            _config[_title][_key] = _value = _args[2]

            IniProcess.save(_path, _config)

