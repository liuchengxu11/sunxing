SX_API_URl="http://47.102.141.214:8093/ccs"


# username: sunxing_ccs
# password: DPNLRMaZPZdX3WHk
# jdbc:mysql://47.102.193.100:3306
SX_DB_HOST="47.102.193.100"

SX_DB_USER="sunxing_ccs"

SX_DB_PASS="DPNLRMaZPZdX3WHk"

User_account="zhangtingting"

User_password="000000"


login_headers = {
    'content-type': 'application/json',
}

app_driver ={
    'platformName':'Android',
    'appPackage':'com.android.settings',
    'appActivity':'com.android.settings.HWSettings',
    "unicodeKeyboard":"True",# appium提供的一种输入法，可以传中文。测试时直接用这个输入法
    "resetKeyboard":"True",# 程序结束时重置原来的输入法
    "noReset":"True", # 不初始化手机app信息（类似不清楚缓存）
    'automationName':'appium',
    'deviceName':'QDY4C17807005548',
    'platformVersion':'7.0'
}

