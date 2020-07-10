# -*- coding: utf-8 -*-

# @File:
# @Time :
# @Author :
# @Detail : 善行

from lib.Operate_Excel import Operate_Execl
from lib import TestCaseKeyWord
import ast


class getData(object):
    def __init__(self):
        self.op_excel=Operate_Execl()

    def get_case_nums(self):
        """获取用例条数"""
        return self.op_excel.get_sheet_nrows()

    def get_is_header(self,row):
        """是否携带请求头"""
        col=int(TestCaseKeyWord.get_case_header())
        header=self.op_excel.get_sheet_cell(row,col)
        if header is not None:
            return header
        else:
            print("没有header")
            return None

    def get_is_run(self,row):
        """是否运行"""
        col=int(TestCaseKeyWord.get_case_is_excute())
        is_run=self.op_excel.get_sheet_cell(row,col)
        if is_run=='yes':
            flag=True

        else:
            flag=False

        return flag

    def get_url(self,row):
        """获取url"""
        col=int(TestCaseKeyWord.get_case_interface_url())
        url=self.op_excel.get_sheet_cell(row,col)
        return url

    def get_method(self,row):
        """获取请求方法"""
        col=int(TestCaseKeyWord.get_case_method())
        method=self.op_excel.get_sheet_cell(row,col)
        return method

    def get_data(self,row):
        """获取请求数据"""
        col=int(TestCaseKeyWord.get_case_payload())
        data=self.op_excel.get_sheet_cell(row,col)
        return data

    def get_excepted_result(self,row):
        """获取预期结果"""
        col=int(TestCaseKeyWord.get_case_expected_result())
        expected_result=self.op_excel.get_sheet_cell(row,col)
        if expected_result=='':
            return None
        else:
            return ast.literal_eval(expected_result)
<<<<<<< HEAD
=======

>>>>>>> f09d45ad1756c30239c058666d78fd46362773e5

    def get_actual_result(self,row,value):
        """获取实际结果"""
        col = int(TestCaseKeyWord.get_case_actual_result())
        actual_result = self.op_excel.get_sheet_cell(row,col)
        self.op_excel.write_to_excel(row,col,value)





if __name__ == '__main__':
    get_data=getData()
    print(get_data.get_is_run(1))
    print(get_data.get_url(1))
    # print(get_data.get_actual_result(1,"test"))




