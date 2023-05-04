# # -*- coding:utf-8 -*-
# import unittest
# import os
# import time
# import HTMLTestRunnerNew
#
# # 用例路径
# case_path = os.path.join(os.path.dirname(__file__),"tests")
# # 报告存放路径
# os.chdir('./result')
# report_path = os.path.join(os.getcwd(), 'report')
# print(report_path)
#
#
# def all_case():
#
#     discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=os.path.dirname(__file__))
#     print(discover)
#     return(discover)
#
#
# if __name__ == '__main__':
#
#     # 1、获取当前时间，这样便于下面的使用。
#     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#
#     # 2、html报告文件路径
#     report_abspath = os.path.join(report_path, "result_"+now+".html")
#
#     # 3、打开一个文件，将result写入此file中
#     fp = open(report_abspath, "wb")
#     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fp,title=r'寓软通界面自动化测试报告,测试结果：',description=r'整租(登记房东)用例执行情况：',tester='王龙龙')
#     # 4、调用add_case函数返回值
#     runner.run(all_case())
#     fp.close()
