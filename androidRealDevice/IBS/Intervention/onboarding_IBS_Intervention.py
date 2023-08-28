import time
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import InvalidSessionIdException
from actions import click_element, send_keys, swipe_down, go_next, swipe_up
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
    phone = '+49123456789'

    def __init__(self):
        self.access_code = AccessCodes().test_rct_intervention()
        # self.access_code = AccessCodes().test_stg_rct_intervention()
        print("Access_Code = " + self.access_code)

    def test_setup(self):
        self.dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu",
            "automationName": "UiAutomator2"
            # "app": "/Users/ishan/Documents/Builds/5840.apk"
        }

        self.time = datetime.now()
        self.ct = time.strftime("%d%m%y%H%M%S")
        self.user_name = "ishan27588" + "+" + self.access_code + "@gmail.com"
        self.name = "ishan" + "+" + self.access_code
        self.driver = webdriver.Remote("http://localhost:4723", self.dc)
        print(self.user_name)

    def test_onboarding(self):

        click_element(self.driver, index=0, path="NEU STARTEN")
        click_element(self.driver, index=0, path="Cara Care für Reizdarm")
        click_element(self.driver, index=0, path="WEITER")
        click_element(self.driver, index=0, path="BESTÄTIGEN")

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ich bin mindestens 18 '
                                                 'Jahre alt."])')

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ich bin unter 70 Jahre alt."])')
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ich bin nicht schwanger."])')

        click_element(self.driver, index=0, path="BESTÄTIGEN")
        click_element(self.driver, index=0, path="WEITER ZUR REGISTRIERUNG")

        send_keys(self.driver, index=0, path="E-Mail-Adresse", keys=self.user_name)
        send_keys(self.driver, index=0, path="Passwort", keys=self.password)
        send_keys(self.driver, index=0, path="Passwort erneut eingeben", keys=self.password)
        send_keys(self.driver, index=0, path="Freischalt- oder Zugangscode", keys=self.access_code)

        click_element(self.driver, index=0, path="Registration screen terms of use checkbox")
        click_element(self.driver, index=0, path="Registration screen privacy policy checkbox")
        click_element(self.driver, index=0, path="Freischalt- oder Zugangscode")

        send_keys(self.driver, index=0, path="Freischalt- oder Zugangscode", keys=self.access_code)
        self.driver.back()
        el = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        el[2].click()

        swipe_down(self.driver)
        click_element(self.driver, index=0, path="Registration screen register button")
        click_element(self.driver, index=0, path="Email verification screen open email button")
        time.sleep(10)
        swipe_up(self.driver)
        time.sleep(15)

        path = '(//android.widget.TextView[@text = "[Cara C…] Bestätige deine E-Mail-Adresse"])'
        click_element(self.driver, index=1, path=path)
        time.sleep(5)
        swipe_down(self.driver)
        time.sleep(5)
        click_element(self.driver, index=0, path="E-Mail-Adresse bestätigen")
        time.sleep(10)

        self.driver.back()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.back()

        self.driver.activate_app('com.gohidoc.caraeu')
        time.sleep(2)

        self.driver.close_app()
        time.sleep(5)

        self.driver.activate_app('com.gohidoc.caraeu')
        time.sleep(5)

        go_next(self.driver, case=1)
        send_keys(self.driver, index=0, path="Set nickname screen input", keys=self.name)
        click_element(self.driver, index=0, path="Set nickname screen next button")

        # Mobile Number Capture
        send_keys(self.driver, index=0, path="Enter your mobile phone number", keys=self.phone)
        go_next(self.driver, case=1)

        click_element(self.driver, index=2, path="android.widget.CheckBox")
        go_next(self.driver, case=1)

        go_next(self.driver, case=1)
        time.sleep(20)

        # go_next(self.driver, case=1)
        # time.sleep(5)

    try:
        def test_teardown(self):
            self.driver.quit()
    except InvalidSessionIdException:
        print("Error in closing the driver")
        pass
