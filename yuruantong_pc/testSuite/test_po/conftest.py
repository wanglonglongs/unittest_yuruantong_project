import os
import allure
import pytest

from yuruantong_pc.common.myDriver import Driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item: 测试用例
    :param call: 测试步骤
    :return:
    """
    # 获取钩子方法的调用结果
    out_come = yield
    rep = out_come.get_result()  # 从钩子方法的调用结果中获取测试报告
    # rep.when表示测试步骤，仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write((rep.nodeid + extra + "\n"))
        # 添加allure报告截图
        dirver = Driver().get_driver()
        if hasattr(dirver, "get_screenshot_as_png"):
            with allure.step('用例执行失败时，添加失败截图...'):
                allure.attach(dirver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
