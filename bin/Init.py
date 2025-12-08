import os, subprocess, shutil
from module import debug, Error, getCommand, IniProcess, getPath

# global
REPO_PATH = f'{os.getcwd()}\\.mira'


def Init(_args: list[str], _data: dict) -> None:
    debug.log(f'调用Init函数,args: {_args}')

    # 销毁仓库
    DestroyRepo()

    initRepoDirectory()


def initRepoDirectory() -> None:
    try:
        os.makedirs(REPO_PATH)
        subprocess.run(f'attrib +h "{REPO_PATH}"', shell=True, check=True)
        debug.logOk('.mira文件初始化成功')
        _path = getPath('repo')
        for _item in _path.keys():
            if not (_item.endswith('File') or _item.endswith('Table')):
                os.makedirs(_path[_item]['path'])
    except FileExistsError:
        debug.log()
        debug.logError('.mira文件初始化失败,文件存在')
        debug.log()






def DestroyRepo():
    try:
        shutil.rmtree(REPO_PATH)
        debug.logOk('成功销毁仓库')
    except FileNotFoundError:
        pass
