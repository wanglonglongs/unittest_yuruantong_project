# coding:utf-8
import time
import allure
import pytest
from nb_log import LogManager
from yuruantong_pc.pageObjects.login_page.login_page import LoginPage
from yuruantong_pc.pageObjects.wholeTenement_page.landlord_page import LandlordPage
from yuruantong_pc.pageObjects.menu_page.menu_page import MenuPage
from yuruantong_pc.pageObjects.wholeTenement_page.go_to_page import goToPage
from yuruantong_pc.common.packaging_methon import yu_ruan_common


@allure.suite('登记房东')
@allure.epic('登记房东')
@allure.feature('包含账号登录-房东登记流程-并且发起初审')
class TestRegisterLandlordCase():
    """   登记房东    """
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.login_page = LoginPage()
        # 创建MenuPage对象
        self.menu_page = MenuPage()
        self.landlord_page = LandlordPage()
        self.go_to_page = goToPage()
        self.logger = LogManager('登记房东').get_logger_and_add_handlers(10, log_filename='登记房东01.log')

    def tear_down_class(self):
        pass

    @pytest.mark.mark_name("回归测试")
    @allure.description("输入账号密码进行登录-登陆后跳转至首页面")
    @allure.story("输入账号密码进行登录")
    @pytest.mark.run(order=1)
    def test_login_case(self):
        """ 登录 """
        # 打开登录页面
        self.login_page.to_login_page()
        # 执行登录操作
        LoginPage().login('18196627126','aaaa123456')
        time.sleep(3)
        self.logger.info('登录成功')

    @allure.story("点击房源按钮打开二级菜单")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("点击房源按钮打开二级菜单")
    @pytest.mark.run(order=2)
    def test_click_house_resources_button(self):
        """ 点击房源按钮 """
        self.menu_page.click_house_resources_button()
        time.sleep(3)

    @allure.story("点击整租按钮进入整租")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("点击二级子菜单打开整租标签页")
    @pytest.mark.run(order=3)
    def test_click_whole_management_button(self):
        """ 点击整租按钮 """
        self.menu_page.click_whole_management_button()
        time.sleep(3)

    @allure.story("跳转整租子页面")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("跳转整租子页面，绕过shadow-dom操纵元素")
    @pytest.mark.run(order=4)
    def test_go_to_whole_management(self):
        """ 跳转整租子页面 """
        self.go_to_page.go_to_whole_management()
        time.sleep(4)

    @allure.story("点击房东按钮")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("点击登记房东按钮,进入房东登录业务流程页面")
    @pytest.mark.run(order=5)
    def test_click_landlord_button(self):
        """ 点击房东按钮 """
        # 点击登记房东按钮
        self.landlord_page.click_landlord_button()
        time.sleep(4)

    @allure.story("输入房东基本信息")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("填写房东基本信息内容")
    @pytest.mark.run(order=6)
    def test_landlord_base_info_input(self):
        """ 输入房东基本信息 """
        buildingNumber = 'B'
        unitNumber = "1"
        houseNumber = f'{yu_ruan_common.free_random_many_num(5)}'
        buildingArea = '510'
        floor = '5'
        allFloor = '20'
        self.landlord_page.landlord_base_info(buildingNumber,unitNumber,houseNumber,buildingArea,floor,allFloor)

    @allure.story("输入房东详细信息")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("填写房东详细信息内容")
    @pytest.mark.run(order=7)
    def test_landlord_info_input(self):
        """ 输入房东详细信息 """
        landlordName = '张三'
        idNumber = '42098419940501751X'
        iphoneNumber = '15893281069'
        payeeName = "李四"
        bankCardsNumber = '6214835400894513'
        payeeIdNumber = '42098419940501751X'
        payeePhoneNumber = '15893281068'
        self.landlord_page.landlord_info(landlordName,idNumber,iphoneNumber,payeeName,bankCardsNumber,payeeIdNumber,payeePhoneNumber)
        time.sleep(2)

    @allure.story("输入托管信息")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("填写输入托管信息内容")
    @pytest.mark.run(order=8)
    def test_trusteeship_info(self):
        """ 输入托管信息 """
        housePrice = '100'
        remark = '托管'
        self.landlord_page.trusteeship_info(housePrice,remark)

    @allure.story("点击下一步")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("点击下一步按钮跳转物品登记信息页面")
    @pytest.mark.run(order=9)
    def test_click_landlord_next_btn(self):
        """ 点击下一步跳转物品登记信息页面 """
        self.landlord_page.click_landlord_next_btn()

    @allure.story("添加物品信息")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("录入物品信息")
    @pytest.mark.run(order=10)
    def test_item_information(self):
        """ 添加物品信息 """
        itemRemark = "登记物品登记物品"
        itemNumber = "1"
        # itemImage = rf"F:\photo\1.jpg"
        self.landlord_page.item_information(itemNumber,itemRemark)

    @allure.story("点击下一步")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("点击下一步跳转预览账单页面")
    @pytest.mark.run(order=11)
    def test_click_item_next_btn(self):
        """ 点击下一步跳转预览账单页面 """
        self.landlord_page.click_item_next_btn()
        time.sleep(5)

    @allure.story("点击下一步")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("点击下一步跳转上传合同页面")
    @pytest.mark.run(order=12)
    def test_click_bill_next_btn(self):
        """ 点击下一步跳转上传合同页面 """
        self.landlord_page.click_bill_next_btn()

    @allure.story("上传合同信息")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("上传合同合同信息")
    @pytest.mark.run(order=13)
    def test_upload_contract(self):
        """ 上传合同 """
        titleDeeds = rf"F:\photo\1.jpg"
        identityCard = rf"F:\photo\2.jpg"
        entrustment = rf"F:\photo\3.jpg"
        originalHouse = rf"F:\photo\4.jpg"
        self.landlord_page.upload_contract(titleDeeds,identityCard,entrustment,originalHouse)

    @allure.story("提交初审")
    @pytest.mark.mark_name(regression="回归测试")
    @allure.description("进行初审，初审后需要进行审批操作")
    @pytest.mark.run(order=14)
    def test_submit_first_review_btn(self):
        """ 点击提交第一次审核 """
        self.landlord_page.submit_first_review_btn()
        time.sleep(8)


if __name__ == '__main__':
    pytest.main(['-vs','--reruns=3', '--reruns-delay=3' , 'test_register_landlord_case.py'])

