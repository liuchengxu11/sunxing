
import time
from appium import webdriver

from appium_jike.page.config_page import Config_page



class swipe(Config_page):
    def __init__(self):
        driver=webdriver

        # 获取屏幕的size
        self.size = self.driver.get_window_size()
        # 获取屏幕宽度 width
        self.width = self.size['width']
        # 获取屏幕高度 height
        height = self.size['height']




    # 封装滑动方法

    def swipeUp(driver, n=5):
        '''定义向上滑动方法'''
        print("定义向上滑动方法")
        x1 = width * 0.5
        y1 = height * 0.9
        y2 = height * 0.25
        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(x1, y1, x1, y2)

    def swipeDown(driver, n=5):
        '''定义向下滑动方法'''
        print("定义向下滑动方法")
        x1 = width * 0.5
        y1 = height * 0.25
        y2 = height * 0.9
        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(x1, y1, x1, y2)

    def swipeLeft(driver, n=5):
        '''定义向左滑动方法'''
        print("定义向左滑动方法")
        x1 = width * 0.8
        x2 = width * 0.2
        y1 = height * 0.5

        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(x1, y1, x2, y1)

    def swipeRight(driver, n=5):
        '''定义向右滑动方法'''
        print("定义向右滑动方法")
        x1 = width * 0.2
        x2 = width * 0.8
        y1 = height * 0.5

        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(x1, y1, x2, y1)
