from module import debug


def getCommand(_command: str, _commands: list[str]) -> str | None:
    matcher = [_matcher for _matcher in _commands if _matcher.startswith(_command)]
    if len(matcher) == 0:
        debug.log()
        debug.logError(f'命令解析失败: 无法识别')
        debug.log(f'command: {_command}', 'OUTPUT')
        debug.log()

        print(f"无法识别的命令 '{_command}'")
        return None
    if len(matcher) > 1:

        debug.log()
        debug.logError(f'命令解析失败: 多个命令')
        debug.log(f'command: {_command}', 'OUTPUT')
        debug.log(f'matcher: {matcher}', 'OUTPUT')
        debug.log()

        print('命令存在多个,您可能想输入:')
        for i in matcher:
            print(i)
        return None
    debug.log()
    debug.logOk(f'命令解析成功 command: {matcher[0]}')
    debug.log()
    return matcher[0]
