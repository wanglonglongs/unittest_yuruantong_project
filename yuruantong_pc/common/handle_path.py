import os

# 1、工程路径
# os.path.obspath(__file__)  当前文件路径
# os.path.dirname()------获取上一层路径
project_path = os.path.dirname(os.path.dirname(__file__))
# 2、截图路径
screenshot_path = os.path.join(project_path, r'common\error_screenshot')
# 3、日志路径
logs_path = os.path.join(project_path, r'outFiles\my_logs')
# 4、测试数据路径
testcase_path = os.path.join(project_path, 'data')
# 5、测试报告路径
reports_path = os.path.join(project_path, r'result\reports\tmp')
# 6、配置路径
config_path = os.path.join(project_path, 'configs')

if __name__ == '__main__':
    # print(project_path)
    # print(screenshot_path)
    # print(logs_path)
    # print(reports_path)
    # print(testcase_path)
    print(config_path)
