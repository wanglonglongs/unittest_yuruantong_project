import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yuruantong_pc.common.yaml_helper import YamlHelper
from yuruantong_pc.common.packaging_methon.yu_ruan_login import LoginPage
from yuruantong_pc.common.error_screenshot import Screen
from nb_log import get_logger, LogManager


class approveCheckTenant(unittest.TestCase):
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
        cls.logger = LogManager('登记租客审批').get_logger_and_add_handlers(10, log_filename='登记租客审批.log')

    @Screen(driver=driver)
    def test_approve_tenant_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)

        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        self.logger.info("登记租客审批-登录")
        time.sleep(2)

    @Screen(driver=driver)
    def test_approve_tenant_openTag_page(self):
        # 进入租客审批界面
        self.driver.get('http://test.yuruantong.com/amp/approval/?#/businessTenant')

    # 租客审批
    @Screen(driver=driver)
    def test_approve_tenant_detail(self):
        # 点击初审
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[16]/div/div/div'))).click()

        # 点击初审弹框 通过
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div[2]/div/div[2]/button[2]'))).click()

        # # 点击初审弹框 驳回
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div[2]/div/div[2]/button[1]'))).click()
        time.sleep(5)

        # 点击复审
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[18]/div/div/div'))).click()

        # 点击复审弹框 通过
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div[2]/div/div[2]/button[2]'))).click()

        # # 点击复审弹框 驳回
        # self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div[2]/div/div[2]/button[1]'))).click()
        self.logger.info("登记租客审批成功")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        # 关闭浏览器对象
        cls.driver.quit()



