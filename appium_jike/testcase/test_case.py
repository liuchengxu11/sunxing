from appium_jike.page.app import App

class TestDemo:

    def setup(self):# 完成app的初始化并进入百度的首页
        self.search_page=App.app().home_search()

    def test_search_po(self):# 进入搜索框后在搜索页面里输入内容
        self.search_page.search("星巴克")

    def teardown(self):
        App.quit()