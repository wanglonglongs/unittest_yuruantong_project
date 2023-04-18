# coding:utf-8
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yuruantong_pc.common.yaml_helper import YamlHelper
from yuruantong_pc.common.packaging_methon.yu_ruan_login import LoginPage
import random
from yuruantong_pc.common.error_screenshot import Screen
import string

class registeredTenantCase(unittest.TestCase):

    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        # 创建Chrome浏览器对象
        cls.driver.maximize_window()
        cls.element_locator_yaml = '../configs/element_locator/fang_dong_login.yaml'
        cls.element = YamlHelper.read_yaml(cls.element_locator_yaml)

        cls.element_locator_whole_yaml = '../configs/element_locator/whole_rent_path_enum.yaml'
        cls.element_whole = YamlHelper.read_yaml(cls.element_locator_whole_yaml)
        cls.wait = WebDriverWait(cls.driver, 10, poll_frequency=0.5)

    @Screen(driver=driver)
    def test_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)

        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")

    @Screen(driver=driver)
    def test_openTag_page(self):
        # 点击菜单选项栏-房源
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.element["MENU_HOUSING_RESOURCES"]))).click()
        time.sleep(2)

        # 点击二级菜单按钮-整租管理
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.element["MENU_WHOLE_MANAGEMENT"]))).click()

        # 验证当前已经打开整租页标签
        jump_housing_results = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.element["TAG_NAME_WHOLE_MANAGEMENT"]))).get_attribute('text')
        self.assertEqual("整租管理" in jump_housing_results, True)

        time.sleep(3)


    # 租赁状态 未租选择
    @Screen(driver=driver)
    def test_zuLinStatus(self):


        # 租赁状态下拉
        lease_status = self.element_whole["LEASE_STATUS"]
        self.driver.execute_script(lease_status)

        # 未租下拉选择
        lease_status_choose = self.element_whole["LEASE_STATUS_CHOOSE"]
        self.driver.execute_script(lease_status_choose)

        # 搜索
        search = self.element_whole["LEASE_STATUS_SEARCH"]
        self.driver.execute_script(search)
        time.sleep(3)

        # 点击登记租客
        check_tenant = self.element_whole["REGISTER_TENANT_BUTTON"]
        self.driver.execute_script(check_tenant)
        time.sleep(1)

        # 生成随机字符
        def random_string_generator():
            print(string.ascii_letters)
            print(string.punctuation)
            return ''.join(random.sample(string.ascii_letters, 8))

        # 租客姓名
        # tenant_name = self.element_whole["TENANT_NAME"].value = random_string_generator()
        # print(tenant_name)
        # tenant_name = self.element_whole["TENANT_NAME"].value = {random_string_generator()}
        # tenant_name = self.element_whole["TENANT_NAME"] = random_string_generator()

        # tenant_name = self.element_whole["TENANT_NAME"] = “123abc”

        # 要加f , js抽出 无法塞值
        tenant_name = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div > div.registerTenlentStyle > div > div.container > div.formStyle > form > div:nth-child(4) > div:nth-child(1) > div > div > div > div > input").value = "{random_string_generator()}" '
        print(tenant_name)
        self.driver.execute_script(tenant_name)



    # 登记租客信息填写
    # @Screen(driver=driver)
    # def test_registered_tenant_info(self):
        # print('进来了1')
        # # 点击登记租客
        # check_tenant = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div > div:nth-child(1) > section > main > div.el-card.table-container.is-never-shadow > div > div > div > div.el-table__fixed-right > div.el-table__fixed-body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_24.is-center.el-table__cell > div > div:nth-child(1) > button").click()'
        # print('进来了2')
        # self.driver.execute_script(check_tenant)


    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        # 关闭浏览器对象
        cls.driver.quit()
