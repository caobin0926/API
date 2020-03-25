import pytest
import allure
from API_1.common.httprequests import HttpRequests
from API_1.common.do_logs import Logs
from API_1.common.do_excel import DoExcel
from API_1.config import path
import json
class TestRegister:
    """测试注册接口类"""
    ex=DoExcel(path.case_file,'register')
    data=ex.get_cass()
    def setup_class(self):
        self.request=HttpRequests()
        self.logs=Logs('register')
        self.logs.loggers('INFO','----------开始执行测试用例---------')
    @allure.feature('注册接口')
    @allure.suite('注册接口测试用例')
    @pytest.mark.parametrize('case',data)
    def test_register(self,case):
        allure.attach('请求参数：{}'.format(case.data))
        self.logs.loggers('INFO', '请求方式:{};请求地址:{};请求参数:{}'.format(case.method, case.url, case.data))
        resp=self.request.requests(case.method,case.url,data=eval(case.data))
        case.actual=json.loads(resp.text)
        allure.attach('响应参数:{}'.format(case.actual))
        self.logs.loggers('INFO','响应参数：{}'.format(case.actual))
        try:
            assert eval(case.expected)==case.actual
            case.result='PASS'
        except AssertionError as e:
            case.result='FAIL'
            self.logs.loggers('error', '错误原因:{}'.format(e))
            raise e
        finally:
            allure.attach('测试结果：{}'.format(case.result))
            self.logs.loggers('INFO','断言结果:{}'.format(case.result))
            TestRegister.ex.write_excel(int(case.case_id)+1,str(case.actual),case.result)




