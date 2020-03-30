import pytest
import allure
from API_1.common.httprequests import HttpRequests
from API_1.common.do_logs import Logs
from API_1.common.do_excel import DoExcel
from API_1.config import path
from API_1.common.do_re import replace
import json
import yaml
@allure.feature('注册接口')
class TestRegister:
    """测试注册接口类"""
    with open(path.register_yml,encoding='utf-8') as f:
        case=yaml.load(f,Loader=yaml.FullLoader)
        # print(case)
    def setup_class(self):
        self.http = HttpRequests()
        # self.ex = DoExcel(path.case_file, 'register')
        self.loger = Logs('logger')
        self.loger.loggers('INFO', '-------------开始执行注册测试用例------------')

    @allure.story('')
    @allure.suite('API接口测试用例')
    # @allure.title("{cases['title']}")
    @allure.step('请求参数：{}')
    @pytest.mark.parametrize('cases', case)
    # @allure.title("{cases[title]}")
    def test_login(self, cases):
        allure.attach('请求参数：{}'.format(cases['data']))
        datas=replace(str(cases['data']))
        self.loger.loggers('INFO', '请求方式:{};请求地址:{};请求参数:{}'.format(cases['method'], cases['url'], cases['data']))
        # cases.data=replace(cases['data'])
        resp = self.http.requests(cases['method'], url=cases['url'], data=datas)
        allure.attach('期望结果:{}'.format(str(cases['expected'])))
        allure.attach('响应结果:{}'.format(resp.text))
        self.loger.loggers('INFO', '期望结果:{}'.format(cases['expected']))
        self.loger.loggers('INFO', '实际结果:{}'.format(json.loads(resp.text)))
        try:
            assert (cases['expected']) == json.loads(resp.text)
            result = 'PASS'
        except AssertionError as e:
            result = 'FAIL'
            self.loger.loggers('ERROR', '报错原因:{}'.format(e))
            raise e
        finally:
            allure.attach('测试结果:{}'.format(result))
            # ex = DoExcel(path.case_file, 'login')
            # self.ex.write_excel(int(cases.case_id) + 1, str(cases.actual), cases.result)
            self.loger.loggers('INFO', '测试结果:{}'.format(result))

    def teardown_class(self):
        self.http.seesion.close()
        self.loger.loggers('INFO', '------------注册测试用例全部完成----------')




