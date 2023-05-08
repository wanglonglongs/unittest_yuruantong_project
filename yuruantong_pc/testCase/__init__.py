# -*- coding:utf-8 -*-
import unittest
import os
import time
import HTMLTestRunnerNew
from yuruantong_pc.testCase.test_approve_check_tenant import approveCheckTenant
from yuruantong_pc.testCase.test_approve_refund_tenant_case import approveRefundTenant
from yuruantong_pc.testCase.test_housing_management_case import wholeManagementCase
from yuruantong_pc.testCase.test_check_tenant_case import checkInTenant
from yuruantong_pc.testCase.test_examine_and_approve import examineApproveCase
from yuruantong_pc.testCase.test_landl_exit_case import landlordCheckOutCase
from yuruantong_pc.testCase.test_refund_tenant_case import refundTenant
from yuruantong_pc.testCase.test_out_approve_landl import outApproverLandl

# 用例路径
# 报告存放路径
os.chdir('../result')
report_path = os.path.join(os.getcwd(), 'report')
print(report_path)


def all_case():
    # 房东登记
    suite = unittest.TestSuite()
    suite.addTest(wholeManagementCase("test_login_yuRuanTong"))
    suite.addTest(wholeManagementCase("test_openTag_page"))
    suite.addTest(wholeManagementCase("test_pen_register_landlord"))
    suite.addTest(wholeManagementCase("test_write_basic_information"))
    suite.addTest(wholeManagementCase("test_write_landlord_information"))
    suite.addTest(wholeManagementCase("test_write_trusteeship_information"))
    suite.addTest(wholeManagementCase("test_write_delivery_information"))
    suite.addTest(wholeManagementCase("test_write_deduct_money_information"))
    suite.addTest(wholeManagementCase("test_write_other_information"))
    suite.addTest(wholeManagementCase("test_write_Item_information"))
    suite.addTest(wholeManagementCase("test_Read_bills_information"))
    suite.addTest(wholeManagementCase("test_upload_contract_information"))

    # 房东登记审批
    suite.addTest(examineApproveCase("test_login_yuRuanTong"))
    suite.addTest(examineApproveCase("test_jump_examine_page"))
    suite.addTest(examineApproveCase("test_click_careful_button"))

    # 租客登记
    suite.addTest(checkInTenant("test_register_tenant_login_yuRuanTong"))
    suite.addTest(checkInTenant("test_register_tenant_openTag_page"))
    suite.addTest(checkInTenant("test_lease_status_choose"))
    suite.addTest(checkInTenant("test_tenant_basics_info"))
    suite.addTest(checkInTenant("test_tenant_lease_info"))
    suite.addTest(checkInTenant("test_other_deduct_info"))
    suite.addTest(checkInTenant("test_preview_bill_info"))
    suite.addTest(checkInTenant("test_preview_contract_info"))

    # 租客登记审批
    suite.addTest(approveCheckTenant("test_approve_tenant_login_yuRuanTong"))
    suite.addTest(approveCheckTenant("test_approve_tenant_openTag_page"))
    suite.addTest(approveCheckTenant("test_approve_tenant_detail"))

    # 租客退房
    suite.addTest(refundTenant("test_refund_tenant_login_yuRuanTong"))
    suite.addTest(refundTenant("test_refund_tenant_openTag_page"))
    suite.addTest(refundTenant("test_lease_status_choose"))
    suite.addTest(refundTenant("test_enter_refund_tenant"))
    suite.addTest(refundTenant("test_operation_refund_tenant"))
    suite.addTest(refundTenant("test_energy_charges_deducted"))
    suite.addTest(refundTenant("test_other_fees_deducted"))
    suite.addTest(refundTenant("test_check_out_photo"))
    suite.addTest(refundTenant("test_refund_tenant_confirm"))

    # 租客退房审批
    suite.addTest(approveRefundTenant("test_approve_refund_tenant_login"))
    suite.addTest(approveRefundTenant("test_approve_refund_tenant_openTag_page"))
    suite.addTest(approveRefundTenant("test_approve_refund_tenant_detail"))

    # 房东退房
    suite.addTest(landlordCheckOutCase("test_1_login_yuRuanTong"))
    suite.addTest(landlordCheckOutCase("test_2_jump_whole_page"))
    suite.addTest(landlordCheckOutCase("test_3_click_landlord_button"))
    suite.addTest(landlordCheckOutCase("test_4_click_landlord_button"))
    suite.addTest(landlordCheckOutCase("test_5_click_landlord_button"))
    suite.addTest(landlordCheckOutCase("test_6_click_landlord_button"))
    suite.addTest(landlordCheckOutCase("test_7_click_landlord_button"))
    suite.addTest(landlordCheckOutCase("test_8_click_landlord_button"))
    suite.addTest(landlordCheckOutCase("test_9_click_landlord_button"))

    # 房东退房审批
    suite.addTest(outApproverLandl("test_1_login_yuRuanTong"))
    suite.addTest(outApproverLandl("test_2_jump_examine_page"))
    suite.addTest(outApproverLandl("test_3_click_careful_button"))


    print(suite)
    return(suite)


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
