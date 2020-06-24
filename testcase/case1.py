# -*- coding: utf-8 -*-

<<<<<<< HEAD

from lib.ApiRequest import ApiRequest
from lib import getData
import json


get_data=getData.getData()
for i in range(1,get_data.get_case_nums()):
    print("获取是否运行key: ",get_data.get_is_run(i))
    print("获取接口url:",get_data.get_url(i))
    print("获取接口请求方法：",get_data.get_method(i))
    print("获取接口请求数据：",get_data.get_data(i))
    url=get_data.get_url(i)
    # print("url12:"+ur12)
    method=get_data.get_method(i)
    # print("method:"+method)
    data=json.loads(get_data.get_data(i))
    # print("data:"+str(data))
    ir2=ApiRequest()
    result=ir2.run_method(url=url,method=method,data=data)
    print(result)
=======
import json,unittest
from lib import TestCaseKeyWord
from lib.ApiRequest import ApiRequest
from lib import getData


class Case1(unittest.TestCase):
    """客户端api"""

    def setUp(self):
        send_requests=ApiRequest()

    def tearDown(self):
        pass

    def test_api(self):



        # get_excel = Operate_Execl()
        # # 获取用例数
        # print(get_excel.get_sheet_nrows()-1)
        # # 返回用例名称关键字的列值
        # case_name_col = int(TestCaseKeyWord.get_case_name())
        # print(case_name_col)
        # # 获取第一条用例的名称
        # get_name = get_excel.get_sheet_cell(1,case_name_col)
        # print(get_name)


        get_data=getData.getData()
        print("获取是否运行key: ",get_data.get_is_run(1))
        print("获取接口url:",get_data.get_url(1))
        print("获取接口请求方法：",get_data.get_method(1))
        print("获取接口请求数据：",get_data.get_data(1))
        ur12=get_data.get_url(1)
        print("url12:"+ur12)
        method=get_data.get_method(1)
        print("method:"+method)
        data=get_data.get_data(1)
        print("data:"+data)
        ir2=ApiRequest()
        result=ir2.run_method(url=ur12,method=method,data=data)
        print(result)
>>>>>>> 170b4f31c5f7ffce26f3115967da5be2068d8fc1
