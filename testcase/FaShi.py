# -*- coding: utf-8 -*-


from lib.ApiRequest import ApiRequest
from lib import getData
import json
from lib.Operate_Excel import *



get_data=getData.getData()
read_xls = Operate_Execl()
ir1=ApiRequest()

def case1(self):
    for i in range(1,get_data.get_case_nums()):
        print("获取是否运行key: ",get_data.get_is_run(i))
        print("获取接口url:",get_data.get_url(i))
        print("获取接口请求方法：",get_data.get_method(i))
        print("获取接口请求数据：",get_data.get_data(i))
        print("获取用例数量：", i)

        url=get_data.get_url(i)
        print("url:"+url)
        method=get_data.get_method(i)
        print("method:"+method)
        data=json.loads(get_data.get_data(i))
        print("data:"+str(data))
        result=ir1.run_method(url=url,method=method,data=data)
        print(result)
        # 把返回的结果写入到excel
        result_str = json.dumps(result,ensure_ascii=False,indent=4,sort_keys=True,separators=(',',':'))
        # print("写入excel表单元格(i,8)的值:",read_xls.write_to_excel(i,8,result_str))


        # 预期结果
        EXPECTED_RESULT=json.dumps(get_data.get_excepted_result(i))

        # 实际结果
        ACTUAL_RESULT = result['code']

        # 对比预期结果和实际结果是否一致
        self.assertEqual(ACTUAL_RESULT['code'],EXPECTED_RESULT['code'])
        self.assertEqual(ACTUAL_RESULT['msg'], EXPECTED_RESULT['msg'])

        # # 对比预期结果和实际结果是否一致
        # assert_result = CompareStr().is_contains(EXPECTED_RESULT,ACTUAL_RESULT)
        # print(f'断言结果为：{assert_result}')









