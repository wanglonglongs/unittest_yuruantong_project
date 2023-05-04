# coding:utf-8
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from yuruantong_pc.common.error_screenshot import Screen
from yuruantong_pc.common.yaml_helper import YamlHelper
from yuruantong_pc.common.packaging_methon.yu_ruan_login import LoginPage
from nb_log import LogManager


class landlordCheckOutCase(unittest.TestCase):

    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        # 创建Chrome浏览器对象
        cls.driver.maximize_window()
        cls.element_locator_yaml = r'../configs/element_locator/fang_dong_login.yaml '
        cls.element = YamlHelper.read_yaml(cls.element_locator_yaml)
        cls.wait = WebDriverWait(cls.driver, 10, poll_frequency=0.5)
        cls.logger = LogManager('房东退房').get_logger_and_add_handlers(10,log_filename='房东退房.log')

    @Screen(driver=driver)
    def test_1_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)
        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        time.sleep(5)
        # logger.info('登录成功')
        self.logger.info("登录寓软通账号成功 -success")

    @Screen(driver=driver)
    def test_2_jump_whole_page(self):
        time.sleep(3)
        # 创建LoginPage对象
        self.driver.get("http://test.yuruantong.com/amp/wholeTenement/")
        self.logger.info("重新进入整租页面 -success")

    # 房东退房
    @Screen(driver=driver)
    def test_3_click_landlord_button(self):
        print(1)


    @classmethod
    def tearDownClass(cls):
        time.sleep(2000)
        # 关闭浏览器对象
        cls.driver.quit()
