ZMLIST = ["abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
def crypt(source):
    from itertools import cycle
    result = ''
    for ch in source:
        result = result + chr(ord(ch) ^ ord(next(temp)))
    return result