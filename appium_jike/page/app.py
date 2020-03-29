import datetime
import os

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from Config.Config import app_driver1,driver_uri1,driver_uri2,app_driver2
from appium_jike.page.home_page import Home_page
"""
查找app包的命令 adb shell dumpsys window windows | grep -E 'mCurrentFocus|FocusedApp'

adb shell pm clear com.baidu.searchbox   包名  清理包的缓存数据  
"""

class App():

    driver: WebDriver = None
    @classmethod
    def app(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['appPackage'] = 'com.tencent.mm'
        # desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['appPackage'] = 'com.baidu.searchbox'
        desired_caps['appActivity'] = 'com.baidu.searchbox.MainActivity'
        # appium提供的一种输入法，可以传中文。测试时直接用这个输入法
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"  # 程序结束时重置原来的输入法
        desired_caps["noReset"] = "True"  # 不初始化手机app信息（类似不清楚缓存）
        desired_caps['automationName'] = 'appium'
        desired_caps['deviceName'] = '12d63ed3'
        desired_caps['platformVersion'] = '9'
        desired_caps['autoGrantPermissions'] = 'True'
        udid=os.getenv("UDID",None)
        if udid!=None:
            desired_caps["udid"]=udid
            print("udid={}".format(udid))
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # cls.driver = webdriver.Remote("http://192.168.100.165:4444/wd/hub", app_driver1)  # grid的地址
        cls.driver.implicitly_wait(10)

        # 这里要封装一个显示等待应为启动后会有广告但是我们后面需要先下啦屏幕操作才能触发封装的方法再次之前先用
        # # 一个显示等待先解决调第一个可能出现的升级弹窗
        # WebDriverWait(cls.driver,10).until(
        #     expected_conditions.visibility_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView[2]")),
        #     cls.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView[2]").click()
        # )
        #
        return Home_page(cls.driver)




    @classmethod
    def quit(cls):
        cls.driver.quit()
