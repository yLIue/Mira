import os


def getPath(_type: str) -> dict | None:
    if _type == 'repo':
        return getRepoStructure()
    return None


def getMiraStructure() -> dict:
    pass


def getRepoStructure() -> dict:
    _path = f'{os.getcwd()}\\.mira\\'

    _logsDirectory = f'{_path}logs'
    _commitFile = f'{_logsDirectory}\\commit'
    _reflogFile = f'{_logsDirectory}\\reflog'

    _stagingDirectory = f'{_path}staging'
    _stagingTable = f'{_stagingDirectory}\\staging.tabe'

    _objectsDirectory = f'{_path}objects'

    _configFile = f'{_path}config'
    _descriptionFile = f'{_path}description'
    _mapTable = f'{_path}map.table'

    _structure = {
        'logs': {
            'path': _logsDirectory,
            'commitFile': _commitFile,
            'reflogFile': _reflogFile
        },
        'staging': {
            'path': _stagingDirectory,
            'stagingTable': _stagingTable
        },
        'objects': {
            'path': _objectsDirectory
        },
        'configFile': _configFile,
        'descriptionFile': _descriptionFile,
        'mapTable': _mapTable
    }

    return _structure
