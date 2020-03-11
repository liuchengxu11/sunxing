from appium import webdriver
import time
import pytest

from selenium.webdriver.support.wait import WebDriverWait
"""
adb shell dumpsys window windows | grep -E 'mCurrentFocus|FocusedApp'
"""

class AppiumTest():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['appPackage'] = 'com.tencent.mm'
        # desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['appPackage'] = 'com.ss.android.article.news'
        desired_caps['appActivity'] = 'com.ss.android.article.news.activity.MainActivity'
        # appium提供的一种输入法，可以传中文。测试时直接用这个输入法
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"  # 程序结束时重置原来的输入法
        desired_caps["noReset"] = "True"  # 不初始化手机app信息（类似不清楚缓存）
        desired_caps['automationName'] = 'appium'
        desired_caps['deviceName'] = 'QDY4C17807005548'
        desired_caps['platformVersion'] = '7.0'

        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        time.sleep(3)

    def get_driver(self):
        return self.driver






# def test_demo(self):
#     def loaded(driver):
#         if len(self.driver.find_element_by_xpath("//*[@text='立即更新']")) >= 1:
#             self.driver.find_element_by_xpath("//*[@text='立即更新']").click()
#             return True
#         else:
#             return False
#     try:
#         WebDriverWait(self.driver, 15).until(loaded())
#     except BaseException:
#         print("没有关闭直接点更新")
#
#
# def teardown(self):
#     self.driver.quit()
