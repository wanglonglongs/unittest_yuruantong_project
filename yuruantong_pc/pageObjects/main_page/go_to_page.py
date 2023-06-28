from yuruantong_pc.pageObjects.basePage import BasePage
from yuruantong_pc.configs.config import test_whole_management_url, test_landlord_approval_url, \
    formal_whole_management_url, pp_management_url, pp_url_landlord


# 继承基类
class goToPage(BasePage):
    # 跳转整租子页面按钮
    def go_to_whole_management(self):
        self._driver.get(test_whole_management_url)  # formal_whole_management_url,test_whole_management_url

    # 跳转房东审批子页面按钮
    def go_to_approval_landlord(self):
        self._driver.get(test_landlord_approval_url)  # formal_whole_management_url,test_whole_management_url
