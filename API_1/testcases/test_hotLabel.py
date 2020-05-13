from API_1.common.httprequests import HttpRequests
from API_1.common.do_logs import Logs
from API_1.common.do_excel import DoExcel
from API_1.config import path
import pytest
import json
import time


class Testhotlabel:
    """
    测试热门标签类
    """
    excel = DoExcel(path.case_file, 'hotLabel')
    hotlabel_case = excel.get_cass()

    def setup_class(self):
        self.req = HttpRequests()
        self.loggers = Logs('loggers')
        self.loggers.loggers('INFO', '----------开始执行热门标签测试用例----------')
    @pytest.mark.parametrize('case',hotlabel_case)
    def test_hotlabel(self,case):
        """
        测试热门标签接口方法
        """
        self.loggers.loggers('INFO','用例编号：{},请求接口地址：{},请求参数：{}'.format(case.case_id,case.url,case.data))
        resp=self.req.requests(case.method,case.url,header=eval(case.headers),data=json.loads(case.data))
        self.loggers.loggers('INFO','响应结果：{}'.format(resp.text))
        resp_actual=json.loads(resp.text)
        # print(resp_actual)
        if int(case.case_id) in range(1,4):
            case.actual={"code":resp_actual['code'],"records":[i["id"] for i in json.loads(resp.text)["data"]["records"]]}
            self.loggers.loggers('INFO','实际结果：{}'.format(case.actual))
            print(case.actual)
            try:
                print(json.loads(case.expected))
                assert json.loads(case.expected)==case.actual
                result='PASS'
                self.loggers.loggers('INFO','测试通过：{}'.format(result))
            except AssertionError as e:
                result='FAIL'
                self.loggers.loggers('ERROR','测试不通过：{},原因：{}'.format(result,e))
                raise e
            finally:
                ex = DoExcel(path.case_file, 'hotLabel')
                ex.write_excel(int(case.case_id)+1,str(json.dumps(case.actual)),result)
                # time.sleep(3)
        else:
            try:
                assert json.loads(case.expected)==json.loads(resp.text)
                result = 'PASS'
                self.loggers.loggers('INFO', '测试通过：{}'.format(result))
            except AssertionError as e:
                result = 'FAIL'
                self.loggers.loggers('ERROR', '测试不通过：{},原因：{}'.format(result, e))
                raise e
            finally:
                case.actual=resp.text
                ex = DoExcel(path.case_file, 'hotLabel')
                ex.write_excel(int(case.case_id) + 1, case.actual, result)
    def teardown_class(self):
        self.req.seesion.close()
        self.loggers.loggers('INFO', '----------热门标签测试用例全部执行完成----------')



