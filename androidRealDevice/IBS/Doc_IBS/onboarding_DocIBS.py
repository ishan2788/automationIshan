import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import InvalidSessionIdException

from actions import click_element, swipe_down, send_keys, swipe_up
from androidRealDevice.IBS.functions_ARD import wait_article, article_loads
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
    dim = ['width', 'height']
    phone = '+49123456789'

    def __init__(self):
        self.access_code = AccessCodes().test_doctors_ibs()
        print("Access_Code = " + self.access_code)

    def test_setup(self):
        self.dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu",
            "newCommandTimeout": "45",
            "automationName": "UiAutomator2"
        }

        self.user_name = "ishan27588" + "+" + self.access_code + "@gmail.com"
        self.name = "ishan" + "+" + self.access_code
        self.driver = webdriver.Remote("http://localhost:4723", self.dc)
        print(self.user_name)
        self.driver.implicitly_wait(45)

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

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen password input").send_keys(self.password)
        self.driver.hide_keyboard('tapOut')
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen signin button").click()

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
