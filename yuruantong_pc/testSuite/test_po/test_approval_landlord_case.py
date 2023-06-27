# coding:utf-8
import time
import allure
import pytest
from nb_log import LogManager

from yuruantong_pc.pageObjects.login_page.login_page import LoginPage
from yuruantong_pc.pageObjects.main_page.search_page import SearchPage
from yuruantong_pc.pageObjects.menu_page.menu_page import MenuPage
from yuruantong_pc.pageObjects.wholeTenement_page.go_to_page import goToPage
from yuruantong_pc.pageObjects.wholeTenement_page.landlord_page import LandlordPage


@allure.epic('登记房东审批')
@allure.feature('获取审批列表中的房东数据进行审批')
@allure.suite('登记房东')
class TestApprovalLandlordCase():
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.logger = LogManager('登记房东').get_logger_and_add_handlers(10, log_filename='登记房东01.log')
        self.menu_page = MenuPage()
        self.go_to_page = goToPage()
        self.landlord_page = LandlordPage()
        self.login_page = LoginPage()
        self.search_page = SearchPage()

    def tear_down_class(self):
        pass

    @pytest.mark.skip("登记房东时已经获取页面token,无需再次登录")
    @pytest.mark.mark_name("回归测试")
    @allure.description("输入账号密码进行登录-登陆后跳转至首页面")
    @allure.story("输入账号密码进行登录")
    @pytest.mark.run(order=1)
    def test_login_case(self):
        """ 登录 """
        self.login_page.to_login_page()
        # 执行登录操作
        self.login_page.login('18196627126', 'aaaa123456')
        time.sleep(3)
        self.logger.info('登录成功')

    @pytest.mark.skip("没有在首页页面，无需执行次操作")
    @allure.story("点击一级审批列表")
    @pytest.mark.run(order=2)
    @allure.description("点击审批，展开二级菜单")
    def test_click_approval_button(self):
        self.menu_page.click_approval_button()
        self.logger.info("点击一级审批列表")

    @pytest.mark.skip("没有在首页页面，无需执行次操作")
    @allure.story("点击房东审批")
    @allure.description("点击房东审批")
    @pytest.mark.run(order=3)
    def test_click_landlord_approval_button(self):
        self.menu_page.click_landlord_approval_button()
        self.logger.info("点击房东审批")

    @allure.story("跳转房东审批子页面")
    @allure.description("跳转房东审批子页面")
    @pytest.mark.run(order=4)
    def test_go_to_approval_landlord(self):
        self.go_to_page.go_to_approval_landlord()
        self.logger.info("跳转房东审批子页面")

    @pytest.mark.skip("没有在首页页面，无需执行次操作")
    @allure.story("查询房东审批状态")
    @pytest.mark.run(order=5)
    def test_landlord_approval_status_search(self):
        self.search_page.landlord_approval_status_search()
        time.sleep(3)

    @allure.story("进行房东审批")
    @allure.description("进行房东审批")
    @pytest.mark.run(order=6)
    def test_landlord_approval(self):
        self.landlord_page.landlord_approval()
        time.sleep(3)


if __name__ == '__main__':
    pytest.main(['-vs', '--reruns=3'])
