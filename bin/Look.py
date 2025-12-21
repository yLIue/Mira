from module import debug, isMira, Error
import repoPath


def Look(_args: list[str]):
    debug.log(f'调用Look函数,args: {_args}')
    if not isMira():
        return
    if len(_args) != 1:
        Error.LookArgError()
        return
    _hash = _args[0]
    result = {}
    i = 0
    try:
        with open(repoPath.objects / _hash[:2] / _hash[2:], 'rb') as f:
            data = f.read()
            while i < len(data):
                j = data.index(b'\0', i)
                header = data[i:j].decode()
                mode, name = header.split(' ', 1)

                sha_bytes = data[j + 1:j + 21]
                sha_hex = sha_bytes.hex()

                if mode == 'dir':
                    typ = 'tree'
                else:
                    typ = 'blob'
                result[name] = (typ, sha_hex)

                i = j + 21
            print(result)
    except FileNotFoundError:
        print(f'致命错误: 记录不存在')
