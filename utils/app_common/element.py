from utils.app_common import appium_driver
class Element:
    """
    封装Appium中关于元素对象的方法
    """

    def __init__(self):
        ar = appium_driver.driver
        self.driver=ar.androiddriver()


    def get_id(self, id):
        element = self.driver.find_element_by_id(id)
        return element

    def get_name(self, name):
        element = self.driver.find_element_by_name(name)
        return element

    def get_xpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def get_class(self, classesname):
        elements = self.driver.find_elements_by_class_name(classesname)
        return elements
    def over(self):
        element = self.driver.quit()
        return element

    def get_screen(self, path):
        self.driver.get_screenshot_as_file(path)

    def get_size(self):
        size = self.driver.get_window_size()
        return size

    def swipe_to_up(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    def swipe_to_down(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    def swipe_to_left(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    def swipe_to_right(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    def back(self):
        self.driver.keyevent(4)


