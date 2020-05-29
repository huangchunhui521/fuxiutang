# -*- coding: utf-8 -*-

# @File:
# @Time :
# @Author :
# @Detail : 善行

class TestCaseKeyWord(object):
    """
    定义测试用例关键字
    """
    CASE_ID = '0'
    CASE_NAME = '1'
    IS_EXECUTE = '2'
    INTERFACE_URL = '3'
    METHOD = '4'
    HEADER = '5'
    REQUEST_DATA = '6'
    EXPECTED_RESULT = '7'
    ACTUAL_RESULT = '8'
    RESULT = '9'

# 获取用例id
def get_case_id():
    return TestCaseKeyWord.CASE_ID

# 获取用例名称
def get_case_name():
    return TestCaseKeyWord.CASE_NAME

# 用例是否执行
def get_case_is_excute():
    return TestCaseKeyWord.IS_EXECUTE

# 接口url
def get_case_interface_url():
    return TestCaseKeyWord.INTERFACE_URL

# 用例方法
def get_case_method():
    return TestCaseKeyWord.METHOD

# 请求头
def get_case_header():
    return TestCaseKeyWord.HEADER

# 请求参数
def get_case_payload():
    return TestCaseKeyWord.REQUEST_DATA

# 预期结果
def get_case_expected_result():
    return TestCaseKeyWord.EXPECTED_RESULT

# 实际结果
def get_case_actual_result():
    return TestCaseKeyWord.ACTUAL_RESULT

# 用例执行结果
def get_case_result():
    return TestCaseKeyWord.RESULT


if __name__ == '__main__':
    print(get_case_id())
    print(get_case_is_excute())



