# coding:utf-8
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yuruantong_pc.common.error_screenshot import Screen
from yuruantong_pc.common.yaml_helper import YamlHelper
from yuruantong_pc.common.packaging_methon.yu_ruan_login import LoginPage
from nb_log import LogManager
from yuruantong_pc.common.packaging_methon import yu_ruan_common


class outApproverLandl(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        # 创建Chrome浏览器对象
        cls.driver = webdriver.Chrome()
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.element_locator_yaml = r'../configs/element_locator/fang_dong_login.yaml '
        cls.element = YamlHelper.read_yaml(cls.element_locator_yaml)
        cls.wait = WebDriverWait(cls.driver, 10, poll_frequency=0.5)
        cls.logger = LogManager('审批').get_logger_and_add_handlers(10,log_filename='审批.log')
        cls.common_utill = yu_ruan_common

    def test_1_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)
        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        time.sleep(5)
        # logger.info('登录成功')
        self.logger.info("登录寓软通账号成功 -success")

    def test_2_jump_examine_page(self):
        time.sleep(3)
        # 创建LoginPage对象
        self.driver.get("http://test.yuruantong.com/amp/approval/")
        self.logger.info("跳转房东审批页面成功 -success")

    # 房东审批
    def test_3_click_careful_button(self):
        # 切换至退房审批页面
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/span[2]'))).click()
        # 初审
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[13]/div/div/div'))).click()
        time.sleep(3)

        # 房东退房审批弹框 （通过）
        preliminary_examination = 'document.querySelector("body > div:nth-child(4) > div > div > div.el-dialog__body > div > div:nth-child(2) > button.el-button.el-button--small.external-btn-size.green-color.font-color").click()'
        self.driver.execute_script(preliminary_examination)
        time.sleep(3)

        # 房东确认
        reexamine = 'document.querySelector("#app > div > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div.el-table__inner-wrapper > div.el-table__body-wrapper > div > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > table > tbody > tr:nth-child(1) > td.el-table_2_column_34.is-center.el-table-fixed-column--right.el-table__cell > div > div > div").click()'
        self.driver.execute_script(reexamine)
        time.sleep(3)

        # 替房东确认 （确认）
        reexamine1 = 'document.querySelector("body > div:nth-child(8) > div > div > div.el-dialog__body > div > div:nth-child(3) > button.el-button.el-button--small.external-btn-size.green-color.font-color").click()'
        self.driver.execute_script(reexamine1)
        time.sleep(3)
        # 复审
        reexamine2 = 'document.querySelector("#app > div > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div.el-table__inner-wrapper > div.el-table__body-wrapper > div > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > table > tbody > tr:nth-child(1) > td.el-table_2_column_35.is-center.el-table-fixed-column--right.el-table__cell > div > div > div").click()'
        self.driver.execute_script(reexamine2)
        time.sleep(3)
        # 房东退房复审
        reexamine3 = 'document.querySelector("body > div:nth-child(6) > div > div > div.el-dialog__body > div > div:nth-child(2) > button.el-button.el-button--small.external-btn-size.green-color.font-color").click()'
        self.driver.execute_script(reexamine3)

        self.logger.info("房东退审 -success")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        # 关闭浏览器对象
        cls.driver.quit()