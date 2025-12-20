from module import debug
import repoPath


def Look(_args: list[str]):
    debug.log(f'调用Look函数,args: {_args}')
    _hash = _args[0]
    result = {}
    i = 0
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
