# # -*- coding: utf-8 -*-
# # @File:
# # @Time :
# # @Author :
# # @Detail :
# import ddt as ddt
#
# from shanxingapi import *
# import unittest
# from shanxingapi.testFile import fux_api,Token
#
#
# class Login(unittest.TestCase):
#
#     __doc__ = "TestCase"
#
#     _classSetupFailed = True
#
#     _cookies = None
#
#     _shop_id = None
#
#     _user_id = None
#
#     _log = None
#
#     _consumer = None
#
#
#     @classmethod
#     def setUpClass(self):
#         self.host = None
#         self.userId = None
#         self.cookies = None
#         self.headers_get = {"authorization": "Bearer " + self.token}
#         self.headers = {'Content-Type': 'application/json'}
#         self.token = Token.Token.login_random()
#         # self.consumer_object =Token.Token()
#         self._log = fux_api.log
#         self._log.debug("=" * 20)
#         self._log.debug("开始测试")
#
#
#     @classmethod
#     def tearDownClass(self):
#         self._log.debug("="*20)
#         self._log.debug("结束测试")
#
#
#     def grant_authorization(self, phone, code):
#         # 法师登录验证码授权
#         self.host = conf.get("Master", "host")
#         url = self.host + conf.get("Master", "grant_authorization")
#         print('url:' + url)
#         # 接口参数
#         data = json.dumps({"phone": phone, "verifiable_code": code})
#         print('data:' + data)
#         try:
#             # 对接口发送请求
#             ret = requests.post(url=url, data=data)
#             # 把返回结果转换成json格式
#             self.ret_json = ret.json()
#             if ret.json()['code'] == 0:
#                 self.login_random = ret.json()['data']['login_random']
#                 print(' self.login_random:' + self.login_random)
#                 self.code= ret.json()['code']
#                 # print(' self.code:' + self.code)
#                 log.info("success")
#                 # return self.ret_json()
#                 # return self.code,self.login_random
#
#                  # 法师登录接口
#                 fs_url = self.host + conf.get('Master', 'login_Master')
#                 print('fs_url:' + fs_url)
#                 print("login_random:" + self.login_random)
#                 # 接口参数
#                 # 获取login_random
#                 # login_random = self.login_random
#                 data = json.dumps({"phone": phone, "login_random": self.login_random})
#                 print('data:' + data)
#                 try:
#                     # 对接口发送请求
#                     ret = requests.post(url=fs_url, data=data)
#                     # 把返回结果转换成json格式
#                     self.ret_json = ret.json()
#                     # 获取token
#                     self.token=self.ret_json
#                     print(ret)
#
#
#             else:
#                 log.warning("warning，response：{}".format(self.ret_json()))
#                 return False
#
#
#         except Exception as msgs:
#             log.error("error, %s" % msgs)
#             return False
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()