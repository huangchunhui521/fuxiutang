# -*- coding: utf-8 -*-

from lib.TestCaseKeyWord import *

class CompareStr(object):

    @classmethod
    def is_contains(cls,str1,str2):
        """
        判断预期结果与实际结果是否相同
        :param str1: 预期结果
        :param str2:实际结果
        :return:标记
        """
        # str1=TestCaseKeyWord.EXPECTED_RESULT
        # str2=TestCaseKeyWord.ACTUAL_RESULT

        cls.flag=None
        if str1 == str2:
            cls.flag=True
        else:
            cls.flag=False
        return cls.flag


if __name__ == '__main__':


    print(CompareStr.is_contains('1','1'))

