import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yuruantong_pc.common.yaml_helper import YamlHelper
from yuruantong_pc.common.packaging_methon.yu_ruan_login import LoginPage
import random
from yuruantong_pc.common.error_screenshot import Screen
import string
import datetime
from nb_log import get_logger
from selenium.webdriver.support.ui import Select
from yuruantong_pc.common.packaging_methon.yu_ruan_common import perform_action


class checkInTenant(unittest.TestCase):
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
        cls.logger = get_logger('登记租客')

    @Screen(driver=driver)
    def test_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)

        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        self.logger.info("登记租客成功")

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
        self.logger.info("打开整租管理页面成功")

        # 重新进入整租页面中
        self.driver.get('http://test.yuruantong.com/amp/wholeTenement/')

    # 租赁状态未租选择
    @Screen(driver=driver)
    def test_zuLinStatus(self):
        print("1111111111111111111")
        # 租赁状态选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[1]/div/div/div/form/div[2]/div/div/div[1]/input'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[1]/div/div/div/form/div[2]/div/div/div[1]/input'))).send_keys("未租")
        # 选择未租
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[1]'))).click()
        # 点击搜索
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[1]/div/div/div/form/div[5]/button[1]'))).click()
        # 登记租客
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/section/main/div[1]/div/div/div/div[4]/div[2]/table/tbody/tr[1]/td[24]/div/div[1]/button'))).click()


    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        # 关闭浏览器对象
        cls.driver.quit()



