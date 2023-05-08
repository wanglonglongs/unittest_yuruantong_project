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


class examineApproveCase(unittest.TestCase):
    """   房东审批    """

    @classmethod
    def setUpClass(cls):
        # 创建Chrome浏览器对象
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.element_locator_yaml = r'../configs/element_locator/fang_dong_login.yaml '
        cls.element = YamlHelper.read_yaml(cls.element_locator_yaml)
        cls.wait = WebDriverWait(cls.driver, 10, poll_frequency=0.5)
        cls.logger = LogManager('登记房东审批').get_logger_and_add_handlers(10,log_filename='审批.log')
        cls.common_utill = yu_ruan_common

    def test_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)
        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        time.sleep(5)
        account_show_title = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="mainDiv"]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/div/div/span'))).text
        assert account_show_title == "李一昂", f"{self.logger.error('断言失败：登录寓软通账号失败！')}"
        self.logger.info('断言成功：登录寓软通账号成功！')

    def test_jump_examine_page(self):
        time.sleep(3)
        # 创建LoginPage对象
        self.driver.get("http://test.yuruantong.com/amp/approval/")
        self.logger.info("跳转房东审批页面成功 -success")
        time.sleep(3)
        # 重新进入整租页面中
        self.driver.get("http://test.yuruantong.com/amp/approval/")
        register_landlord_but_title = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[2]/table/thead/tr/th[17]/div'))).text
        assert register_landlord_but_title == "审批", f"{self.logger.error('断言失败：未进入房东审批页面！')}"
        self.logger.info('断言成功：已进入房东审批页面！')

    # 房东审批
    def test_click_careful_button(self):
        # 初审
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[17]/div/div'))).click()
        time.sleep(2)
        self.logger.info("点击初审按钮打开弹窗 -success")
        # 弹框 alert 登记房东审批
        preliminary_examination = 'document.querySelector("body > div:nth-child(4) > div > div > div.el-dialog__body > div > div:nth-child(2) > button.el-button.el-button--small.external-btn-size.green-color.font-color").click()'
        self.driver.execute_script(preliminary_examination)
        time.sleep(5)
        self.logger.info("通过房东初审 -success")

        # 复审
        reexamine = 'document.querySelector("#app > div > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div.el-table__inner-wrapper > div.el-table__body-wrapper > div > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > table > tbody > tr:nth-child(1) > td.el-table_1_column_19.is-center.el-table-fixed-column--right.el-table__cell > div > div > div").click()'
        self.driver.execute_script(reexamine)
        time.sleep(2)

        # 弹框 alert 登记房东复审
        reexamine1 = 'document.querySelector("body > div:nth-child(6) > div > div > div.el-dialog__body > div > div:nth-child(2) > button.el-button.el-button--small.external-btn-size.green-color.font-color").click()'
        self.driver.execute_script(reexamine1)
        time.sleep(5)
        self.logger.info("房东审批成功 -success")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        # 关闭浏览器对象
        cls.driver.quit()