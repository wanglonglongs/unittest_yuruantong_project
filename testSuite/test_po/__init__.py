# # -*- coding:utf-8 -*-
# import unittest
# import os
# import time
# import HTMLTestRunnerNew
# from yuruantong_pc.testSuite.test_po.test_register_landlord_case import registerLandlordCase
# from yuruantong_pc.common.handle_path import reports_path
#
#
# def all_case():
#     # # 房东登记
#     suite = unittest.TestSuite()
#     suite.addTest(registerLandlordCase("test_login_case"))
#     suite.addTest(registerLandlordCase("test_click_house_resources_button"))
#     suite.addTest(registerLandlordCase("test_click_whole_management_button"))
#     suite.addTest(registerLandlordCase("test_go_to_whole_management"))
#     suite.addTest(registerLandlordCase("test_click_landlord_button"))
#     suite.addTest(registerLandlordCase("test_landlord_base_info_input"))
#     suite.addTest(registerLandlordCase("test_landlord_info_input"))
#     suite.addTest(registerLandlordCase("test_trusteeship_info"))
#     suite.addTest(registerLandlordCase("test_click_landlord_next_btn"))
#     suite.addTest(registerLandlordCase("test_item_information"))
#     suite.addTest(registerLandlordCase("test_click_item_next_btn"))
#     suite.addTest(registerLandlordCase("test_click_bill_next_btn"))
#     suite.addTest(registerLandlordCase("test_upload_contract"))
#     suite.addTest(registerLandlordCase("test_submit_first_review_btn"))
#     return(suite)
#
#
# if __name__ == '__main__':
#
#     # 1、获取当前时间，这样便于下面的使用。
#     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#
#     # 2、html报告文件路径
#     report_abspath = os.path.join(reports_path, "result_"+now+".html")
#
#     # 3、打开一个文件，将result写入此file中
#     fp = open(report_abspath, "wb")
#     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fp,title=r'测试结果：',description=r'用例执行情况：',tester='111')
#     # 4、调用add_case函数返回值
#     runner.run(all_case())
#     fp.close()
