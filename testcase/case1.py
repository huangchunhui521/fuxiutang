# -*- coding: utf-8 -*-


from lib.ApiRequest import ApiRequest
from lib import getData
import json
from lib.Operate_Excel import *
from lib.CompareStr import *

get_data=getData.getData()
read_xls = Operate_Execl()
ir1=ApiRequest()
# CompareStr=Comparni zeStr()
for i in range(1,get_data.get_case_nums()):
    print("获取是否运行key: ",get_data.get_is_run(i))
    print("获取接口url:",get_data.get_url(i))
    print("获取接口请求方法：",get_data.get_method(i))
    print("获取接口请求数据：",get_data.get_data(i))
    print("获取接口请求数据：",get_data.get_data(i))
    print("获取i：", i)

    url=get_data.get_url(i)
    print("url:"+url)
    method=get_data.get_method(i)
    print("method11:"+method)
    data=json.loads(get_data.get_data(i))
    print("data11:"+str(data))
    result=ir1.run_method(url=url,method=method,data=data)
    print(result)
    # 把返回的结果写入到excel
    result_str = json.dumps(result,ensure_ascii=False,indent=4,sort_keys=True,separators=(',',':'))
    print("写入excel表单元格(2,2)的值:",read_xls.write_to_excel(i,i+7,result_str))

    assert_info = get_data.get_excepted_result(i)
   # 预期结果
    EXPECTED_RESULT = assert_info['code']
   #  EXPECTED_RESULT=str(read_xls.get_sheet_cell(i,i+6))
    # print('EXPECTED_RESULT:'+EXPECTED_RESULT)
    # 实际结果
    ACTUAL_RESULT = result['code']
    # ACTUAL_RESULT=str(read_xls.get_sheet_cell(i,i+7))
    # print('ACTUAL_RESULT:'+ACTUAL_RESULT)
    # 对比预期结果和实际结果是否一致
    assert_result = CompareStr.is_contains(EXPECTED_RESULT,ACTUAL_RESULT)
    print(f'断言结果为：{assert_result}')

a = '''{
  "code":0
}'''

b = '''{
    "code":0,
    "data":{
        "list":[
            {
                "abbot":"开心",
                "address":"广东省深圳市南山区科技南一路",
                "area_id":2166,
                "banners":"18788",
                "certificate":14375,
                "city_id":2162,
                "content":"深圳弘法寺弘法寺，位于广东省深圳市仙湖植物园内，始建于1983年寺院建筑面积达三万多平方米，殿、堂、寮、...",
                "created_at":"2019-11-26 09:48:21",
                "description":"<section style=\"font-size: 16px;\" data-role=\"outer\">\n<section class=\"_135editor\" data-tools=\"135编辑器\" data-id=\"94656\">\n<section style=\"border-bottom: 3px solid #db2c38; margin: 10px auto; box-sizing: border-box;\">\n<section style=\"margin-left: 1em; display: inline-block; padding: 4px 1em; border-top-left-radius: 10px; letter-spacing: 1.5px; font-weight: bold; border-top-right-radius: 10px; background-image: -webkit-linear-gradient(top, #e24e4e, #db2c38); color: #db2c38; box-sizing: border-box;\">\n<section class=\"135brush\" style=\"box-sizing: border-box; color: #fff;\" data-brushtype=\"text\">深圳弘法寺</section>\n</section>\n</section>\n</section>\n<section class=\"_135editor\" data-tools=\"135编辑器\" data-id=\"95198\">\n<section style=\"width: 100%; margin: 10px auto;\" data-width=\"100%\">\n<section class=\"assistant\" style=\"display: flex; justify-content: center; align-items: center;\">\n<section style=\"width: 100%; border-top: 1px solid #333333; box-sizing: border-box;\" data-width=\"100%\"></section>\n<section style=\"width: 6em; background: #fefefe; vertical-align: middle; margin: 0px auto; height: 20px; transform: rotate(0deg); -webkit-transform: rotate(0deg); -moz-transform: rotate(0deg); -ms-transform: rotate(0deg); -o-transform: rotate(0deg);\">\n<section style=\"width: 6em;\"><img class=\"assistant\" style=\"width: 6em; display: block;\" src=\"https://image2.135editor.com/cache/remote/aHR0cHM6Ly9tbWJpei5xbG9nby5jbi9tbWJpel9naWYvN1FSVHZrSzJxQzVOeG9hc3FZb1ZrVndUOU5hcEdPTU9hdUdNc1M2MXBvTVo2VjdVcmliMHFhaExZTGVEbmlhd3psMzFVbDZJazVEcTh6RnhSMkNvbzl2dy8wP3d4X2ZtdD1naWY=\" data-ishape=\"h-rect\" data-ipos=\"center-top\" data-ratio=\"1\" /></section>\n</section>\n<section style=\"width: 100%; border-top: 1px solid #333333; box-sizing: border-box;\" data-width=\"100%\"></section>\n</section>\n<section class=\"135brush\" style=\"font-size: 14px; text-align: center; letter-spacing: 1.5px; line-height: 1.75em; color: #3e3e3e; padding: 1em; box-sizing: border-box;\" data-autoskip=\"1\">\n<p><span style=\"color: #333333; text-indent: 28px; font-family: arial, 宋体, sans-serif;\">弘法寺，位于广东省深圳市</span><a style=\"color: #136ec2; text-decoration-line: none; text-indent: 28px; font-family: arial, 宋体, sans-serif;\" href=\"https://baike.baidu.com/item/%E4%BB%99%E6%B9%96%E6%A4%8D%E7%89%A9%E5%9B%AD/483462\" target=\"_blank\" rel=\"noopener\" data-lemmaid=\"483462\">仙湖植物园</a><span style=\"color: #333333; text-indent: 28px; font-family: arial, 宋体, sans-serif;\">内，始建于1983年</span></p>\n<p><span style=\"color: #333333; text-indent: 28px; font-family: arial, 宋体, sans-serif;\">寺院建筑面积达三万多平方米，殿、堂、寮、房、楼、阁共四十余处。</span></p>\n<p><span style=\"color: #333333; text-indent: 28px; font-family: arial, 宋体, sans-serif;\">弘法寺是1949年建国后，国内兴建的首座寺院。弘法寺由于地处中国改革开放的前沿陈地深圳，毗邻港澳，面向东南亚，因此，赵朴初及中国佛协其他领导寄予了深切的厚望：把弘法寺办成中国一流的佛教文化寺院，使之成为同海外佛教界联谊的纽带。</span></p>\n</section>\n<section class=\"assistant\" style=\"width: 100%; border-top: 1px solid #333333; box-sizing: border-box;\" data-width=\"100%\"></section>\n</section>\n</section>\n</section>",
                "id":61,
                "latitude":"22.543041",
                "logo":16508,
                "longitude":"113.949335",
                "name":"因陀罗",
                "province_id":2135,
                "status":1,
                "storage":14363,
                "updated_at":"2020-06-04 18:29:01",
                "user_id":1
            }
        ],
        "login_random":"cHgtI3FZ5qfGAE9O"
    },
    "message":"操作成功"
}'''

print(a in b)







