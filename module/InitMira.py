import os
from .Debug import debug
from module import IniProcess

# global
LOCAL_PATH = ''
DIRECTORY_PATH = ''


def InitMira(_localPath: str) -> None:
    global LOCAL_PATH
    LOCAL_PATH = _localPath
    initDirectoryStructure()
    initConfig()
    initCommands()


def initDirectoryStructure() -> None:
    _ectDirectory = f'{LOCAL_PATH}etc'
    _configFile = f'{_ectDirectory}\\config.ini'
    _directoryFile = f'{_ectDirectory}\\directories.ini'
    _commandsFile = f'{_ectDirectory}\\commands.ini'

    global DIRECTORY_PATH
    DIRECTORY_PATH = _directoryFile
    _directoryStructure = {
        'etc': {
            'path': _ectDirectory,
            'configFile': _configFile,
            'directoryFile': _directoryFile,
            'commandsFile': _commandsFile
        }
    }
    os.mkdir(_ectDirectory)
    IniProcess.save(_directoryFile, _directoryStructure)


def initConfig() -> None:
    _directory = IniProcess.load(DIRECTORY_PATH)
    _config = {
        'info': {
            'version': '0.0.1'
        },
        'user': {
            'name': 'default',
            'email': 'default@mira.com'
        }
    }
    IniProcess.save(_directory['etc']['configFile'], _config)


def initCommands() -> None:
    _directory = IniProcess.load(DIRECTORY_PATH)
    _commands = {
        'config': {
            'long': ['--global']
        },
        'help': {}
    }
    IniProcess.save(_directory['etc']['commandsFile'], _commands)
