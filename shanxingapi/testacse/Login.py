# -*- coding: utf-8 -*-
# @File:
# @Time :
# @Author :
# @Detail :
import ddt as ddt

from shanxingapi import *
import unittest
from shanxingapi.testFile import fux_api,Token


class ConsumerTestCase(unittest.TestCase):

    __doc__ = "TestCase"

    _classSetupFailed = True

    _cookies = None

    _shop_id = None

    _user_id = None

    _log = None

    _consumer = None


    @classmethod
    def setUpClass(cls):
        cls.consumer_object =Token.Token()
        cls._log = fux_api.log
        cls._log.debug("=" * 20)
        cls._log.debug("开始测试")


    @classmethod
    def tearDownClass(cls):
        cls._log.debug("="*20)
        cls._log.debug("结束测试")


    def test_001(self):
        """法师登录接口"""
        log.info('获取法师登录验证码授权')
        self.consumer_object.grant_authorization(phone='15818650805', code='123456')
        log.info('法师端登录')
        self.consumer_object.login_Master(phone='15818650805')



if __name__ == '__main__':
    unittest.main()