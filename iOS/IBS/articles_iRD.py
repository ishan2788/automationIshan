import time
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from iOS.IBS.functions_iRD import wait, find, swipe_down, element_visible


class Articles:
    dc = {}
    driver = None
    time = datetime.now()
    ct = time.strftime("%d%m%y%H%M%S")
    user_name = "ishan" + "+" + ct + "@cara.care"
    name = "ishan" + "+" + ct
    password = "Caracare@123"
    code = "CARADIGATEST1234"
    path = "string"
    x_path = '//android.widget.TextView[contains(@text, "Kapitel")]'
    next_path = '(//android.widget.TextView[@text = "Fertig! 🎉"])'
    feed_path = '(//android.widget.TextView[@text = "ÜBERSPRINGEN"])'
    c1_path = '(//android.widget.TextView[@text = "10 Fakten über Cara Care für Reizdarm"])'
    c2_path = '(//android.widget.TextView[@text = "Deine Funktionen in der App"])'
    dimension = ['width', 'height']
    i = 0

    def setup(self):
        self.dc = {
            "platformName": "iOS",
            "xcodeOrgId": "5K7J2838R5",
            "xcodeSigningId": "iPhone Developer",
            "deviceName": "Cara's iPhone",
            "automationName": "XCUITest",
            "bundleId": "com.gohidoc.caraeu",
            "udid": "cebfcd519bbf550c384f2fa30c201c86926ab935",
            "skipDeviceInitialization": "true",
            "skipServerInstallation": "true",
            "platformVersion": "15.3",
            "noReset": "true"
        }
        time.sleep(10)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
        self.dimension = self.driver.get_window_size()
        self.driver.implicitly_wait(30)
        time.sleep(8)

    def testarticles(self):

        # el = self.driver.find_elements(AppiumBy.CLASS_NAME, "XCUIElementTypeOther")
        # print(len(el))
        # el[0].click()
        # el = self.driver.find_elements(AppiumBy.CLASS_NAME, "XCUIElementTypeOther")
        # print(len(el))
        # el[39].send_keys('Carcare@123')
        # print("1")
        # el[40].send_keys('Carcare@123')
        # print("1")
        # el[41].send_keys('Carcare@123')
        #
        # el[42].send_keys('Carcare@123')

        self.driver.hide_keyboard('tapOut')
        self.path = "xpath=//*[@text='Passwort']"
        el = self.driver.find_elements(AppiumBy.XPATH, self.path)
        print(len(el))

        wait(self.driver, self.path)
        self.driver.find_element(AppiumBy.XPATH, self.path).send_keys('Carcare@123')

        self.path = "xpath=//*[@text='Einloggen']"
        wait(self.path, self.driver)
        self.driver.find_element(AppiumBy.XPATH, self.path).click()

        self.path = "xpath=//*[@text='Programm']"
        wait(self.path, self.driver)
        self.driver.find_element(AppiumBy.XPATH, self.path).click()

        swipe_down(self.driver)
        wait(self.c1_path, self.driver)
        element_visible(self.c1_path, self.driver)
        element_visible(self.c1_path, self.driver)
        swipe_down(self.driver)

        wait(self.x_path, self.driver)
        find(self.x_path, self.driver, self.dimension)

        wait(self.next_path, self.driver)
        self.driver.find_element(AppiumBy.XPATH, self.next_path).click()

        wait(self.feed_path, self.driver)
        element_visible(self.feed_path, self.driver)

        wait(self.c1_path, self.driver)
        swipe_down(self.driver)

        wait(self.c2_path, self.driver)
        element_visible(self.c2_path, self.driver)

        wait(self.x_path, self.driver)
        find(self.x_path, self.driver, self.dimension)

        wait(self.next_path, self.driver)
        self.driver.find_element(AppiumBy.XPATH, self.next_path).click()

        wait(self.feed_path, self.driver)
        element_visible(self.feed_path, self.driver)

        self.path = '(//android.widget.TextView[@text = "Weiter"])'
        wait(self.path, self.driver)
        self.driver.find_element(AppiumBy.XPATH, self.path).click()

        self.path = '(//android.widget.TextView[@text = "Nicht jetzt"])'
        wait(self.path, self.driver)
        self.driver.find_element(AppiumBy.XPATH, self.path).click()

        time.sleep(5)
        swipe_down(self.driver)
        time.sleep(15)

    def teardown(self):
        self.driver.quit()
