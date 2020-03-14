class Common:
    """
    封装通用的方法
    """

    def __init__(self):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read('enable_data.conf')



    def zjzh_login(self, driver):
        """
        资金账号登录方法,传入appium-driver
        APP启动时需要资金账号为登录状态时调用
        :param driver: Appium驱动
        :return: True
        """
        driver.get_name('发现').click()
        driver.switch_h5()
        driver.get_classes('list-item')[1].click()
        driver.switch_app()
        driver.get_name('买入').click()
        username = self.cf.get('zjzh_login_info', 'username')
        password = self.cf.get('zjzh_login_info', 'password')
        if self.tra_login(username, password, driver):
            self.check_title(u'委托买入', driver)
            driver.back()
            driver.back()
            self.check_title(u'发现', driver)
            logging.info('资金账号登录成功')
            return True

    def tra_login(self, username, password, driver):
        """
        资金账号登录页面的登录方法
        :param username:账号
        :param password:密码
        :param driver:Appium驱动
        :return:True
        """
        driver.get_id('com.weizq:id/edit_account').clear()
        driver.get_id('com.weizq:id/edit_account').send_keys(username)
        logging.info('输入的账号为: {}'.format(username))
        driver.get_id('com.weizq:id/edit_password').send_keys(password)
        logging.info('输入的密码为: {}'.format(password))
        yzm = driver.get_id('com.weizq:id/text_yanzhengma').text
        logging.info('验证码为:{}'.format(yzm))
        driver.get_id('com.weizq:id/edit_yanzhengma').send_keys(yzm)
        driver.get_id('com.weizq:id/login').click()
        time.sleep(3)
        return True