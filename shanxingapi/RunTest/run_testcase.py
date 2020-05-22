# -*- coding: utf-8 -*-


from shanxingapi.RunTest import *
import datetime

if __name__ == '__main__':
    nowtime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H_%M_%S')
    # testcase_dir = "D:\shanxing\TestCase"
    testcase_dir= "D:\\fuxiutang\shanxingapi\\testcase"
    report_dir= "D:\\fuxiutang\shanxingapi\\report"
    result = br(unittest.defaultTestLoader.discover(testcase_dir, "case.py"))
    result.report(
        filename="善行"+nowtime+'自动化测试报告',
        description='善行-安卓ui自动化测试',
        report_dir=report_dir,
    )
