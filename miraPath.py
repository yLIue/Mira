import os
import sys
from module import debug, Path

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

miraPath_path = base_path + os.sep

debug.setLocalPath(miraPath_path)
# debug.cleanDebug()

root = Path(debug.DebugPath())
etc = root / 'etc'
configIni = etc / 'config.ini'
