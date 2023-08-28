import time
from appium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from iOS.IBS.functions_iRD import click_element, go_next, swipe_down, send_keys, scroll_right, find


class Tracking:
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

    def add_to_tracking(self):
        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Tagebuch"])')
        print("Test Complete")
        go_next(self.driver, case=0)
