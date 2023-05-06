"""
驱动模块
    1、考虑到浏览器的兼容性，可以分为主流的几个浏览器驱动
        1、谷歌
        2、火狐
        3、其他
"""

from selenium import webdriver
from yuruantong_pc.configs.config import implicitly_wait_time

# 设置单例模式
'''
类创建实例：
    1、先调用—__new__()创建方法，一般类中不写，自动调用
    2、再调用初始化方法__init__()
  判断一个类是否有实例，如果有，就不会创建新的实例  
'''


# 哪一个类的实例需要使用单例模式，就直接继承这个类（`固定写法`）
class Single(object):
    # new方法创建对象
    def __new__(cls, *args, **kwargs):
        # 判断当前的类是否已经实例化
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)  # super是父类的new方法
        return cls._instance


class Driver(Single):
    # 新建一个初始值
    _driver = None

    # 判断使用浏览器,---------默认指定谷歌浏览器
    def get_driver(self, browser_name='chrome'):
        if self._driver is None:
            if browser_name == "chrome":
                self._driver = webdriver.Chrome()
            elif browser_name == "firefox":
                self._driver = webdriver.Firefox()
            else:
                raise (f"没有这个{browser_name}浏览器，请使用可用浏览器打开")
            # 设置隐式等等时间---设置`**全局变量`**等等时间5s
            self._driver.implicitly_wait(implicitly_wait_time)
            # 浏览器对大化
            self._driver.maximize_window()
        return self._driver  # 返回浏览器对象


if __name__ == '__main__':
    Driver().get_driver('chrome')  # 创建实例对象，调用对应的方法,传什么浏览器使用什么浏览器

