# -*- coding: utf-8 -*-

# @File:
# @Time :
# @Author :
# @Detail : 善行


from shanxingapi import *
import unittest
from shanxingapi.testcase.Login import Login



try:
    conf.get("Master", "host")
except Exception as msg:
    log.error("请检查配置文件是否正确:%s" % msg)



class Consumer(unittest.TestCase):


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
        print(ret)
        try:
            # 把返回结果转换成json格式
            if ret.json()['code'] == 0:
                self.login_random = ret.json()['data']['login_random']
                print(' self.login_random:' + self.login_random)
                self.code= ret.json()['code']
                log.info("success")
                return ret.json()

            else:
                log.warning("warning，response：{}".format(ret.json()))
                # log.warning("warning，response：%s" % ret.json())
                return False


        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False


    def login_Master(self,phone):
        """法师登录接口"""
        fs_url=self.host+conf.get('Master','login_Master')
        print('fs_url:'+fs_url)

        # 接口参数
        # 获取login_random
        login_random=self.login_random
        print("login_random:" + self.login_random)
        data = json.dumps({"phone": phone, "login_random": login_random})
        print('data:'+data)
        try:
            # 对接口发送请求
            ret = requests.post(url=fs_url, data=data)
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


    @property
    def Master_list(self):
        # 获取礼物列表接口
        self.host = conf.get("Master", "host")
        url = self.host + conf.get("Master", "Gift_list")
        print(url)
        self.token=Login().fs_login()
        self.headers={"authorization": "Bearer " + self.token}

        try:
            # 对礼物列表接口发送请求
            ret = requests.get(url=url,headers=self.headers)
            print(ret.text)
            if ret.json()["code"] == 0:
                log.info("success")
                log.info(ret)
                return ret.json()
            else:
                log.warning("warning，response：%s" % ret.json())
                return False

        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False


















