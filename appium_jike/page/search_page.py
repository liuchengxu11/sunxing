from selenium.webdriver.common.by import By

from appium_jike.page.config_page import Config_page

"""
点击百度上的搜索框而进入的搜索页面
"""
class Search_page(Config_page):
    _input_locator = (By.ID, "com.baidu.searchbox:id/SearchTextInput")
    # 变量前面加个_表示这个变量是私有的
    _name_locator = (By.ID, "com.baidu.searchbox:id/float_search_or_cancel")

    def search(self, keyword):
        self.find_element(self._input_locator).clear()
        self.find_element(self._input_locator).send_keys(keyword)
        self.find_element(self._name_locator).click()
        return self
