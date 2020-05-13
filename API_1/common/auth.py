import hashlib
import time


def token():
    pass


def signs(token=None, unionId=None):
    """
    函数功能是生成签名
    :param to_sign_str:
    :return:
    """

    token = ''
    timestamp = time.time()
    print(int(timestamp))
    unionId = 'F73FD58DFD30BDB55AA2601DF47DEF9A'
    # to_sign_str = "timestamp={}&token={}&unionId={}".format(timestamp, token, unionId)
    to_sign_str='timestamp=1562640039&token=tokenabc&unionId=3489877dsd'
    sign = hashlib.sha256(to_sign_str.encode('utf-8')).hexdigest().upper()
    return sign
a=signs()
print(a)
