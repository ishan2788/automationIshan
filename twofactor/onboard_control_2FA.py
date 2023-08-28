import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import InvalidSessionIdException
# import subprocess
from actions import click_element, send_keys, swipe_down, swipe_up
from get_AccessCode import AccessCodes


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
    phone = '17627516657'
    otp = "123456"
    num = 0
    var = None
    email_code = None

    def __init__(self):
        # self.access_code = AccessCodes().test_stg_rct_control()
        self.access_code = AccessCodes().test_rct_control()
        print("Access_Code = " + self.access_code)

    def test_setup(self):
        self.dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu"
        }

        self.user_name = "ishan27588" + "+" + self.access_code + "@gmail.com"
        self.name = "ishan" + "+" + self.access_code
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
        print(self.user_name)
        self.driver.implicitly_wait(30)

    def test_onboarding(self):

        click_element(self.driver, index=0, path="welcome screen register button")
        click_element(self.driver, index=0, path="diagnosis code reminder continue button")
        click_element(self.driver, index=0, path="program selection screen program card Reizdarm")
        click_element(self.driver, index=0, path="instructions of use screen continue button")
        click_element(self.driver, index=0, path="contradiction check screen checkBox diagnosis")
        time.sleep(2)
        click_element(self.driver, index=0, path="contradiction check screen checkBox minAge")
        click_element(self.driver, index=0, path="contradiction check screen checkBox maxAge")
        click_element(self.driver, index=0, path="contradiction check screen checkBox pregnancy")
        click_element(self.driver, index=0, path="contradiction check screen continue button")

        send_keys(self.driver, index=0, path="registration screen nickname text input", keys=self.name)

        send_keys(self.driver, index=0, path="registration screen email text input", keys=self.user_name)
        send_keys(self.driver, index=0, path="registration screen password text input", keys=self.password)
        self.driver.back()
        time.sleep(2)
        swipe_down(self.driver)

        click_element(self.driver, index=0, path="registration screen password terms of use check box")
        click_element(self.driver, index=0, path="registration screen password privacy policy check box")

        swipe_down(self.driver)
        click_element(self.driver, index=0, path="registration screen register button")

        click_element(self.driver, index=0, path="email verification screen open email app button")
        time.sleep(5)
        swipe_up(self.driver)
        time.sleep(5)
        swipe_up(self.driver)
        time.sleep(10)

        path = '(//android.widget.TextView[@text = "[Cara C…] Bestätige deine E-Mail-Adresse"])'
        click_element(self.driver, index=1, path=path)
        time.sleep(5)
        swipe_down(self.driver)
        time.sleep(5)

        el = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        print(len(el))

        for i in range(len(el)):
            print(i, el[i].text)

        email_code = el[6].text
        print(email_code)

        if email_code == "Forward":
            self.driver.back()
            time.sleep(2)
            path = '(//android.widget.TextView[@text = "[Cara C…] Bestätige deine E-Mail-Adresse"])'
            click_element(self.driver, index=1, path=path)
            time.sleep(5)
            swipe_down(self.driver)
            time.sleep(5)
            el = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
            print(len(el))
            email_code = el[6].text
            print(email_code)

        self.driver.back()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.back()

        self.driver.activate_app('com.gohidoc.caraeu')
        time.sleep(10)

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='|']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='|']").click()
        time.sleep(5)

        for i in range(len(email_code)):
            time.sleep(2)
            num = int(email_code[i]) + 7
            self.driver.press_keycode(num)

        click_element(self.driver, index=0, path="email verification screen verify button")
        time.sleep(5)
        click_element(self.driver, index=0, path="recovery code screen informed check box")
        click_element(self.driver, index=0, path="recovery code screen continue button")

        # Bio Metric Login
        # click_element(self.driver, index=0, path="biometric auth screen enable button")
        # time.sleep(5)
        # subprocess.call("adb -e emu finger touch 1", shell=True)

        # Skip Biometric Login
        click_element(self.driver, index=0, path="biometric auth screen not now button")

        click_element(self.driver, index=0, path="technical tracking consent checkbox")
        click_element(self.driver, index=0, path="technical tracking consent continue button")
        send_keys(self.driver, index=0, path="code entry screen input code text input", keys=self.access_code)
        click_element(self.driver, index=0, path="code entry screen continue button")
        send_keys(self.driver, index=0, path="phone entry screen phone text input", keys=self.phone)
        click_element(self.driver, index=0, path="phone entry screen continue button")

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='|']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='|']").click()
        time.sleep(5)

        for i in range(6):
            time.sleep(2)
            num = int(self.otp[i]) + 7
            self.driver.press_keycode(num)

        click_element(self.driver, index=0, path="phone verification screen verify button")
        click_element(self.driver, index=0, path="study confirmation screen informed check box")
        time.sleep(5)
        click_element(self.driver, index=0, path="study confirmation screen continue button")
        time.sleep(5)
        click_element(self.driver, index=0, path="study intro screen continue button")
        time.sleep(15)

    try:
        def test_teardown(self):
            self.driver.quit()
    except InvalidSessionIdException:
        print("Error in closing the driver")
        pass
