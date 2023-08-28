import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class Test:
    dc = {}
    driver = None
    time = None
    ct = None
    name = None
    user_name = None
    password = "Caracare@123"
    access_code = None
    dimension = ['width', 'height']
    path = None
    next_path = None
    phone = '+49123456789'

    def test_setup(self):
        self.dc = {
            "platformName": "iOS",
            "xcodeOrgId": "5K7J2838R5",
            "xcodeSigningId": "iPhone Developer",
            "deviceName": "Cara's iPhone",
            "automationName": "XCUITest",
            "bundleId": "com.gohidoc.caraeu",
            "udid": "cebfcd519bbf550c384f2fa30c201c86926ab935",
            "platformVersion": "15.3",
            "noReset": "true"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
        self.driver.implicitly_wait(50)

    def test_logic(self):
        el = self.driver.find_elements(AppiumBy.XPATH, '//XCUIElementTypeOther')
        print(len(el))
        el[1].send_keys('Caracare@123')
        for i in el:
            i.click()
            print(i)
            time.sleep(5)


t = Test()
t.test_setup()
t.test_logic()
