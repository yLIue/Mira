from module import debug, Error, IniFile
import miraPath


def Config(_args: list[str]) -> None:
    debug.log(f'调用config函数,args: {_args}')

    if len(_args) != 3 or _args[0] != '--global':
        Error.ConfigArgError()
        return
    _configIni = IniFile(miraPath.configIni)
    _dict = _configIni.load()
    [_title, _key] = _args[1].split('.')
    try:
        _dict[_title][_key]
    except KeyError:
        print('没查到此配置文件')
        return
    _dict[_title][_key] = _value = _args[2]
    _configIni.save(_dict)
