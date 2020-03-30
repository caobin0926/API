from API_1.common.httprequests import HttpRequests
import json
from API_1.common.do_excel import *
from API_1.config import path
from API_1.common.do_logs import Logs
import pytest
import allure
import yaml
@allure.feature('登录接口')
class TestLogin:
    """测试登录接口"""
    # ex = DoExcel(path.case_file, 'login')
    # case = ex.get_cass()
    with open(path.login_yml,encoding='utf-8') as f:
        case=yaml.load(f,Loader=yaml.FullLoader)
    def setup_class(self):
        self.http=HttpRequests()
        # self.ex = DoExcel(path.case_file, 'login')
        self.loger = Logs('logger')
        self.loger.loggers('INFO','-------------开始登录执行测试用例------------')

    @allure.story('测试场景')
    @allure.suite('API接口测试用例')
    @pytest.mark.parametrize('cases',case)
    def test_login(self,cases):
        # global loger
        allure.attach('请求参数：{}'.format(cases['data']))
        self.loger.loggers('INFO','请求方式:{};请求地址:{};请求参数:{}'.format(cases['method'],cases['url'],cases['data']))
        resp=self.http.requests(cases['method'],url=cases['url'],data=cases['data'])
        allure.attach('期望结果:{}'.format(str(cases['expected'])))
        allure.attach('响应结果:{}'.format(resp.text))
        # cases.actual=json.loads(resp.text)
        self.loger.loggers('INFO','响应报文:{}'.format(json.loads(resp.text)))
        try:
            # assert (eval(cases.expected)==cases.actual)
            assert cases['expected']==json.loads(resp.text)
            # cases['result']='PASS'
            result='PASS'
        except AssertionError as e:
            result='FAIL'
            self.loger.loggers('ERROR','报错原因:{}'.format(e))
            raise e
        finally:
            allure.attach('测试结果:{}'.format(result))
            # ex = DoExcel(path.case_file, 'login')
            # self.ex.write_excel(int(cases.case_id)+1,str(cases.actual),cases.result)
            self.loger.loggers('INFO', '测试结果:{}'.format(result))
    def teardown_class(self):
        self.http.seesion.close()
        self.loger.loggers('INFO','------------登录测试用例全部完成----------')




