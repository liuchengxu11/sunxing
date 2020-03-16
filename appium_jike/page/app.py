import datetime

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from Config.Config import app_driver
from appium_jike.page.home_page import Home_page
"""
查找app包的命令 adb shell dumpsys window windows | grep -E 'mCurrentFocus|FocusedApp'

adb shell pm clear包名  清理包的缓存数据  
"""

class App():
    driver: WebDriver = None
    @classmethod
    def app(cls):
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", app_driver)
        cls.driver.implicitly_wait(10)
        return Home_page(cls.driver)



    @classmethod
    def quit(cls):
        cls.driver.quit()
