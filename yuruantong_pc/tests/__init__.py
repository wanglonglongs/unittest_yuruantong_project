# -*- coding:utf-8 -*-
import unittest
import os
import time
import HTMLTestRunnerNew
from yuruantong_pc.tests.test_housing_management_case import wholeManagementCase
from yuruantong_pc.tests.test_check_in_tenant_case import checkInTenant
from yuruantong_pc.tests.test_examine_and_approve import examineApproveCase

# 用例路径
case_path = os.path.join(os.path.dirname(__file__),"tests")
# 报告存放路径
os.chdir('../result')
report_path = os.path.join(os.getcwd(), 'report')
print(report_path)


def all_case():
    # 房东登记
    suite = unittest.TestSuite()
    suite.addTest(wholeManagementCase("test_1_case_login_yuRuanTong"))
    suite.addTest(wholeManagementCase("test_2_case_openTag_page"))
    suite.addTest(wholeManagementCase("test_3_case_pen_register_landlord"))
    suite.addTest(wholeManagementCase("test_4_case_write_basic_information"))
    suite.addTest(wholeManagementCase("test_5_case_write_landlord_information"))
    suite.addTest(wholeManagementCase("test_6_case_write_trusteeship_information"))
    suite.addTest(wholeManagementCase("test_7_case_write_Item_information"))
    suite.addTest(wholeManagementCase("test_8_case_Read_bills_information"))
    suite.addTest(wholeManagementCase("test_9_case_upload_contract_information"))

    # 房东审批
    suite.addTest(examineApproveCase("test_1_case_login_yuRuanTong"))
    suite.addTest(examineApproveCase("test_2_case_jump_examine_page"))
    suite.addTest(examineApproveCase("test_3_case_click_careful_button"))

    # 租客登记
    suite.addTest(checkInTenant("test_login_yuRuanTong"))
    suite.addTest(checkInTenant("test_openTag_page"))
    suite.addTest(checkInTenant("test_zuLinStatus"))
    print(suite)
    return (suite)


if __name__ == '__main__':

    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 2、html报告文件路径
    report_abspath = os.path.join(report_path, "result_"+now+".html")

    # 3、打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fp,title=r'寓软通界面自动化测试报告,测试结果：',description=r'整租(登记流程)用例执行情况：',tester='王龙龙')
    # 4、调用add_case函数返回值
    runner.run(all_case())
    fp.close()
