import yaml
import time
import time
import pytest
from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from utils.app_common.appium_driver import driver
from Config.Config import app_driver,driver_uri1,driver_uri2
"""
adb shell dumpsys window windows | grep -E 'mCurrentFocus|FocusedApp'
adb logcat|grep -i displayed 
"""


class Test_login():
    def setup_class(self):
        # self.driver = driver().androiddriver()
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", app_driver)
        self.driver.implicitly_wait(10)
        time.sleep(3)

    def test_11(self):
        pass




    # def test_334(self):
    #     TestCase("/Users/liuchengxu/work/sunxing/sunxing/Config/testcase.yaml").run(self.driver)
    #
#
# class TestCase():
#     def __init__(self,p):
#         file=open(p,"r")
#         self.setp=yaml.safe_load(file)

    #
    # def run(self, driver: WebDriver):
    #     for set in self.setp:
    #         element=None
    #         if isinstance(set,dict):
    #             if "id" in set.keys():
    #                 element=driver.find_element_by_id(set["id"])
    #             elif "xpath" in set.keys():
    #                 element=driver.find_element_by_xpath(set["xpath"])
    #                 time.sleep(2)
    #             if "input" in set.keys():
    #                 element.send_keys(set["input"])
    #             else:
    #                 element.click()









