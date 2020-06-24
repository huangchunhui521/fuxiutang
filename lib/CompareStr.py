# coding=utf8

from lib.TestCaseKeyWord import TestCaseKeyWord
class CompareStr(object):
    def is_contains(self,str1,str2):
        """
        判断预期结果与实际结果是否相同
        :param str1: 预期结果
        :param str2:实际结果
        :return:标记
        """
        # str1=TestCaseKeyWord.EXPECTED_RESULT
        # str2=TestCaseKeyWord.ACTUAL_RESULT

        self.flag=None
        if str1 in str2:
            self.flag=True
        else:
            self.flag=False
        return self.flag


if __name__ == '__main__':
    cs=CompareStr()
    print(cs.is_contains('1234','123456'))

