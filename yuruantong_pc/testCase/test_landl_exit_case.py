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
import datetime


class landlordCheckOutCase(unittest.TestCase):
    """   房东退房    """

    @classmethod
    def setUpClass(cls):
        # 创建Chrome浏览器对象
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.element_locator_yaml = r'../configs/element_locator/fang_dong_login.yaml '
        cls.element = YamlHelper.read_yaml(cls.element_locator_yaml)
        cls.wait = WebDriverWait(cls.driver, 10, poll_frequency=0.5)
        cls.logger = LogManager('房东退房').get_logger_and_add_handlers(10,log_filename='房东退房.log')
        cls.common_utill = yu_ruan_common

    def test_login_yuRuanTong(self):
        ''' 登录 '''
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)
        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        time.sleep(5)
        # logger.info('登录成功')
        self.logger.info("登录寓软通账号成功 -success")

    def test_jump_whole_page(self):
        ''' 切换整租界面 '''
        time.sleep(3)
        # 创建LoginPage对象
        self.driver.get("http://test.v1.yuruantong.com/wholeTenement/")
        self.logger.info("重新进入整租页面 -success")

    # 房东退房
    def test_switch_tag(self):
        ''' 进入房东退房 '''
        time.sleep(2)
        # 切换至房东标签页
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/span[2]'))).click()
        # 打开操作菜单栏
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/section/main/div[1]/div/div[5]/div[2]/table/tbody/tr[1]/td[21]/div/button/span/div/button/span'))).click()
        # 房东退房按钮
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > ul > div.el-tree > div:nth-child(4) > div > span.el-tree-node__label'))).click()
        time.sleep(3)

    # 退房信息
    def test_landlord_basics_info(self):
        ''' 填写房东退房信息 '''
        # 水止数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[3]/div[1]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 电止数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[3]/div[2]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 气止数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[3]/div[3]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 物管费交至
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[3]/div[4]/div/div/div/div/input'))).click()
        time.sleep(2)
        # 选择日期
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[4]/div/span'))).click()

        time.sleep(1)

    # 房东应退还
    def test_refundable_proceeds(self):
        ''' 填写房东应退还 '''
        # 退还押金
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[5]/div[1]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 剩余房租
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[5]/div[2]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 其他应退
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[5]/div[3]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        # 卖东西给房东
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[5]/div[4]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_one_num(1,1000))
        time.sleep(1)

    # 被房东扣除金额
    def test_amount_deducted_landlord(self):
        ''' 填写被房东扣除金额 '''
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
        time.sleep(1)

    # 退房照片
    def test_refund_photo(self):
        ''' 填写退房照片 '''
        # 退房照片
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[12]/div/div/div/div/div[1]/div/input'))).send_keys(rf"F:\photo\{self.common_utill.free_random_one_num(1,4)}.jpg")

    # 备注信息
    def test_landlord_remark(self):
        ''' 填写备注信息 '''
        # 备注
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[2]/form/div[14]/div/div/div/div/div/textarea'))).send_keys("自动化测试时间:" + current_time)
        time.sleep(2)

    # 提交退房
    def test_click_landlord_button(self):
        ''' 提交退房 '''
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[3]/button[2]'))).click()
        time.sleep(3)
        # 第一次点击 没法调接口 再次点击
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[7]/div/div/div[3]/button[2]'))).click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        # 关闭浏览器对象
        cls.driver.quit()


if __name__ == '__main__':
    landlordCheckOutCase()
