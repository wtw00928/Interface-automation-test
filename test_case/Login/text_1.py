
import allure
import pytest
from utils.read_files_tools.get_yaml_data_analysis import GetTestCase
from utils.assertion.assert_control import Assert
from utils.requests_tool.request_control import RequestControl
from utils.read_files_tools.regular_control import regular
from utils.requests_tool.teardown_control import TearDownHandler

if __name__ == '__main__':
    in_data = {'url': 'https://www.wanandroid.com/user/login',
               'method': 'POST',
               'detail': '正常登录',
               'assert_data': {'errorCode': {'jsonpath': '$.errorCode', 'type': '==', 'value': 0, 'AssertType': None},
                               'username': {'jsonpath': '$.data.username', 'type': '==', 'value': '1418668133',
                                            'AssertType': None}},
               'headers': None,
               'requestType': 'DATA',
               'is_run': None,
               'data': {'username': '1418668133', 'password': '13275099793'},
               'dependence_case': False,
               'dependence_case_data': None,
               'sql': None, 'setup_sql': None,
               'status_code': None,
               'teardown_sql': None,
               'teardown': None,
               'current_request_set_cache': None,
               'sleep': None}
    res = RequestControl(in_data).http_request()
    TearDownHandler(res).teardown_handle()
    Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                   sql_data=res.sql_data, status_code=res.status_code)