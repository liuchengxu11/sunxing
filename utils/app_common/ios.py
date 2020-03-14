"""
adb shell r"dumpsys window w|grep \/|grep name=|sed 's/mSurface(name=//g'|sed 's/)//g'|sed 's/ //g'"  手机上找到对应包名的adb指令

adb kill-server

adb kill-server

adb shell “dumpsys window | grep mCurrentFocus”

pip install Appium-Python-Client 下载appium的包

pip install guoya-tools


mac下的   adb shell dumpsys window windows | grep -E 'mCurrentFocus|FocusedApp'

"""

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['automationName'] = 'xcuitest'
desired_caps['app'] = '/Users/liuchengxu/Library/Developer/Xcode/DerivedData/bzz-dbznccgqghtlzvgfxmaxdmiikhvq/Build/Products/Release-iphoneos/bzz.app'
desired_caps['udid'] = '00008020-00015C960A33002E'
# appium提供的一种输入法，可以传中文。测试时直接用这个输入法
# desired_caps["unicodeKeyboard"] = "True"
# desired_caps["resetKeyboard"] = "True"  # 程序结束时重置原来的输入法
# desired_caps["noReset"] = "True"  # 不初始化手机app信息（类似不清楚缓存）
desired_caps['deviceName'] = '刘程旭'
desired_caps['showXcodeLog'] = 'true'
desired_caps['xcodeOrgId'] = 'Q24M7JR2C4'
desired_caps['xcodeSigningId'] = 'iPhone Developer'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
time.sleep(5)
driver.find_element_by_xpath("//XCUIElementTypeOther[@name='学习计时 锦鲤游学 排行榜 时间小店']/XCUIElementTypeOther[2]/XCUIElementTypeOther").click()
driver.find_element_by_xpath("//XCUIElementTypeOther[@name='常见问题']").click()
# 获取屏幕的size
size = driver.get_window_size()
print(size)
# 获取屏幕宽度 width
width = size['width']
print(width)
# 获取屏幕高度 height
height = size['height']
print(height)
# 执行滑屏操作,向上（上拉）滑动
print("swipe滑动方法演示")
x1 = width * 0.5
y1 = height * 0.8
y2 = height * 0.25
time.sleep(3)
print("向上滑动")
for i in range(5):
    l=i+1
    print("第%d次滑屏" % l)
    time.sleep(3)
    driver.swipe(x1, y1, x1, y2)
time.sleep(3)
print("向下滑动")
for i in range(5):
    l = i + 1
    print("第%d次滑屏" % l)
    time.sleep(3)
    driver.swipe(x1, y2, x1, y1)
print("前面swipe的方法在ios上不管用")
for i in range(5):
    driver.execute_script('mobile: swipe', {'direction': 'up'})
time.sleep(3)
for i in range(5):
    driver.execute_script('mobile: swipe', {'direction': 'down'})




