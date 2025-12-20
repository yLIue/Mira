import os
from module import Path

workRoot = Path(os.getcwd())
root = workRoot / '.mira'
objects = root / 'objects'
logs = root / 'logs'
miraignore = {'.mira', '.log'}
config = root / 'config'
