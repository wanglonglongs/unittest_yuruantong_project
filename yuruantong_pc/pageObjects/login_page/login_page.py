from yuruantong_pc.pageObjects.basePage import BasePage
from yuruantong_pc.configs.config import test_url, formal_url, pp_url
from yuruantong_pc.common.handle_yaml import get_yaml_data
from yuruantong_pc.common.handle_path import config_path
import time


# 继承基类
class LoginPage(BasePage):

    def to_login_page(self):
        # 打开登录页面，url在config包中配置
        self._driver.get(test_url) # formal_url test_url
        return self

    def login(self, username, pwd):
        # 读取yaml定位参数locator['LoginPage']提取键值数据

        locator = get_yaml_data(rf'{config_path}\element_locator\loginPageElement.yaml')['LoginPage']

        self.input_text(locator['username_input'],username,action='输入账号')
        # 输入密码
        self.input_text(locator['pwd_input'],pwd,action="输入密码")
        # 点击登录按钮
        self.click(locator['login_btn'],action="点击登录按钮")
        # 已登陆账号名称
        return self.get_text(locator['account_name_span'],action="已登陆账号名称")