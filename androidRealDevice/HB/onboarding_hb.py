import time
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import InvalidSessionIdException
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
    phone = None

    def __init__(self):
        self.access_code = AccessCodes().anwender_test_hb()
        # self.access_code = AccessCodes().anwender_test_hb_stg()
        print("Access_Code = " + self.access_code)

    def test_setup(self):
        self.dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu",
            "automationName": "UiAutomator2"
        }

        self.time = datetime.now()
        self.ct = time.strftime("%d%m%y%H%M%S")
        self.user_name = "ishan27588" + "+" + self.access_code + self.ct + "@gmail.com"
        self.name = "ishan" + "+" + self.access_code
        print(self.user_name)
        self.phone = "+4917627516657"
        self.driver = webdriver.Remote("http://localhost:4723", self.dc)
        self.driver.implicitly_wait(45)

    def test_onboarding(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "NEU STARTEN").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Cara Care für Sodbrennen").click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "WEITER").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BESTÄTIGEN").click()
        el = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.CheckBox')
        el[0].click()
        el[1].click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BESTÄTIGEN").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "WEITER ZUR REGISTRIERUNG").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E-Mail-Adresse").send_keys(self.user_name)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Passwort").send_keys(
            self.password)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Passwort erneut eingeben").send_keys(
            self.password)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Freischalt- oder Zugangscode").send_keys(
            self.access_code)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen terms of use checkbox").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen privacy policy checkbox").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Freischalt- oder Zugangscode").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Freischalt- oder Zugangscode").send_keys(
            self.access_code)
        self.driver.back()
        el = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        el[2].click()

        self.dimension = self.driver.get_window_size()
        start_x = self.dimension['width'] * 0.5
        start_y = self.dimension['height'] * 0.8
        end_x = self.dimension['width'] * 0.2
        end_y = self.dimension['height'] * 0.2

        self.driver.swipe(start_x, start_y, end_x, end_y, 1)

        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen register button").click()

        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Email verification screen open email button").click()

        time.sleep(5)
        self.driver.swipe(end_x, end_y, start_x, start_y, 1)
        time.sleep(10)

        self.path = '(//android.widget.TextView[@text = "[Cara C…] Bestätige deine E-Mail-Adresse"])'
        self.driver.find_element(AppiumBy.XPATH, self.path).click()
        time.sleep(5)
        self.driver.swipe(end_x, end_y, start_x, start_y, 1)
        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E-Mail-Adresse bestätigen").click()
        time.sleep(15)

        self.driver.back()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

        self.driver.activate_app('com.gohidoc.caraeu')
        path = '(//android.widget.TextView[@text = "WEITER"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        el = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.CheckBox')
        el[0].click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Confirm").click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Set nickname screen input").send_keys(self.name)
        time.sleep(3)

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Set nickname screen next button").click()
        time.sleep(3)

        # Mobile Number Capture
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Enter your mobile phone number").send_keys(self.phone)
        time.sleep(3)
        path = '(//android.widget.TextView[@text = "WEITER"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "BESTÄTIGEN"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(10)

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen password input").send_keys(self.password)
        self.driver.hide_keyboard('tapOut')
        time.sleep(5)

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen signin button").click()
        time.sleep(15)

    try:
        def test_teardown(self):
            self.driver.quit()
    except InvalidSessionIdException:
        print("Error in closing the driver")
        pass
