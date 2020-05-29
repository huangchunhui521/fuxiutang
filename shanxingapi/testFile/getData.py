# -*- coding: utf-8 -*-

# @File:
# @Time :
# @Author :
# @Detail : 善行

from shanxingapi.testFile.Operate_Excel import Operate_Execl
class getData(object):
    def __init__(self):
        self.op_excel=Operate_Execl()

    def get_case_nums(self):
        """获取用例条数"""
        return self.op_excel.get_sheet_nrows()

    def get_is_header(self):
        """是否携带请求头"""
        pass