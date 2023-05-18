
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yuruantong_pc.common.yaml_helper import YamlHelper


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.element_locator_yaml = '../configs/element_locator/fang_dong_login.yaml'
        self.element = YamlHelper.read_yaml(self.element_locator_yaml)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=0.5)

    def login(self, username, password):
        # 打开网页
        self.driver.get("http://test.yuruantong.com/amp/#/login?redirect=/index")
        # 输入账号
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.element["SHOU_YE_ACCOUNT"]))).send_keys(username)
        # 输入密码
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.element["SHOU_YE_PASSWORD"]))).send_keys(password)
        # 登录
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.element["SHOU_YE_LOGIN_BUTTON"]))).click()
