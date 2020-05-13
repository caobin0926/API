# 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
# 每个请求要求有请求参数
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# #请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码

import requests
from API_1.common.do_config import Config
from API_1.config import path
import json


class HttpRequests:
    def __init__(self):
        self.seesion = requests.session()

    def requests(self, method, url,header=None,data=None, json=None):
        cf=Config(path.environment_file)
        url=cf.get_str('test','ip')+url
        if method.lower() == 'get':
            resp = self.seesion.request(method, url ,headers=header,params=data)
        elif method.lower() == 'post':
            if json:
                resp = self.seesion.request(method, url, json=json)
            else:
                resp = self.seesion.request(method, url, data=data)
        return resp


if __name__ == '__main__':
    url = '/labelInfo/hotLabel'
    datas = {"current":1,"size":30}
    headr={'Content-Type':'application/json'}
    req=HttpRequests()
    resp=req.requests('get',url,header=headr,data=datas)
    print(resp.url)
    print(resp.text)
    print([i["id"] for i in json.loads(resp.text)["data"]["records"]])

