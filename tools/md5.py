import hashlib


# 封装md5加密函数
def generate_md5(data):

    hl = hashlib.md5()
    hl.update(data.encode(encoding="utf-8"))

    return hl.hexdigest()