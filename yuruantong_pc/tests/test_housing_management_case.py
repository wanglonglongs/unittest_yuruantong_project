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


class wholeManagementCase(unittest.TestCase):

    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        # 创建Chrome浏览器对象
        cls.driver.maximize_window()
        cls.element_locator_yaml = '../configs/element_locator/fang_dong_login.yaml '
        cls.element = YamlHelper.read_yaml(cls.element_locator_yaml)
        cls.wait = WebDriverWait(cls.driver, 10, poll_frequency=0.5)
        cls.logger = LogManager('登记房东').get_logger_and_add_handlers(10,log_filename='登记房东.log')
        cls.common_utill = yu_ruan_common

    @Screen(driver=driver)
    def test_1_case_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)

        # 调用login()方法
        login_page.login("18196627126","aaaa123456")
        # logger.info('登录成功')

        self.logger.info("登录寓软通账号成功 -success")

    @Screen(driver=driver)
    def test_2_case_openTag_page(self):
        # 点击菜单选项栏-房源
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.element["MENU_HOUSING_RESOURCES"]))).click()
        time.sleep(2)

        # 点击二级菜单按钮-整租管理
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH,self.element["MENU_WHOLE_MANAGEMENT"]))).click()

        # 验证当前已经打开整租页标签
        jump_housing_results = self.wait.until(EC.presence_of_element_located((By.XPATH,self.element["TAG_NAME_WHOLE_MANAGEMENT"]))).get_attribute('text')
        self.assertEqual("整租管理" in jump_housing_results, True)
        self.logger.info("打开整租管理页面成功 -success")
        # 重新进入整租页面中
        self.driver.get('http://test.yuruantong.com/amp/wholeTenement/')

    @Screen(driver=driver)
    def test_3_case_pen_register_landlord(self):
        # 进入登记房东整租页面 点击登记房东按钮
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/button[1]/span'))).click()
        self.logger.info("进入登记房东页面成功 -success")
    # 填写登记基本信息
    @Screen(driver=driver)
    def test_4_case_write_basic_information(self):

        # 所属店面选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div/div/div/div/input'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div/div/div/div/input'))).send_keys("金中环")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[1]'))).click()

        # 店面下拉选择
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[14]/div[1]/div[1]/ul/li[1]'))).cllick()
        # 座幢填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[3]/div/div/div/div[1]/input'))).send_keys("1")

        # 单元填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[3]/div/div/div/div[2]/input'))).send_keys("1")
        time.sleep(2)
        # 门牌号填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[4]/div/div/div/div/input'))).send_keys(self.common_utill.free_random_many_num(6))

        # 物业地址选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[7]/div/div/div/div/div[1]/input'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[7]/div/div/div/div/div[1]/input'))).send_keys('包河万达')
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[1]'))).click()

        # 物业地址下拉选择
        # self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div:nth-child(18) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span'))).click()

        # 建筑面积填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[8]/div/div/div/div[1]/div/input'))).send_keys("1521")

        # 房屋类型选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[9]/div/div/div/div[1]/input'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[9]/div/div/div/div[1]/input'))).send_keys("大三房")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[1]'))).click()

        # # 房屋类型下拉选择
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[14]/div[1]/div[1]/ul/li[1]'))).click()

        # # 装修程度选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[10]/div/div/div/div/div[1]/input'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[10]/div/div/div/div/div[1]/input'))).send_keys("毛坯")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[1]'))).click()

        # # 装修程度下拉选择
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[10]/div/div/div/div/div[1]/input'))).click()

        # 所在楼层填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[11]/div/div/div/div[1]/input'))).send_keys("1")

        # 总楼层填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[11]/div/div/div/div[2]/input'))).send_keys("15")

        # 朝向选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[12]/div/div/div/div/div[1]/input'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[12]/div/div/div/div/div[1]/input'))).send_keys("朝南")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[1]/div[1]/ul/li[1]'))).click()

        # # 朝向下拉选择
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[1]/div[1]/ul/li[1]'))).click()
        self.logger.info("房东基本信息填写 -success")

    # # 填写登记房东信息
    @Screen(driver=driver)
    def test_5_case_write_landlord_information(self):
        # 填写房东姓名
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[1]/div/div/div/div/input'))).send_keys("房东姓名")
        # 选择证件类型
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/div[1]/div[1]/input'))).click()
        # 选择证件类型下拉选
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[7]/div[1]/div[1]/ul/li[2]/span'))).click()
        # 证件号码填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/div[2]/input'))).send_keys("42098419940501751X")
        # 手机号码填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[3]/div/div/div/div/input'))).send_keys(self.common_utill.random_create_phone())
        # 收款人姓名
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[4]/div/div/div/div/input'))).send_keys("张三")
        # 银行卡卡号填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[6]/div/div/div/div/input'))).send_keys("6214835400894513")
        # 收款身份证填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[7]/div/div/div/div/input'))).send_keys("42098419940501751X")
        # 收款人手机号填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[8]/div/div/div/div/input'))).send_keys(self.common_utill.random_create_phone())
        # 渠道来源选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[9]/div/div/div/div/div[1]/input'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[9]/div/div/div/div/div[1]/input'))).send_keys("网上联系")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[7]/div[1]/div[1]/ul/li[1]'))).click()
        # 渠道来源下拉选择
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[8]/div[1]/div[1]/ul/li[1]'))).click()
        # 房东包物业 选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[10]/div/div/div/div[1]/div/input'))).click()
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[8]/div[1]/div[1]/ul/li[2]/span'))).click()
        # 房东包物业下拉选择
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[9]/div[1]/div[1]/ul/li[2]'))).click()
        # 房东包物业 金额填写
        # self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[4]/div[10]/div/div/div/div[2]/input'))).send_keys("50")
        self.logger.info("房东信息填写成功 -success")

    # 填写托管房东信息
    @Screen(driver=driver)
    def test_6_case_write_trusteeship_information(self):
        # 开始时间
        # 结束时间
        # 合同期限按钮点击 3年
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[3]/div/div/div/span[1]'))).click()
        # 缴费方式
        # 收房价格填写
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[5]/div/div/div/input'))).send_keys("1500")
        # 房屋押金点击押一
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[6]/div/div/div/span'))).click()
        # 维修方案选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[7]/div/div/div/div/div[1]/input'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[7]/div/div/div/div/div[1]/input'))).send_keys("房东承担")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[9]/div[1]/div[1]/ul/li[1]'))).click()
        # 维修方案下拉选择
        #self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[9]/div[1]/div[1]/ul/li[1]'))).click()

        # 装修方案选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[8]/div/div/div/div/div[1]/div[1]/input'))).click()
        time.sleep(3)
        # 装修方案下拉选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[10]/div[1]/div[1]/ul/li[1]'))).click()
        # 首次付款日期选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[9]/div/div/div/div/input'))).click()
        time.sleep(2)
        # 首次付款日期下拉选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[11]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[5]'))).click()
        # 业务人员选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[10]/div/div/div/div/div[1]/input'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[10]/div/div/div/div/div[1]/input'))).send_keys()
        time.sleep(3)
        # 业务人员下拉选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[12]/div[1]/div[1]/ul/li[1]'))).click()
        # 协助人员选择
        # 累计免租期选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/div[12]/div/div/div/div/div/div[1]/div/div[1]/input'))).click()
        time.sleep(3)
        # 累计免租期下拉选择
        self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[13]/div[1]/div[1]/ul/li[1]/span'))).click()
        # 点击下一步
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[3]/button[2]'))).click()
        time.sleep(3)
        self.logger.info("托管信息填写成功 -success")

    # 填写物品管理页面
    @Screen(driver=driver)
    def test_7_case_write_Item_information(self):

        # 删除物品按钮点击
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td[7]/div/i'))).click()
        # 点击下一步
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[3]/button[2]'))).click()
        self.logger.info("物品管理页面 -success")

    # 账单明细页面
    @Screen(driver=driver)
    def test_8_case_Read_bills_information(self):
        # 点击下一步按钮
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[4]/div[3]/button[2]'))).click()
        self.logger.info("账单信息页面 -success")

    # 上传合同信息 并提交初审
    @Screen(driver=driver)
    def test_9_case_upload_contract_information(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/div[1]/div/div[1]/div/input'))).send_keys("C:/Users/admin\Desktop\image/tu-01.png")

        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[2]/div[2]/div[2]/div/div[1]/div/input'))).send_keys("C:/Users/admin\Desktop\image/tu-01.png")

        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div[3]/button[2]'))).click()

        time.sleep(5)
        self.logger.info("登记房东初审成功-success")
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器对象
        cls.driver.quit()
