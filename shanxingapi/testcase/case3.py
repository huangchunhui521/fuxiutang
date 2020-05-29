
from shanxingapi.testFile import TestCaseKeyWord

from shanxingapi.testFile.Operate_Excel import Operate_Execl




get_excel = Operate_Execl()
# 获取用例数
print(get_excel.get_sheet_nrows()-1)
# 返回用例名称关键字的列值
case_name_col = int(TestCaseKeyWord.get_case_name())
print(case_name_col)
# 获取第一条用例的名称
get_name = get_excel.get_sheet_cell(1,case_name_col)
print(get_name)