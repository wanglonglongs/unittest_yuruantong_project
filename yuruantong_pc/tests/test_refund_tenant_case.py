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
from nb_log import get_logger, LogManager
from selenium.webdriver.support.ui import Select
from yuruantong_pc.common.packaging_methon import yu_ruan_common


class refundTenant(unittest.TestCase):
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
        cls.logger = LogManager('租客退房').get_logger_and_add_handlers(10,log_filename='租客退房.log')

    @Screen(driver=driver)
    def test_refund_tenant_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)

        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        self.logger.info("租客退房-登录-success")
        time.sleep(2)
    @Screen(driver=driver)
    def test_refund_tenant_openTag_page(self):
        # 重新进入整租页面中
        self.driver.get('http://test.yuruantong.com/amp/wholeTenement/')

    # 租赁状态已租选择
    @Screen(driver=driver)
    def test_lease_status_choose(self):
        # 租赁状态下拉
        lease_status = f'document.querySelector("#app > div > div:nth-child(2) > div > div:nth-child(1) > div > div.el-card__header > div > div > div > form > div:nth-child(2) > div > div > div > input").click()'
        self.driver.execute_script(lease_status)

        # 已租下拉选择
        lease_status_choose = f'document.querySelector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)").click()'
        self.driver.execute_script(lease_status_choose)

        # 搜索
        search = f'document.querySelector("#app > div > div:nth-child(2) > div > div:nth-child(1) > div > div.el-card__header > div > div > div > form > div:nth-child(5) > button.el-button.el-button--danger.el-button--mini").click()'
        self.driver.execute_script(search)
        time.sleep(2)
        self.logger.info("筛选已租状态完成-success")

    # 点击租客退房
    @Screen(driver=driver)
    def test_enter_refund_tenant(self):
        # 点击操作按钮
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/section/main/div[1]/div/div/div/div[4]/div[2]/table/tbody/tr[1]/td[24]/div/div[2]/button/span/div/button'))).click()

        # 点击租客退房
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/ul/div[1]/div[4]/div/span[2]'))).click()
        self.logger.info("进入租客退房界面-success")

    # 进入租客退房操作界面,信息填写 (应退还给租客)
    @Screen(driver=driver)
    def test_operation_refund_tenant(self):
        # 退还押金
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[6]/div[1]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(3))

        # 剩余房租
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[6]/div[2]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(3))

        # 预存物管费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[6]/div[3]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 预存水费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[6]/div[4]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 预存电费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[6]/div[5]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 预存气费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[6]/div[6]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 服务费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[6]/div[7]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 空调费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[6]/div[8]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 退还房租
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[6]/div[9]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(3))


    # 应扣能源费
    @Screen(driver=driver)
    def test_energy_charges_deducted(self):
        # 水费-上次底数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[8]/div[1]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(1))

        # 水费-本次底数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[8]/div[2]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 水费-单价
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[8]/div[3]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(1))

        # 水费-滞纳金
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[8]/div[4]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 电费-上次底数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[9]/div[1]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(1))

        # 电费-本次底数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[9]/div[2]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 电费-单价
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[9]/div[3]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(1))

        # 电费-滞纳金
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[9]/div[4]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 气费-上次底数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[10]/div[1]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(1))

        # 气费-本次底数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[10]/div[2]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 气费-单价
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[10]/div[3]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(1))

        # 气费-滞纳金
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[10]/div[4]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

    # 应扣其他费
    @Screen(driver=driver)
    def test_other_fees_deducted(self):
        # 违约金
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[13]/div[1]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 垃圾费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[13]/div[2]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 赔偿费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[13]/div[3]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 清洁费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[13]/div[4]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 其他费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[14]/div[1]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

        # 超期房租天数
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[14]/div[2]/div/div/div/div[1]/input'))).send_keys(yu_ruan_common.free_random_many_num(1))

        # 空调费
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[14]/div[3]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))

    # 退房照片 + 备注信息
    @Screen(driver=driver)
    def test_check_out_photo(self):
        # 身份证照片
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[18]/div/div/div/div/div[1]/div/input'))).send_keys(fr"F:\photo\{yu_ruan_common.free_random_one_num(1, 4)}.jpg")

        # 备注 当前时间
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[2]/form/div[20]/div/div/div/div/div/textarea'))).send_keys(current_time)

    # 租客退房确认 取消
    @Screen(driver=driver)
    def test_refund_tenant_confirm(self):
        time.sleep(2)
        # 确认
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[3]/div/div/div[3]/button[2]'))).click()
        time.sleep(2)
        # # 取消
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/section/main/div[1]/div/div/div/div[4]/div[2]/table/tbody/tr[1]/td[24]/div/div[2]/button/span/div/button'))).click()
        self.logger.info("租客退房审批成功-success")
    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        # 关闭浏览器对象
        cls.driver.quit()



