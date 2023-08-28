import time
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import InvalidSessionIdException

from functions_prescription import wait_article, article_loads


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
    dim = ['width', 'height']
    phone = '+49123456789'

    def __init__(self):
        self.access_code = 'CARADIGATEST1234'
        print("Access_Code = " + self.access_code)

    def test_setup(self):
        self.dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu",
            "app": "/Users/ishan/Documents/Builds/5794.apk",
            "newCommandTimeout": "45"
        }

        self.time = datetime.now()
        self.ct = time.strftime("%d%m%y%H%M%S")
        self.user_name = "ishan" + "+" + self.access_code + "@cara.care"
        print(self.user_name)
        self.name = "ishan" + "+" + self.access_code
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
        self.driver.implicitly_wait(45)

    def test_onboarding(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "New start").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Select IBS program").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Confirm").click()
        el = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.CheckBox')
        el[0].click()
        el[1].click()
        el[2].click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Confirm").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue with registration").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen email input").send_keys(self.user_name)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen password input").send_keys(
            self.password)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen repeat password input").send_keys(
            self.password)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen access code input").send_keys(
            self.access_code)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen terms of use checkbox").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen privacy policy checkbox").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen access code input").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen access code input").send_keys(
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
        self.dim = ['50', '50']
        time.sleep(10)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registration screen register button").click()

        # 16 Characters Coupon Code Validation
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Reimbursmentapi Code Input").send_keys(self.access_code)
        # self.driver.swipe(start_x, start_y, end_x, end_y, 1)
        # self.path = '(//android.widget.TextView[@text = "WIEDERHOLEN"])'
        # self.driver.find_element(AppiumBy.XPATH, self.path).click()

        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Email verification screen open email button").click()

        time.sleep(5)
        self.driver.swipe(end_x, end_y, start_x, start_y, 1)
        time.sleep(10)

        self.path = '(//android.widget.TextView[@text = "[Cara C…] Bestätige deine E-Mail-Adresse"])'
        self.driver.find_element(AppiumBy.XPATH, self.path).click()
        time.sleep(10)
        self.driver.swipe(end_x, end_y, start_x, start_y, 1)
        time.sleep(10)
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

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Set nickname screen input").send_keys(self.name)
        time.sleep(3)

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Set nickname screen next button").click()
        time.sleep(3)

        # Mobile Number Capture
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Enter your mobile phone number").send_keys(self.phone)
        time.sleep(3)
        path = '(//android.widget.TextView[@text = "WEITER"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "BESTÄTIGEN"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(10)

        path = '(//android.widget.TextView[@text = "Programm"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(15)

        c1_path = '(//android.widget.TextView[@text = "10 Fakten über Cara Care für Reizdarm"])'
        wait_article(c1_path, self.driver)
        article_visible = article_loads(c1_path, self.driver)

        if not article_visible:
            self.driver.reset()
            time.sleep(40)
            var = Onboarding()
            var.test_setup()
            var.test_onboarding()
        else:
            print("Onboarding Articles Load fine. Proceed to next Test Case")

    try:
        def test_teardown(self):
            self.driver.quit()
    except InvalidSessionIdException:
        print("Error in closing the driver")
        pass



