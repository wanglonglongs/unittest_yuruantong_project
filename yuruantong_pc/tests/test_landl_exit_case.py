# coding:utf-8
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from yuruantong_pc.common.error_screenshot import Screen
from yuruantong_pc.common.yaml_helper import YamlHelper
from yuruantong_pc.common.packaging_methon.yu_ruan_login import LoginPage
from yuruantong_pc.common.packaging_methon import yu_ruan_common
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
        cls.common_utill = yu_ruan_common

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
        # 切换至房东标签页
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/span[2]'))).click()
        # 打开操作菜单栏
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/section/main/div[1]/div/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/button/span/div/button/span'))).click()
        # 房东退房按钮
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > ul > div.el-tree > div:nth-child(4) > div > span.el-tree-node__label'))).click()
        time.sleep(3)

    # 退房信息
    @Screen(driver=driver)
    def test_4_click_landlord_button(self):
        # 水止数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[3]/div[1]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 电止数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[3]/div[2]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 气止数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[3]/div[3]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 物管费交至
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[3]/div[4]/div/div/div/div/input'))).click()
        # 选择日期
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[4]/div/span'))).click()

    # 房东应退还
    @Screen(driver=driver)
    def test_5_click_landlord_button(self):
        # 退还押金
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[5]/div[1]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 剩余房租
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[5]/div[2]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 其他应退
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[5]/div[3]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 卖东西给房东
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[5]/div[4]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))

    # 被房东扣除金额
    @Screen(driver=driver)
    def test_6_click_landlord_button(self):
        # 水费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[7]/div[1]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,500))
        # 电费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[7]/div[2]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,500))
        # 气费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[7]/div[3]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,500))
        # 物管费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[7]/div[4]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,500))
        # 垃圾费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[8]/div[1]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,500))
        # 赔偿费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[8]/div[2]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,500))
        # 清洁费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[8]/div[3]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,500))
        # 其他费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[8]/div[4]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,500))

    # 退房照片
    @Screen(driver=driver)
    def test_7_click_landlord_button(self):
        # 退房照片
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[12]/div/div/div/div/div[1]/div/input'))).send_keys(rf"F:\photo\{self.common_utill.free_random_one_num(1,4)}.jpg")

    # 备注信息
    @Screen(driver=driver)
    def test_8_click_landlord_button(self):
        # 备注
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[14]/div/div/div/div/div/textarea'))).send_keys('%Y-%m-%d %H:%M:%S')

    # 提交退房
    @Screen(driver=driver)
    def test_9_click_landlord_button(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[3]/button[2]'))).click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        # 关闭浏览器对象
        cls.driver.quit()


if __name__ == '__main__':
    landlordCheckOutCase()
