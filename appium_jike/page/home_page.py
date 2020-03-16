from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from appium_jike.page.config_page import Config_page
from appium_jike.page.search_page import Search_page

"""
app启动过后进入的百度首页
"""

class Home_page(Config_page):
    _search_locator = (By.ID, "com.baidu.searchbox:id/baidu_searchbox")
    def home_search(self):
        # 百度首页上点击搜索
        self.find_element_and_click(self._search_locator)
        return Search_page(self.driver)

    # 向上滑动
    def swipe_up(self, t=500, n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.75  # 起点y坐标
        y2 = s['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)


    # 向下滑动
    def swipe_down(self, t=500, n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.25  # 起点y坐标
        y2 = s['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    # 向左滑动
    def swipe_left(self, t=500, n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.75
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # 向右
    def swipe_right(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)


