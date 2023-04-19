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
import random
from nb_log import get_logger


class wholeManagementCase(unittest.TestCase):

    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        # 创建Chrome浏览器对象
        cls.driver.maximize_window()
        cls.element_locator_yaml = '../configs/element_locator/fang_dong_login.yaml '
        cls.element = YamlHelper.read_yaml(cls.element_locator_yaml)
        cls.wait = WebDriverWait(cls.driver, 10, poll_frequency=0.5)
        cls.logger = get_logger('登记房东')

    @Screen(driver=driver)
    def test_login_yuRuanTong(self):
        # 创建LoginPage对象
        login_page = LoginPage(self.driver)

        # 调用login()方法
        login_page.login("18196627126","aaaa123456")
        # logger.info('登录成功')

        self.logger.info("登录寓软通账号成功")

    @Screen(driver=driver)
    def test_openTag_page(self):
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
        self.logger.info("打开整租管理页面成功")

    @Screen(driver=driver)
    def test_pen_register_landlord(self):
        time.sleep(2)
        # 通过JS代码定位并点击元素 [点击登记房东]
        register_landlord = self.element["REGISTER_LANDLORD_JS"]
        self.driver.execute_script(register_landlord)

        # 校验是否已在登记[房东页面]
        basic_information_js = self.element["FANG_DONG_PAGE_BASE"]
        basic_information_result = self.driver.execute_script(basic_information_js)

        # 文字判断是否出现 [基本信息]
        self.assertEqual("基本信息" in basic_information_result, True)
        time.sleep(2)

        self.logger.info("打开登录房东页面成功")

    @Screen(driver=driver)
    def test_register_landlord_information(self):
        # 所属店面下拉展开
        select_shopfront_option = self.element["FANG_DONG_SHOP_FRONT"]
        self.driver.execute_script(select_shopfront_option)
        time.sleep(2)
        # 随机选取店面子级元素

        dian_mian_random = random.randint(1,21)

        # shopfront_value = self.element["FANG_DONG_SHOP_FRONT_NODES"]
        shopfront_value = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > ' \
                          f'wujie-app").shadowRoot.querySelector("body > div.el-select-dropdown.el-popper > ' \
                          f'div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(' \
                          f'{dian_mian_random})").click()'
        self.driver.execute_script(shopfront_value)

        # 生成随机字母
        def get_random_letter():
            return chr(random.randint(65, 90))

        # 座幢写入
        input_block_number = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div.registerTenlentStyle > div > div:nth-child(2) > div.formStyle > form > div:nth-child(2) > div.el-col.el-col-24.el-col-lg-10.el-col-xl-6 > div > div > div > div:nth-child(1) > input").value = "{get_random_letter()}" '
        self.driver.execute_script(input_block_number)

        # 单元写入
        input_unit_number = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div.registerTenlentStyle > div > div:nth-child(2) > div.formStyle > form > div:nth-child(2) > div.el-col.el-col-24.el-col-lg-10.el-col-xl-6 > div > div > div > div:nth-child(2) > input").value = "{dian_mian_random}" '
        self.driver.execute_script(input_unit_number)

        # 门牌号写入
        input_house_number = f'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div.registerTenlentStyle > div > div:nth-child(2) > div.formStyle > form > div:nth-child(2) > div:nth-child(4) > div > div > div > div.el-input.el-input--small.el-input--suffix > input").value = "{dian_mian_random}" '
        self.driver.execute_script(input_house_number)
        # 物业地址选择
        select_property_address = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section ' \
                                  '> div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > ' \
                                  'div.registerTenlentStyle > div > div:nth-child(2) > div.formStyle > form > ' \
                                  'div:nth-child(2) > div:nth-child(7) > div > div > div > div > ' \
                                  'div.el-input.el-input--small.el-input--suffix > input").click()'
        self.driver.execute_script(select_property_address)

        # click1 = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul").click()'
        # self.driver.execute_script(click1)
        #
        # property_address_value = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item.selected.hover > span").click()'
        # self.driver.execute_script(property_address_value)

        # # 建筑面积
        # input_build_area = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > ' \
        #                    'wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > ' \
        #                    'div.registerTenlentStyle > div > div:nth-child(2) > div.formStyle > form > div:nth-child(' \
        #                    '2) > div:nth-child(8) > div > div > div > div.el-col.el-col-10 > div > input").value = ' \
        #                    '"150" '
        # self.driver.execute_script(input_build_area)
        # # 房屋类型
        # select_house_type = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > div.registerTenlentStyle > div > div:nth-child(2) > div.formStyle > form > div:nth-child(2) > div:nth-child(9) > div > div > div > div > input").click()'
        # self.driver.execute_script(select_house_type)
        # time.sleep(2)
        # house_type_value = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > wujie-app").shadowRoot.querySelector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item.hover").click()'
        #
        # self.driver.execute_script(house_type_value)
        #
        # # 装修程度
        #
        # select_decoration_level = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section ' \
        #                           '> div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > ' \
        #                           'div.registerTenlentStyle > div > div:nth-child(2) > div.formStyle > form > ' \
        #                           'div:nth-child(2) > div:nth-child(10) > div > div > div > div > ' \
        #                           'div.el-input.el-input--small.el-input--suffix > input").click()'
        # self.driver.execute_script(select_decoration_level)
        # decoration_level_value = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > ' \
        #                          'div > wujie-app").shadowRoot.querySelector("body > div.el-select-dropdown.el-popper ' \
        #                          '> div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ' \
        #                          'li:nth-child(1) > span").click()'
        # self.driver.execute_script(decoration_level_value)
        # # 楼层
        # input_place_storey = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div ' \
        #                      '> wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > ' \
        #                      'div.registerTenlentStyle > div > div:nth-child(2) > div.formStyle > form > ' \
        #                      'div:nth-child(2) > div:nth-child(11) > div > div > div > div:nth-child(1) > ' \
        #                      'input").value = "12" '
        # self.driver.execute_script(input_place_storey)
        # input_all_storey = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > div > ' \
        #                    'wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > ' \
        #                    'div.registerTenlentStyle > div > div:nth-child(2) > div.formStyle > form > div:nth-child(' \
        #                    '2) > div:nth-child(11) > div > div > div > div:nth-child(3) > input").value = "25" '
        # self.driver.execute_script(input_all_storey)
        # # 朝向
        # select_open_direction = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > ' \
        #                         'div > wujie-app").shadowRoot.querySelector("#app > div > div:nth-child(2) > ' \
        #                         'div.registerTenlentStyle > div > div:nth-child(2) > div.formStyle > form > ' \
        #                         'div:nth-child(2) > div:nth-child(12) > div > div > div > div > ' \
        #                         'div.el-input.el-input--small.el-input--suffix > input").click() '
        # self.driver.execute_script(select_open_direction)
        # time.sleep(2)
        # open_direction_value = 'document.querySelector("#mainDiv > div > div.hasTagsView.main-container > section > ' \
        #                        'div > wujie-app").shadowRoot.querySelector("body > div:nth-child(5) > ' \
        #                        'div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ' \
        #                        'li:nth-child(1) > span").click() '
        # self.driver.execute_script(open_direction_value)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        # 关闭浏览器对象
        cls.driver.quit()
