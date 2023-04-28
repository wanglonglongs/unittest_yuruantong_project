import unittest
from yuruantong_pc.tests.test_housing_management_case import wholeManagementCase
from yuruantong_pc.tests.test_check_in_tenant_case import checkInTenant

if __name__ == "__main__":

    # 构造测试集
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

    # 租客登记
    suite.addTest(checkInTenant("test_login_yuRuanTong"))
    suite.addTest(checkInTenant("test_openTag_page"))
    suite.addTest(checkInTenant("test_zuLinStatus"))

    # 执行测试
    runner = unittest.TextTestRunner(verbosity=9)
    runner.run(suite)