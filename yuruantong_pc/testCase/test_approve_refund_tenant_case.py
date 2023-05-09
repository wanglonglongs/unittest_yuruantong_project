import time
import unittest
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yuruantong_pc.common.yaml_helper import YamlHelper
from yuruantong_pc.common.packaging_methon.yu_ruan_login import LoginPage
from yuruantong_pc.common.error_screenshot import Screen
from nb_log import get_logger, LogManager


class approveRefundTenant(unittest.TestCase):
    """   租客退房审批    """

    @classmethod
    def setUpClass(cls):
        # 创建Chrome浏览器对象
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.element_locator_yaml = '../configs/element_locator/fang_dong_login.yaml'
        cls.element = YamlHelper.read_yaml(cls.element_locator_yaml)

        cls.element_locator_whole_yaml = '../configs/element_locator/whole_rent_path_enum.yaml'
        cls.element_whole = YamlHelper.read_yaml(cls.element_locator_whole_yaml)
        cls.wait = WebDriverWait(cls.driver, 10, poll_frequency=0.5)
        cls.logger = LogManager('租客退房审批').get_logger_and_add_handlers(10, log_filename='审批.log')

    def test_approve_refund_tenant_login(self):
        ''' 登录 '''
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)

        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        self.logger.info("租客退房审批-登录-success")
        time.sleep(2)

    def test_approve_refund_tenant_openTag_page(self):
        ''' 切换租客审批界面 '''
        # 进入租客审批界面
        self.driver.get('http://test.v1.yuruantong.com/approval/?#/businessTenant')

        time.sleep(3)
        # 点击租客退房 进入
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/span[2]'))).click()


    # 租客审批
    def test_approve_refund_tenant_detail(self):
        ''' 租客退房初审/复审 '''
        # 点击租客确认
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[13]/div/div/div'))).click()

        time.sleep(2)
        # 备注 当前时间
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div/div/div[2]/div/div[2]/div[2]/div/textarea'))).send_keys("自动测试时间:" + current_time)
        time.sleep(2)

        # 点击租客确认弹框 通过
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div/div/div[2]/div/div[3]/button[2]'))).click()

        # # 点击租客确认弹框 驳回
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div/div/div[2]/div/div[3]/button[1]'))).click()

        # 接口反应时间 会提示操作频繁
        time.sleep(2)

        # 点击审批
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[14]/div/div/div'))).click()

        # 点击审批弹框 通过
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[2]/button[2]'))).click()

        # # 点击审批弹框 驳回
        # self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[2]/button[1]'))).click()

        time.sleep(2)

        # 点击复审
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[15]/div/div/div'))).click()
        time.sleep(2)

        # 点击复审弹框 通过
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div/div[3]/button[2]'))).click()

        # # 点击复审弹框 驳回
        # self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div/div[3]/button[1]'))).click()
        self.logger.info("租客退房审批成功 -success")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        # 关闭浏览器对象
        cls.driver.quit()



