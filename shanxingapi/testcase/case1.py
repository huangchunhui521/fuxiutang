# -*- coding: utf-8 -*-
# @File:
# @Time :
# @Author :
# @Detail :


from shanxingapi import *
import unittest
from shanxingapi.testFile import fux_api



class case1(unittest.TestCase):

    __doc__ = "TestCase"

    _classSetupFailed = True

    _cookies = None

    _shop_id = None

    _user_id = None

    _log = None

    _consumer = None



    @classmethod
    def setUpClass(cls):
        cls.consumer_object =fux_api.Consumer()
        cls._log = fux_api.log
        cls._log.debug("=" * 20)
        cls._log.debug("开始测试")


    @classmethod
    def tearDownClass(cls):
        cls._log.debug("="*20)
        cls._log.debug("结束测试")



    def test_001(self):
        """法师登录验证码授权"""
        log.info('法师登录验证码授权')
        code=''
        aa= self.consumer_object.grant_authorization(phone='1581865080511',code='12345678')
        self.assertEqual(aa[code], 0)
        # self.assertEqual(code,0)








    # def test_002(self):
    #     """法师登录接口"""
    #     log.info('获取法师登录验证码授权')
    #     self.consumer_object.grant_authorization(phone='15818650805', code='123456')
    #     log.info('法师端登录')
    #     self.consumer_object.login_Master(phone='15818650805')



    # def test_003(self):
    #     """礼物列表"""
    #     self.ret = self.consumer_object.Master_list()
    #     self.assertEqual(self.ret["code"], 0)


if __name__ == '__main__':
    unittest.main()