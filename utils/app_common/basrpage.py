import time
import conf


class BasrPage:

    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, element, contents, sleep=conf.SLEEP_TIME):
        element.clear()
        element.send_keys(contents)
        time.sleep(sleep)

    def click(self, element, sleep=conf.SLEEP_TIME):
        element.click
        time.sleep(sleep)

    def find(self, path, by="xpath"):
        if by == "xpath":
            ele = self.driver.find_element_by_xpath(path)
        if by == "id":
            ele = self.driver.find_element_by_id(path)
        if by == "class":
            ele = self.driver.find_element_by_class(path)
        return ele
