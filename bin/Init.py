import os
import subprocess
import shutil
import repoPath
import miraInfo
import miraPrint
from module import debug, IniFile


def Init(_args: list[str] = None) -> None:
    debug.log(f'调用Init函数,args: {_args}')
    try:
        initRepo()
        miraPrint.initRepo(repoPath.root / "")
    except FileExistsError:
        DestroyRepo()
        miraPrint.reInitRepo(repoPath.root / "")
        initRepo()


def DestroyRepo():
    shutil.rmtree(repoPath.root)
    debug.logOk('成功销毁仓库')


def initRepo():
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
