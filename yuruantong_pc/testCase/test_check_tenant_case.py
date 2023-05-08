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


class checkInTenant(unittest.TestCase):
    """   登记租客    """

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
        cls.logger = LogManager('登记租客').get_logger_and_add_handlers(10,log_filename='登记租客.log')

    def test_register_tenant_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)

        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        self.logger.info("登记租客-登录-success")

    def test_register_tenant_openTag_page(self):
        # 点击菜单选项栏-房源
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.element["MENU_HOUSING_RESOURCES"]))).click()
        time.sleep(2)

        # 点击二级菜单按钮-整租管理
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.element["MENU_WHOLE_MANAGEMENT"]))).click()

        # 验证当前已经打开整租页标签
        jump_housing_results = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.element["TAG_NAME_WHOLE_MANAGEMENT"]))).get_attribute('text')
        self.assertEqual("整租管理" in jump_housing_results, True)
        self.logger.info("打开整租管理页面成功-success")

        # 重新进入整租页面中
        self.driver.get('http://test.yuruantong.com/amp/wholeTenement/')

    # 租赁状态未租选择
    def test_register_tenant_detail(self):
        # 租赁状态下拉
        lease_status = f'document.querySelector("#app > div > div:nth-child(2) > div > div:nth-child(1) > div > div.el-card__header > div > div > div > form > div:nth-child(2) > div > div > div > input").click()'
        self.driver.execute_script(lease_status)

        # 未租下拉选择
        lease_status_choose = f'document.querySelector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)").click()'
        self.driver.execute_script(lease_status_choose)

        # 搜索
        search = f'document.querySelector("#app > div > div:nth-child(2) > div > div:nth-child(1) > div > div.el-card__header > div > div > div > form > div:nth-child(5) > button.el-button.el-button--danger.el-button--mini").click()'
        self.driver.execute_script(search)
        time.sleep(2)
        # 点击登记租客
        check_tenant = f'document.querySelector("#app > div > div:nth-child(2) > div > div:nth-child(1) > section > main > div.el-card.table-container.is-never-shadow > div > div > div > div.el-table__fixed-right > div.el-table__fixed-body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_24.is-center.el-table__cell > div > div:nth-child(1) > button").click()'
        self.driver.execute_script(check_tenant)
        time.sleep(2)

        # 租客姓名
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[4]/div[1]/div/div/div/div[1]/input'))).send_keys(yu_ruan_common.random_string_number(yu_ruan_common.free_random_one_num(8, 10)))

        # 证件类型选择 默认台胞证
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[4]/div[2]/div/div[1]/div/input'))).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[3]'))).click()
        # 台胞证默认值
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[4]/div[2]/div/div[2]/input'))).send_keys(yu_ruan_common.free_random_many_num(yu_ruan_common.free_random_one_num(8,11)))

        # 联系电话
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[4]/div[3]/div/div/div/div[1]/input'))).send_keys(yu_ruan_common.random_create_phone())

        # 紧急联系人
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[4]/div[4]/div/div/div/div/input'))).send_keys(yu_ruan_common.random_create_phone())

        # 业务人员点击
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[5]/div[1]/div/div/div/div/div[1]/input'))).click()
        time.sleep(1)
        # 业务人员选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[2]'))).click()

        # 协助人员点击
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[5]/div[2]/div/div/div/div/input'))).click()
        time.sleep(1)
        # 协助人员选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]'))).click()

        # 渠道来源点击
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[5]/div[4]/div/div/div/div/div[1]/input'))).click()
        time.sleep(1)
        # 渠道来源选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]'))).click()

        # 租赁期限年 点击
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[7]/div[3]/div/div/div/div[1]/div/div[1]/input'))).click()
        time.sleep(1)
        # 租赁期限年 选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[6]/div[1]/div[1]/ul/li[{yu_ruan_common.free_random_one_num(2,5)}]'))).click()

        # 租赁期限月 点击
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[7]/div[3]/div/div/div/div[2]/div/div/input'))).click()
        time.sleep(1)
        # 租赁期限月 选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[7]/div[1]/div[1]/ul/li[{yu_ruan_common.free_random_one_num(1,11)}]'))).click()

        # 缴费方式
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[8]/div[1]/div/div/div/div[2]/div/span'))).click()

        # 出房价格
        price = yu_ruan_common.free_random_many_num(4)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[8]/div[2]/div/div/div/div[1]/div/input'))).send_keys(price)

        time.sleep(1)
        # 房屋押金
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[8]/div[3]/div/div/div/div[2]/div/span'))).click()

        # 提前缴费
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[8]/div[4]/div/div/div/div[2]/div/span[1]'))).click()
        time.sleep(2)

        # 备注 当前时间
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[17]/div/div/div/div/div/textarea'))).send_keys(current_time)

        # 下一步 进入预览账单列表
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/div[2]/div[3]/button[2]'))).click()
        time.sleep(2)

        # 下一步 进入上传合同
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[3]/div[5]/button[2]'))).click()
        time.sleep(2)

        # 身份证照片
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div/div[1]/div/input'))).send_keys(fr"F:\photo\{yu_ruan_common.free_random_one_num(1,4)}.jpg")

        # 合同上传
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[4]/div/div/div/div/div[1]/div/input'))).send_keys(fr"F:\photo\{yu_ruan_common.free_random_one_num(1,4)}.jpg")

        # 交割单照片
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[6]/div/div/div/div/div[1]/div/input'))).send_keys(fr"F:\photo\{yu_ruan_common.free_random_one_num(1,4)}.jpg")

        # 其他
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[3]/div[2]/div[8]/div/div/div/div/div[1]/div/input'))).send_keys(fr"F:\photo\{yu_ruan_common.free_random_one_num(1,4)}.jpg")
        time.sleep(1)

        # 提交初审
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[3]/div[3]/button[2]'))).click()

        # # 提交复审
        # self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/div[3]/div[3]/button[3]'))).click()

        self.logger.info("登记租客成功-success")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        # 关闭浏览器对象
        cls.driver.quit()



