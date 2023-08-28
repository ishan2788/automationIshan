import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from iOS.IBS.functions_iRD import *

dc = {
    "platformName": "iOS",
    "xcodeOrgId": "5K7J2838R5",
    "xcodeSigningId": "iPhone Developer",
    "deviceName": "Cara's iPhone",
    "automationName": "XCUITest",
    "bundleId": "com.gohidoc.caraeu",
    "udid": "cebfcd519bbf550c384f2fa30c201c86926ab935",
    "platformVersion": "15.3",
    "noReset": "false",
    "newCommandTimeout": 3000
}
# count = 0
driver = webdriver.Remote("http://localhost:4723", dc)
time.sleep(5)

dimension = driver.get_window_size()
print(dimension['width'])
print(dimension['height'])
x = int(dimension['width'] * 0.08533333333)
y = int(dimension['height'] * 0.36206896551)

print(x, y)
action = ActionBuilder(driver)
action.pointer_action.move_to_location(x, y)
action.pointer_action.click()
action.perform()

# el = driver.find_elements(AppiumBy.CLASS_NAME, "XCUIElementTypeOther")
# print(len(el))
# for check in range(10):
#     print(check)
# swipe_up(driver)
# swipe_down(driver)
# click_element(driver, index=0, path="studyConfirmationScreen_informedCheckBox")
# for p in range(len(el)):
#     time.sleep(1)
#     print(el[p])
#     actions = TouchAction(driver)
#     actions.tap(el[p])
#     actions.perform()
#     count = count + 1
#     print(count)
#
