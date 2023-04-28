import unittest,os
from yuruantong_pc.tests.test_housing_management_case import wholeManagementCase

if __name__ == "__main__":
    # tests 文件下的用例全部执行
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),"tests"),\
                                                pattern='*.py',top_level_dir=os.path.dirname(__file__))
    unittest.TextTestRunner(verbosity=2).run(suite)

    # # 此用法可以同时测试多个类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(test_housing_management_case)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(test_old_registered_tenant_case)
    # suite = unittest.TestSuite(suite1)
    # unittest.TextTestRunner(verbosity=2).run(suite)