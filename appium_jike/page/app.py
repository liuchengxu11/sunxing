import datetime

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from Config.Config import app_driver
from appium_jike.page.home_page import Home_page
"""
查找app包的命令 adb shell dumpsys window windows | grep -E 'mCurrentFocus|FocusedApp'

adb shell pm clear com.baidu.searchbox   包名  清理包的缓存数据  
"""

class App():
    driver: WebDriver = None
    @classmethod
    def app(cls):
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", app_driver)
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
