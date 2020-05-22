# -*- coding: utf-8 -*-

# @File:
# @Time :
# @Author :
# @Detail : 善行


from shanxingapi import *
import unittest
from shanxingapi.testFile import Token

try:
    conf.get("Master", "host")
except Exception as msg:
    log.error("请检查配置文件是否正确:%s" % msg)



class Consumer(unittest.TestCase):
    def Basic(self):
        self.host = None
        self.userId = None
        self.cookies = None
        # self.token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWYiOjE1ODc1NTEyNDgsIlRlbXBsZVVzZXIiOnsiaWQiOjI1OCwidXNlcl9pZCI6NTMzLCJ0ZW1wbGVfaWQiOjYxLCJjcmVhdGVkX2F0IjoiMjAxOS0xMS0yNiAxMToxNToyOCIsInVwZGF0ZWRfYXQiOiIyMDE5LTEyLTI3IDE3OjA0OjM3IiwidXBkYXRlX3VzZXJfbmFtZSI6MSwidXBkYXRlX2F2YXRhciI6MSwibmlja19uYW1lIjoi6YeK5byA5ouJIiwicGFzc3dvcmQiOiIkMnkkMTAkQTJjRjEvdXp3MVAwUG9VblpzaEtZdWJUbmRBVWZqUDZERy55c1RUbnhkR1dxazkwYTlvYzYiLCJhdmF0YXIiOiIvZ3JvdXAxL2RlZmF1bHQvMjAxOTEyMjcvMTcvMDQvMC8wMWNhOTE1NTU4OGM5MWI2MzYwOTMyN2I3ZTJmMDFlZC5qcGciLCJiaW8iOiLmnKzmnaXml6DkuIDnianvvIzkuIDliIfnmobpmo_nvJheXyIsImlzX21hc3RlciI6dHJ1ZSwiaXNfaG9zdCI6dHJ1ZSwibWFzdGVyX25hbWUiOiLms5XluIgxMDAifSwibG9naW5fdHlwZSI6IiIsImF1ZCI6IkFueSIsImV4cCI6MTU4NTg4ODA0OCwianRpIjoiNGQ5NzczYmYtNmNmYS00Yjg4LWJkYWEtNWNlODA2ZDFlMzZhIiwiaWF0IjoxNTg1MTMyMDQ4LCJpc3MiOiJTWE9TIiwibmJmIjoxNTg1MTMyMDQ4fQ._YKX3a5wy_fCINcDWC4UDzCf5mYUtNCxNc4uWF-31W0'
        self.headers_get = {"authorization": "Bearer " + self.token}
        self.headers = {'Content-Type': 'application/json'}
        self.token=Token.Token.login_random()



    def grant_authorization(self, phone, code):
        # 法师登录验证码授权
        self.host = conf.get("Master", "host")
        url = self.host + conf.get("Master", "grant_authorization")
        print('url:' + url)
        # 接口参数
        data = json.dumps({"phone": phone, "verifiable_code": code})
        print('data:' + data)
        # 对接口发送请求
        ret = requests.post(url=url, data=data)
        try:
            # 把返回结果转换成json格式
            if ret.json()['code'] == 0:
                self.login_random = ret.json()['data']['login_random']
                print(' self.login_random:' + self.login_random)
                self.code= ret.json()['code']
                # print(' self.code:' + self.code)
                log.info("success")
                # return self.code,self.login_random
                return ret.json()

            else:
                log.warning("warning，response：{}".format(self.ret.json()))
                # log.warning("warning，response：%s" % self.ret.json())
                return False


        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False



    def login_Master(self,phone):
        """法师登录接口"""
        fs_url=self.host+conf.get('Master','login_Master')
        print('fs_url:'+fs_url)
        print("login_random:" + self.login_random)
        # 接口参数
        # 获取login_random
        login_random=self.login_random
        data = json.dumps({"phone": phone, "login_random": login_random})
        print('data:'+data)
        try:
            # 对接口发送请求
            # ret = requests.post(url=fs_url, data=data)
            ret = requests.post(url=fs_url, data=data)
            # 把返回结果转换成json格式
            ret_json = ret.json()
            print(ret)
            if ret.json()["code"]==0:
                self.token=ret.json()['data']['token']
                print('self.token:'+self.token)
                log.info("success")
                return ret.json()
            else:
                log.warning("warning，response：%s" % self.ret.json())
                return False

        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False


    def Master_list(self):
        # 获取礼物列表接口
        self.host = conf.get("Master", "host")
        url = self.host + conf.get("Master", "Gift_list")
        print(url)
        try:
            # 对礼物列表接口发送请求
            ret = requests.get(url=url)
            print(ret.text)
            # 把返回结果转换成json格式
            ret_json = ret.json()

            if ret_json["code"] == 0:
                log.info("success")
                log.info(ret)
                return ret_json
            else:
                log.warning("warning，response：%s" % self.ret_json)
                return False

        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False


    # def ret(self):
    #     return self.code
















