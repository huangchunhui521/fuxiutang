# -*- coding: utf-8 -*-

# @File:
# @Time :
# @Author :
# @Detail : 善行

import requests
import json

class ApiRequest(object):
    """
    请求方法
    """

    # 请求方法get
    def get_method(self,url,data=None,header=None):

        if header is not None:
            res=requests.get(url,params=data,headers=header)
        else:
            res=requests.get(url,params=data)
        return res.json()

    #请求方法post
    def post_method(self,url,data=None,hearder=None):
        if hearder is not None:
            res=requests.post(url,json=data,heards=hearder)
        else:
            res = requests.post(url, json=data,)

        if str(res)=="<Response [200]>":
            return res.json()
        else:
            return res.text

    #请求方法put
    def put_method(self,url,data=None,hearder=None):
        if hearder is not None:
            res=requests.put(url,params=data,headers=hearder)
        else:
            res=requests.put(url,params=data)
        return res.json()

    # 请求方法delete
    def delete_method(self,url,data=None,hearder=None):
        if hearder is not None:
            res=requests.delete(url,params=data,headers=hearder)
        else:
            res=requests.delete(url,params=data)
        return res.json()


    # 主方法
    def run_method(self,method,url,data=None,hearder=None):
        if method=='get' or method=='GET':
            res=self.get_method(url,data,hearder)
        elif method=='post' or method=='POST':
            res=self.post_method(url,data,hearder)
        elif method=='put' or method=='PUT':
            res=self.put_method(url,data,hearder)
        elif method=='delete' or method=='DELETE':
            res=self.delete_method(url,data,hearder)
        else:
            res="你的请求方式不对!"
        return json.dumps(res,ensure_ascii=False,indent=4,sort_keys=True,separators=(',',':'))


    # ensure_ascii：默认值True，如果dict内含有non - ASCII的字符，则会类似\uXXXX的显示数据，设置成False后，就能正常显示。
    #
    # indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，否则会换行且按照indent的数量显示前面的空白，这样打印出来的json数据也叫pretty - printed
    # json。
    #
    # separators：分隔符，实际上是(item_separator, dict_separator)
    # 的一个元组，默认的就是(‘, ’, ’:’)；这表示dictionary内keys之间用“, ”隔开，而KEY和value之间用“：”隔开。
    #
    # encoding：默认是UTF - 8，设置json数据的编码方式。
    #
    # sort_keys：将数据根据keys的值进行排序。



if __name__ == '__main__':
    url = "http://httpbin.org/get"
    ir = ApiRequest()
    result = ir.run_method(url=url,method='get')
    print(result)


    url2="http://httpbin.org/post"
    ir2=ApiRequest()
    data={'id':'测试'}
    result=ir2.run_method(url=url2,method='post',data=data)
    print(result)