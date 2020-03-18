from selenium.webdriver.common.by import By

from appium_jike.page.config_page import Config_page
from hamcrest import *

"""
点击百度上的搜索框而进入的搜索页面
"""
class Search_page(Config_page):
    _input_locator = (By.ID, "com.baidu.searchbox:id/SearchTextInput")
    # 变量前面加个_表示这个变量是私有的
    _name_locator = (By.ID, "com.baidu.searchbox:id/float_search_or_cancel")
    _chengxu_locator=(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.baidu.searchbox.widget.SlidingPaneLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.baidu.zeus.webviewpager2.ViewPager/android.widget.FrameLayout/com.baidu.webkit.sdk.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View[4]")
    def search(self, keyword):
        self.find_element(self._input_locator).clear()
        self.find_element(self._input_locator).send_keys(keyword)
        self.find_element(self._name_locator).click()
        prze =self.find_element(self._chengxu_locator)
        assert_that(prze.get_attribute("package"),equal_to("com.baidu.searchbox"))
        #  上面这两行就是断言执行用例后页面上有没有某个元素
        return self



