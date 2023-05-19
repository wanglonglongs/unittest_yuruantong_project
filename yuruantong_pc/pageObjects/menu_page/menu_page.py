from yuruantong_pc.pageObjects.basePage import BasePage
from yuruantong_pc.common.handle_yaml import get_yaml_data
from yuruantong_pc.common.handle_path import config_path


# 继承基类
class MenuPage(BasePage):
    # 点击房源按钮
    def click_house_resources_button(self):
        # 读取yaml定位参数locator['LoginPage']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\new_fangdong.yaml')['Menu']
        # 点击菜单房源按钮
        self.click(locator['house_resources_btn'],action="点击房源按钮")

    # 点击整租按钮
    def click_whole_management_button(self):
        # 读取yaml定位参数locator['LoginPage']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\new_fangdong.yaml')['Menu']
        # 点击整租按钮
        self.click(locator['whole_management_btn'],action="点击整租按钮")