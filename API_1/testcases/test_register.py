import pytest
import allure
from API_1.common.httprequests import HttpRequests
from API_1.common.do_logs import Logs
from API_1.common.do_excel import DoExcel
from API_1.config import path
from API_1.common.do_re import replace
import json
class TestRegister:
    """测试注册接口类"""
    ex = DoExcel(path.case_file, 'register')
    case = ex.get_cass()

    def setup_class(self):
        self.http = HttpRequests()
        self.ex = DoExcel(path.case_file, 'register')
        self.loger = Logs('logger')
        self.loger.loggers('INFO', '-------------开始执行测试用例------------')

    @allure.story('测试场景')
    @allure.suite('注册测试用例')
    @pytest.mark.parametrize('cases', case)
    def test_login(self, cases):
        # global loger
        allure.attach('请求参数：{}'.format(cases.data))
        self.loger.loggers('INFO', '请求方式:{};请求地址:{};请求参数:{}'.format(cases.method, cases.url, cases.data))
        cases.data=replace(cases.data)
        resp = self.http.requests(cases.method, url=cases.url, data=eval(cases.data))
        allure.attach('期望结果:{}'.format(cases.expected))
        allure.attach('响应结果:{}'.format(resp.text))
        cases.actual = json.loads(resp.text)
        self.loger.loggers('INFO', '响应报文:{}'.format(cases.actual))
        try:
            assert (eval(cases.expected) == cases.actual)
            cases.result = 'PASS'
        except AssertionError as e:
            cases.result = 'FAIL'
            self.loger.loggers('ERROR', '报错原因:{}'.format(e))
            raise e
        finally:
            allure.attach('测试结果:{}'.format(cases.result))
            # ex = DoExcel(path.case_file, 'login')
            self.ex.write_excel(int(cases.case_id) + 1, str(cases.actual), cases.result)
            self.loger.loggers('INFO', '测试结果:{}'.format(cases.result))

    def teardown_class(self):
        self.http.seesion.close()
        self.loger.loggers('INFO', '------------登录测试用例全部完成----------')




