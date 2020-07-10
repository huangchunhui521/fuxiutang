# -*- coding: utf-8 -*-

<<<<<<< HEAD

class CompareStr(object):

    def is_contains(self,str1,str2):
=======
from lib.TestCaseKeyWord import *

class CompareStr(object):

    @classmethod
    def is_contains(cls,str1,str2):
>>>>>>> f09d45ad1756c30239c058666d78fd46362773e5
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
<<<<<<< HEAD
    cs=CompareStr()
    print(cs.is_contains('1','123'))
=======


    print(CompareStr.is_contains('1','1'))
>>>>>>> f09d45ad1756c30239c058666d78fd46362773e5

