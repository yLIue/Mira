def initRepo(_repoPath: str):
    print(f'已初始化空的Mira仓库,路径: {_repoPath}')


def reInitRepo(_repoPath: str):
    print(f'已经重新初始化Mira仓库,路径: {_repoPath}')


def noCommand():
    print('以下是在各种情况下常用的Mira命令\n')
    print('更改你的配置文件')
    printCommand('config', '修改Mira的配置文件')
    print('\n创建一个工作区')
    printCommand('init', 'init一个空的Mira仓库或重新初始化')
    print('\n针对当前的变更进行工作')
    printCommand('add', '将文件内容添加到缓冲区内')
    print('\n检查历史和状态')
    printCommand('log', '显示提交日志')
    printCommand('status', '显示工作区的文件状态')
    printCommand('look', '显示哈希的内容(未测试)')
    print('\n提交或更改你的记录')
    printCommand('commit', '提交记录更改到仓库')
    printCommand('reset', '重置当前指向的记录')
    print('\n从提交中映射你的文件')
    printCommand('map', '查看当前的映射关系')
    printInCommand('status', '显示提交中的文件状态')
    printInCommand('add', '将提交的内容添加映射关系')
    printInCommand('push', '推送映射文件到指定目录')


def printCommand(_command, _msg):
    print(f'\t{_command:12}{_msg}')


def printInCommand(_command, _msg):
    print(f'\t-\t{_command:12}{_msg}')
