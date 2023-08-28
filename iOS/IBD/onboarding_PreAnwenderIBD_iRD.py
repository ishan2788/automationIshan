import time
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import InvalidSessionIdException
from get_AccessCode import AccessCodes
from iOS.IBS.functions_iRD import click_element, send_keys, swipe_down, swipe_up
import random


class Onboarding:
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
    num = 0
    phone = '+49123456789'

    def __init__(self):
        self.access_code = AccessCodes().anwender_test_ibd()
        print("Access_Code = " + self.access_code)

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

        self.time = datetime.now()
        self.ct = time.strftime("%d%m%y%H%M%S")
        self.num = str(random.randint(0, 1000000))

        # self.user_name = "ishan" + "+" + self.access_code + "@cara.care"
        self.user_name = "ishan" + "+" + self.num + "@cara.care"
        print(self.user_name)
        self.name = "ishan" + "+" + self.access_code
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
        self.driver.implicitly_wait(1)

    def test_onboarding(self):

        click_element(self.driver, index=0, path="new_account")
        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="select_IBS_program"])[2]')
        click_element(self.driver, index=0, path="continue")
        click_element(self.driver, index=0, path="confirm")
        path = '//XCUIElementTypeStaticText[@name="Ich bin mindestens 18 Jahre alt."]'
        click_element(self.driver, index=1, path=path)
        click_element(self.driver, index=1, path='//XCUIElementTypeStaticText[@name="Ich bin unter 70 Jahre alt."]')
        click_element(self.driver, index=0, path="confirm")
        click_element(self.driver, index=0, path="accessCodeReminderScreen_next")

        send_keys(self.driver, index=0, path="registrationScreen_email_input", keys=self.user_name)
        send_keys(self.driver, index=0, path="registrationScreen_password_input", keys=self.password)
        send_keys(self.driver, index=0, path="registrationScreen_repeat_password_input", keys=self.password)
        send_keys(self.driver, index=0, path="registrationScreen_access_code_input", keys=self.access_code)

        time.sleep(3)

        self.driver.hide_keyboard('tapOut')
        click_element(self.driver, index=0, path="registrationScreen_termsOfUse_checkbox")
        click_element(self.driver, index=0, path="registrationScreen_privacyPolicy_checkbox")

        swipe_down(self.driver)
        time.sleep(5)
        swipe_down(self.driver)

        time.sleep(5)
        click_element(self.driver, index=0, path="registrationScreen_register_button")
        click_element(self.driver, index=0, path="emailVerificationScreen_open_email_button")

        time.sleep(10)
        swipe_up(self.driver)
        time.sleep(10)

        path = '(//XCUIElementTypeStaticText[@name="Mail.messageList.cell.view.subjectLabel"])[1]'
        click_element(self.driver, index=1, path=path)

        click_element(self.driver, index=1, path='//XCUIElementTypeStaticText[@name="E-Mail-Adresse bestätigen"]')
        time.sleep(10)

        self.driver.activate_app("com.gohidoc.caraeu")
        time.sleep(5)

        click_element(self.driver, index=0, path='appUsageScreen_next_button')
        time.sleep(5)

        el = self.driver.find_elements(AppiumBy.CLASS_NAME, "XCUIElementTypeOther")
        print(len(el))
        el[66].click()

        click_element(self.driver, index=0, path='confirm')

        send_keys(self.driver, index=0, path="setNicknameScreen_name_input", keys=self.name)
        self.driver.hide_keyboard('tapOut')
        click_element(self.driver, index=0, path='setNicknameScreen_next_button')

        send_keys(self.driver, index=0, path="mobilePhoneScreen.numberInput", keys=self.phone)
        time.sleep(5)
        click_element(self.driver, index=3, path='Done')
        click_element(self.driver, index=0, path='setNicknameScreen_next_button')
        click_element(self.driver, index=0, path='confirm')

    try:
        def test_teardown(self):
            self.driver.quit()
    except InvalidSessionIdException:
        print("Error in closing the driver")
        pass
