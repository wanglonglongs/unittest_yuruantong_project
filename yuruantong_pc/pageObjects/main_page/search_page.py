import time

from yuruantong_pc.common.handle_path import config_path
from yuruantong_pc.common.handle_yaml import get_yaml_data
from yuruantong_pc.pageObjects.basePage import BasePage


# 继承基类
class SearchPage(BasePage):

    # ------------------------------------------------------------------------------------------------------------------
    #                                                     房东审批搜索页面操作方法
    # ------------------------------------------------------------------------------------------------------------------
    def landlord_approval_status_search(self):
        # 读取yaml定位参数locator['Approval']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\approvalLandlordPageElement.yaml')['Approval']
        # 点击更多按钮
        self.click(locator['more_btn'],action="点击登记按钮")
        # 点击审批状态
        self.click(locator['approval_status_selection'],action="点击审批状态")
        # 选择审批状态 （未审批）
        self.click(locator['approval_status_dropdown'],action="选择审批状态未审批")
        # 点击搜索按钮
        self.click(locator['search_btn'],action="点击搜索按钮")
