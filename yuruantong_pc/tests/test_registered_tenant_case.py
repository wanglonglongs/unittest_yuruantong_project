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


class registeredTenantCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 创建Chrome浏览器对象
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.element_locator_yaml = '../configs/element_locator/fang_dong_login.yaml '
        cls.element = YamlHelper.read_yaml(cls.element_locator_yaml)
        cls.wait = WebDriverWait(cls.driver, 10, poll_frequency=0.5)

    def test_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)

        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")

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

        time.sleep(5)
    def test_zuLinStatus(self):
        input_block_number = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div > div:nth-child(1) > div > div.el-card__header > div > div > div > form > div:nth-child(2) > div > div > div > input").click()'
        self.driver.execute_script(input_block_number)

        # input_block_number2 = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item.hover > span").click()'
        # self.driver.execute_script(input_block_number2)

        # sousuo = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div > div:nth-child(1) > div > div.el-card__header > div > div > div > form > div:nth-child(5) > button.el-button.el-button--danger.el-button--mini > span").click()'
        # self.driver.execute_script(sousuo)
    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        # 关闭浏览器对象
        cls.driver.quit()
