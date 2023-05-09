# coding:utf-8
import time
import unittest
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yuruantong_pc.common.error_screenshot import Screen
from yuruantong_pc.common.yaml_helper import YamlHelper
from yuruantong_pc.common.packaging_methon.yu_ruan_login import LoginPage
from nb_log import LogManager
from yuruantong_pc.common.packaging_methon import yu_ruan_common


class wholeManagementCase(unittest.TestCase):
    """   登记房东    """

    @classmethod
    def setUpClass(cls):
        # 创建一个参数对象，用来控制chrome以无界面模式打开
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.element_locator_yaml = r'../configs/element_locator/fang_dong_login.yaml '
        cls.element = YamlHelper.read_yaml(cls.element_locator_yaml)
        cls.wait = WebDriverWait(cls.driver, 10, poll_frequency=0.5)
        cls.logger = LogManager('登记房东').get_logger_and_add_handlers(10,log_filename='登记房东.log')
        cls.common_utill = yu_ruan_common

    def test_login_yuRuanTong(self):
        """ 登录 """
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)
        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        time.sleep(5)
        account_show_title = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainDiv"]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/div/div/span'))).text
        assert account_show_title == "李一昂", f"{self.logger.error('断言失败：登录寓软通账号失败！')}"
        self.logger.info('断言成功：登录寓软通账号成功！')

    def test_openTag_page(self):
        """ 切换整租页面 """
        # 重新进入整租页面中
        self.driver.get('http://test.v1.yuruantong.com/wholeTenement/')
        register_landlord_but_title = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/button[1]'))).text
        assert register_landlord_but_title == "登记房东", f"{self.logger.error('断言失败：未进入整租页面！')}"
        self.logger.info('断言成功：已进入整租页面！')

    def test_pen_register_landlord(self):
        """ 进入登记房东页面 """
        # 进入登记房东整租页面 点击登记房东按钮
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/button[1]/span'))).click()
        basic_information_show_title = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[1]/span'))).text
        assert basic_information_show_title == "基本信息", f"{self.logger.error('断言失败：未进入登记房东页面！')}"
        self.logger.info('断言成功：已进入登记房东页面！')

    # 填写登记基本信息
    def test_write_basic_information(self):
        '''    房东基本信息    '''

        # 所属店面选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div/div/div/div/input'))).click()
        # 店面下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[1]'))).click()
        # 座幢填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[3]/div/div/div/div[1]/input'))).send_keys(self.common_utill.random_string_generator(1))
        # 单元填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[3]/div/div/div/div[2]/input'))).send_keys(self.common_utill.random_string_number(1))
        # 门牌号填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[4]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_many_num(6))
        # 接扣拉取 物业地址速度较慢 需等待
        time.sleep(2)
        # 物业地址选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[7]/div/div/div/div/div[1]/input'))).click()
        # 物业地址下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[1]'))).click()
        # 建筑面积填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[8]/div/div/div/div[1]/div/input'))).send_keys(self.common_utill.random_string_number(3))
        # 房屋类型选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[9]/div/div/div/div[1]/input'))).click()
        # # 房屋类型下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[1]'))).click()
        # # 装修程度选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[10]/div/div/div/div/div[1]/input'))).click()
        # # 装修程度下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[1]'))).click()
        # 所在楼层填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[11]/div/div/div/div[1]/input'))).send_keys("1")
        # 总楼层填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[11]/div/div/div/div[2]/input'))).send_keys("15")
        # 朝向选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[12]/div/div/div/div/div[1]/input'))).click()
        # # 朝向下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[1]/div[1]/ul/li[1]'))).click()

        self.logger.info("(房东) 基本信息")

    # # 填写登记房东信息
    def test_write_landlord_information(self):
        ''' 填写登记房东信息 '''
        # 填写房东姓名
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[1]/div/div/div/div/input'))).send_keys(self.common_utill.random_string_generator(3))
        # 选择证件类型
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/div[1]/div[1]/input'))).click()
        # 选择证件类型下拉选
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[7]/div[1]/div[1]/ul/li[2]/span'))).click()
        # 证件号码填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/div[2]/input'))).send_keys("42098419940501751X")
        # 手机号码填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[3]/div/div/div/div/input'))).send_keys(self.common_utill.random_create_phone())
        # 收款人姓名
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[4]/div/div/div/div/input'))).send_keys(self.common_utill.random_string_generator(3))
        # 银行卡卡号填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[6]/div/div/div/div/input'))).send_keys("6214835400894513")
        # 收款身份证填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[7]/div/div/div/div/input'))).send_keys("42098419940501751X")
        # 收款人手机号填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[8]/div/div/div/div/input'))).send_keys(self.common_utill.random_create_phone())
        # 渠道来源选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[9]/div/div/div/div/div[1]/input'))).click()
        # 渠道来源下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div[1]/div[1]/ul/li[1]'))).click()
        # 房东包物业 选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[10]/div/div/div/div[1]/div/input'))).click()
        # 房东包物业下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[8]/div[1]/div[1]/ul/li[2]/span'))).click()
        # 房东包物业 金额填写
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[10]/div/div/div/div[2]/input'))).send_keys("50")
        self.logger.info("(房东) 房东信息")

    # 填写托管房东信息
    def test_write_trusteeship_information(self):
        ''' 填写托管房东信息 '''
        # 开始时间
        # 结束时间
        # 合同期限按钮点击 3年
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[3]/div/div/div/span[1]'))).click()
        # 缴费方式
        # 收房价格填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[5]/div/div/div/input'))).send_keys("1500")
        # 房屋押金点击押一
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[6]/div/div/div/span'))).click()
        # 维修方案选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[7]/div/div/div/div/div[1]/input'))).click()
        # 维修方案下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div[1]/div[1]/ul/li[1]'))).click()
        # 装修方案选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[8]/div/div/div/div/div[1]/div[1]/input'))).click()
        # 装修方案下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div[1]/div[1]/ul/li[1]'))).click()
        # 首次付款日期选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[9]/div/div/div/div/input'))).click()
        time.sleep(2)
        # 首次付款日期下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[11]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[5]'))).click()
        # 业务人员选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[10]/div/div/div/div/div[1]/input'))).click()
        # 业务人员下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[12]/div[1]/div[1]/ul/li[1]'))).click()
        # 协助人员选择
        # 累计免租期选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[12]/div/div/div/div/div/div[1]/div/div[1]/input'))).click()
        # 累计免租期下拉选择
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[13]/div[1]/div[1]/ul/li[1]/span'))).click()
        self.logger.info("(房东) 托管信息")

        # 备注 当前时间
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                        '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[16]/div/div/div/div/div/div/textarea'))).send_keys(
            "自动化测试时间:" + current_time)
        self.logger.info("(房东) 其他信息")
        time.sleep(2)

        # 点击下一步
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/button[2]'))).click()
        self.logger.info("(房东) 托管信息")
        time.sleep(3)
    # # 填写交割信息
    # def test_write_delivery_information(self):
    #     ''' 填写交割信息 '''
    #     time.sleep(1)
    #     # 电表底数
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[8]/div[1]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(3))
    #     # 气表底数
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[8]/div[2]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(3))
    #     # 副电表底数
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[8]/div[3]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(1))
    #     # 水表底数
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[8]/div[4]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(3))
    #     # 副气表底数
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[8]/div[5]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))
    #     # 热水表底数
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[8]/div[6]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))
    #     # 副水表底数
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[8]/div[7]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))
    #     self.logger.info("(房东)交割信息")
    #
    # # 填写扣款信息
    # def test_write_deduct_money_information(self):
    #     ''' 填写扣款信息 '''
    #     time.sleep(1)
    #     # 扣除费用
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[12]/div[1]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))
    #     # 违约退房
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[12]/div[2]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(3))
    #     # 东西丢失
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[12]/div[3]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(3))
    #     # 转租扣除费
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[12]/div[4]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(2))
    #     # 杂物处理费
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[12]/div[5]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(1))
    #     self.logger.info("(房东) 扣款信息")
    #
    # # 填写其他信息 + 备注
    # def test_write_other_information(self):
    #     ''' 填写其他信息 '''
    #     time.sleep(1)
    #     # 门卡号
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[14]/div[1]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(7))
    #     # 气卡号
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[14]/div[2]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(7))
    #     # 水卡号
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[14]/div[3]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(8))
    #     # 电卡号
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[14]/div[4]/div/div/div/div/input'))).send_keys(yu_ruan_common.free_random_many_num(8))



    # 填写物品管理页面
    def test_write_Item_information(self):
        ''' 进入物品管理页面 '''
        time.sleep(2)

        bill_preview_show_title = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/button/span'))).text
        print(bill_preview_show_title)
        assert bill_preview_show_title == "添加", f"{self.logger.error('断言失败：未进入物品登记页面！')}"
        self.logger.info('断言成功：已进入物品登记页面！')

        # 删除物品按钮点击
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td[7]/div/i'))).click()
        # 点击下一步
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[3]/button[2]'))).click()
        time.sleep(3)

    # 账单明细页面
    def test_Read_bills_information(self):
        ''' 进入账单明细页面 '''
        time.sleep(2)
        # 断言账单是否成功生成
        bill_show_title = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[4]/div[2]/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div'))).text
        assert bill_show_title == "1", f"{self.logger.error('断言失败：未进入账单预览页面！或没有生成账单')}"
        self.logger.info('断言成功：已进入账单预览页面！且成功生成账单。')

        # 点击下一步按钮
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[4]/div[3]/button[2]'))).click()
        time.sleep(3)

    # 上传合同信息 并提交初审
    def test_upload_contract_information(self):
        ''' 上传合同信息 提交初审 '''
        upload_the_contract_title = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[2]/div[1]/span'))).text
        assert upload_the_contract_title == "上传照片", f"{self.logger.error('断言失败：未进入上传合同页面！')}"
        self.logger.info('断言成功：已进入上传合同页面！')

        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/div[1]/div/div[1]/div/input'))).send_keys(rf"F:\photo\{self.common_utill.free_random_one_num(1,4)}.jpg")

        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/div[2]/div/div[1]/div/input'))).send_keys(rf"F:\photo\{self.common_utill.free_random_one_num(1,4)}.jpg")

        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/div[3]/div/div[1]/div/input'))).send_keys(rf"F:\photo\{self.common_utill.free_random_one_num(1,4)}.jpg")

        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/div[4]/div/div[1]/div/input'))).send_keys(rf"F:\photo\{self.common_utill.free_random_one_num(1,4)}.jpg")

        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[3]/button[2]'))).click()

        add_prompt_landlord_success = self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/p'))).text

        assert add_prompt_landlord_success == "保存成功", f"{self.logger.error('断言失败：登记房东失败！')}"
        self.logger.info('断言成功：登记房东成功！')

    @classmethod
    def tearDownClass(cls):
        time.sleep(8)
        # 关闭浏览器对象
        cls.driver.quit()
