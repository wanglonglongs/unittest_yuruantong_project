from yuruantong_pc.common.myDriver import Driver
import time
import os.path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from yuruantong_pc.configs.config import wait_timeout, wait_poll_frequency


class BasePage:
    def __init__(self):  # 调用basepage 需要的浏览器对象，默认谷歌浏览器
        self._driver = Driver().get_driver()

    # ----------------------封装页面操作------------------------
    # -1
    def click_js(self, locator,action=None):
        time.sleep(1)
        self._driver.execute_script(locator)

    # 0 , 封裝上傳照片-操作
    def upload_picture(self, locator,text, action=None):
        '''
            :param locator: 元素定位： locator定义为包含-元素定位方法-和-定位方式-的包 ----['id','name']
            :param text: 输入文本的内容
            :param action: 执行的动作描述,缺省参数
        '''
        # 1,元素定位
        element = self._driver.find_element(*locator)
        # 2,上傳圖片
        element.send_keys(text)

    # 1、封装-输入-操作
    def input_text(self, locator, text, action=None):
        '''

        :param locator: 元素定位： locator定义为包含-元素定位方法-和-定位方式-的包 ----['id','name']
        :param text: 输入文本的内容
        :param action: 执行的动作描述,缺省参数

        '''
        # 1、元素定位
        # find_element(定位方式，定位表达式)
        element = self._driver.find_element(*locator)  # "*"号解包
        # 2、很多输入框有默认提示文本，需要先清除
        element.clear()
        # 3、输入值
        element.send_keys(text)

    # 2、封装-点击-操作
    def click(self, locator, action=None):
        # 1、元素定位
        # find_element(定位方式，定位表达式)
        element = self.element_is_visibility(locator)  # "*"号解包
        # 2、点击
        element.click()

    # 3、封装-清空-操作
    def clear(self, locator, action=None):
        # 1/元素定位
        element = self._driver.find_element(*locator)
        # 2/清空
        element.clear()

    # 4、封装 -获取文本内容-操作
    def get_text(self, locator, action=None):
        return WebDriverWait(
            self._driver,
            timeout=wait_timeout,
            poll_frequency=wait_poll_frequency).until(
            EC.visibility_of_element_located(locator)).text

    # ----------------------可见元素且是可点击的-----------------
    def element_is_clickable(
            self,
            locator,
            action=None,
            timeout=5,
            poll_frequency=0.5):
        # 1/设置显式等待可见元素定位时间
        try:
            ele = WebDriverWait(
                self._driver,
                timeout=timeout,
                poll_frequency=poll_frequency).until(
                # 判断元素是否可点击执行定位
                EC.element_to_be_clickable(locator))
        except BaseException:
            raise
        # 如果存在返回元素本身
        return ele

        # ----封装显式等待---判断元素是否存在，如果没有获取到元素，使用显示等待判断----日志及截图-------

    def element_is_presence(
            self,
            locator,
            action=None,
            timeout=5,
            poll_frequency=0.5):
        '''

        :param locator: 定位元素和定位方法和表达式，包（'',''）
        :param action: 动作描述，
        :param timeout: 等待时间设置
        :param poll_frequency: 等待频率
        '''
        # 1/设置显式等待时间
        try:
            WebDriverWait(
                self._driver,
                timeout=timeout,
                poll_frequency=poll_frequency).until(
                EC.presence_of_element_located(locator))
        except BaseException:
            # 3/元素不存在返回False
            return False
        # 如果存在返回True
        return True

    def element_is_visibility(
            self,
            locator,
            action=None,
            timeout=10,
            poll_frequency=0.5):
        # 1/设置显式等待可见元素定位时间
        try:
            ele = WebDriverWait(
                self._driver,
                timeout=timeout,
                poll_frequency=poll_frequency).until(
                # 判断元素是否可见再执行定位
                EC.visibility_of_element_located(locator))
        except BaseException:
            raise
        # 如果存在返回元素本身
        return ele
