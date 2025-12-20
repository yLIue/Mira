from module import debug, Path

miraPath_path = '\\'.join(__file__.split('\\')[:-1]) + '\\'
debug.setLocalPath(miraPath_path)
# debug.cleanDebug()

root = Path(debug.DebugPath())
etc = root / 'etc'
configIni = etc / 'config.ini'
