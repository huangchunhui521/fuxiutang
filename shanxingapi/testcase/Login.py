# -*- coding: utf-8 -*-
# @File:
# @Time :
# @Author :
# @Detail :
import ddt as ddt

from shanxingapi import *
import unittest


<<<<<<< HEAD
class Login(unittest.TestCase):
    host = conf.get("Master", "host")
=======

class Login(unittest.TestCase):


>>>>>>> b3ec293c15fb4fba64d8d00bed0910664a2390a9

    def grant_authorization(self):
        self.host = conf.get("Master", "host")
        # 法师登录验证码授权接口
        url = self.host + conf.get("Master", "grant_authorization")
        print('url:' + url)
        # 接口参数
        data = json.dumps({"phone": '15818650805', "verifiable_code": '123456'})
        print('data:' + data)
        # 对接口发送请求
        ret = requests.post(url=url, data=data)

        try:
            if ret.json()['code'] == 0:
                self.login_random = ret.json()['data']['login_random']
                print(' self.login_random:' + self.login_random)
                log.info("success")
                return self.login_random

            else:
                log.warning("warning，response：{}".format(ret.json()))
                return False

        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False


<<<<<<< HEAD
=======

>>>>>>> b3ec293c15fb4fba64d8d00bed0910664a2390a9
    def fs_login(self):
        # 法师登录接口
        fs_url = self.host + conf.get('Master', 'login_Master')
        print('fs_url:' + fs_url)
        # 接口参数
<<<<<<< HEAD
        login_random = self.grant_authorization()
=======
        login_random = self.login_random
>>>>>>> b3ec293c15fb4fba64d8d00bed0910664a2390a9
        data = json.dumps({"phone": '15818650805', "login_random": login_random})
        print('data:' + data)
        # 对接口发送请求
        ret = requests.post(url=fs_url, data=data)

        try:
            if ret.json()['code'] == 0:
                # 获取token
                self.token=ret.json()['data']['token']
                print('aaaa:'+self.token)
                return self.token

            else:
                log.warning("warning，response：{}".format(ret.json()))
                return False


        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False



<<<<<<< HEAD

=======
>>>>>>> b3ec293c15fb4fba64d8d00bed0910664a2390a9
if __name__ == '__main__':
    unittest.main()