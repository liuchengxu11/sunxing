from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from appium_jike.page.config_page import Config_page
from appium_jike.page.search_page import Search_page

"""
app启动过后进入的百度首页
"""

class Home_page(Config_page):
    _search_locator = (By.ID, "com.xueqiu.android:id/home_search")
    def home_search(self):
        # 百度首页上点击搜索
        self.find_element_and_click(self._search_locator)
        return Search_page(self.driver)




