import os
import subprocess
import shutil
import repoPath
import miraInfo
from module import debug, IniFile


def Init(_args: list[str]) -> None:
    debug.log(f'调用Init函数,args: {_args}')
    try:
        os.mkdir(repoPath.root)
        subprocess.run(f'attrib +h "{repoPath.root}"', shell=True, check=True)
        os.mkdir(repoPath.objects)
        os.mkdir(repoPath.logs)
        IniFile(repoPath.config).save({
            'info': {
                'version': miraInfo.version
            }
        })
        debug.logOk('.mira文件初始化成功')
        print(f'已初始化空的mira仓库,路径: {repoPath.root / ""}')
    except FileExistsError:
        debug.log()
        debug.logError('.mira文件初始化失败,文件存在')
        debug.log()


def DestroyRepo():
    try:
        shutil.rmtree(repoPath.root)
        debug.logOk('成功销毁仓库')
    except FileNotFoundError:
        pass
