# coding:utf-8
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yuruantong_pc.common.yaml_helper import YamlHelper
from yuruantong_pc.common.packaging_methon.yu_ruan_login import LoginPage
import random
from yuruantong_pc.common.error_screenshot import Screen
import string
import datetime
from nb_log import get_logger


class registeredTenantCase(unittest.TestCase):
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
        cls.logger = get_logger('登记房东')

    @Screen(driver=driver)
    def test_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)

        # 调用login()方法
        login_page.login("18196627126", "aaaa123456")
        self.logger.info("登记租客成功")

    @Screen(driver=driver)
    def test_openTag_page(self):
        # 点击菜单选项栏-房源
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.element["MENU_HOUSING_RESOURCES"]))).click()
        time.sleep(2)

        # 点击二级菜单按钮-整租管理
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.element["MENU_WHOLE_MANAGEMENT"]))).click()

        # 验证当前已经打开整租页标签
        jump_housing_results = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.element["TAG_NAME_WHOLE_MANAGEMENT"]))).get_attribute('text')
        self.assertEqual("整租管理" in jump_housing_results, True)

        time.sleep(3)

    # 租赁状态 未租选择
    @Screen(driver=driver)
    def test_zuLinStatus(self):
        # 租赁状态下拉
        lease_status = self.element_whole["LEASE_STATUS"]
        self.driver.execute_script(lease_status)

        # 未租下拉选择
        lease_status_choose = self.element_whole["LEASE_STATUS_CHOOSE"]
        self.driver.execute_script(lease_status_choose)

        # 搜索
        search = self.element_whole["LEASE_STATUS_SEARCH"]
        self.driver.execute_script(search)
        time.sleep(3)

        # 点击登记租客
        check_tenant = self.element_whole["REGISTER_TENANT_BUTTON"]
        self.driver.execute_script(check_tenant)
        time.sleep(1)

        # 随机生成 某区间 内的任意一个整数
        def free_random_one_num(start_num, end_num):
            return random.randint(start_num, end_num)

        # 随机生成X位字符 纯数字
        def free_random_many_num(num_sign):
            return "".join(map(lambda x:random.choice(string.digits), range(num_sign)))

        # 随机生成X位字符 纯字母
        def random_string_generator(num_sign):
            random_char = random.sample(string.ascii_letters, num_sign)
            return ''.join(random_char)
            # now_date = str(datetime.date.today())
            # return ''.join(random_char) + now_date

        # 随机生成X位字符 字母+数字组合
        def random_string_number(n):
            m = random.randint(1, n)
            a = "".join([str(random.randint(0, 9)) for _ in range(m)])
            b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
            return ''.join(random.sample(list(a + b), n))

        print(string.digits+string.ascii_letters+string.punctuation)

        # 随机生成手机号 暂只对第二位做要求
        def random_create_phone():
            # 第二位数字
            second = [3, 4, 5, 6, 7, 8][random.randint(0, 4)]
            # 最后九位数字
            suffix = random.randint(99999999, 1000000000)
            # 拼接手机号
            return "1{}{}".format(second, suffix)
        print(random_create_phone())

        # 租客姓名
        tenant_name = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > ' \
                      f'wujie-app").shadowRoot.querySelector("#app > div > ' \
                      f'div:nth-child(2) > div > div.registerTenlentStyle > div > div.container > div.formStyle > ' \
                      f'form > div:nth-child(4) > div:nth-child(1) > div > ' \
                      f'div > div > div > input").value = "{random_string_number(free_random_one_num(8,10))}" '
        self.driver.execute_script(tenant_name)

        # 证件选择（要先点开下拉框 再去选择）
        identity_card_input = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > ' \
                               f'div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div > ' \
                               f'div.registerTenlentStyle > div > div.container > div.formStyle > form > ' \
                               f'div:nth-child(4) > div:nth-child(2) > div > div.el-select.el-select--medium > div > ' \
                               f'input").click()'
        self.driver.execute_script(identity_card_input)

        # 默认台胞证
        identity_card_choose = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > ' \
                                f'div > wujie-app").shadowRoot.querySelector("body > div.el-select-dropdown.el-popper ' \
                                f'> div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ' \
                                f'li:nth-child({free_random_one_num(3,3)}) > span").click()'
        self.driver.execute_script(identity_card_choose)

        # 证件号码 台胞证>8位
        identity_card = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > ' \
                        f'wujie-app").shadowRoot.querySelector("#app > div > ' \
                        f'div:nth-child(2) > div > div.registerTenlentStyle > div > div.container > div.formStyle > ' \
                        f'form > div:nth-child(4) > div:nth-child(2) > div > ' \
                        f'div.el-input.el-input--medium > input").value = "{random_string_generator(free_random_one_num(8,11))}"'
        self.driver.execute_script(identity_card)

        # 联系电话
        phone = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > ' \
                       f'wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div > ' \
                       f'div.registerTenlentStyle > div > div.container > div.formStyle > form > div:nth-child(4) > ' \
                       f'div:nth-child(3) > div > div > div > div > input").value = "{random_create_phone()}"'
        self.driver.execute_script(phone)

        # 紧急联系电话
        urgency_phone = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > ' \
                        f'wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div > ' \
                        f'div.registerTenlentStyle > div > div.container > div.formStyle > form > div:nth-child(4) > ' \
                        f'div:nth-child(4) > div > div > div > div > input").value = "{random_create_phone()}"'
        self.driver.execute_script(urgency_phone)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        # 关闭浏览器对象
        cls.driver.quit()
