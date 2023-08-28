import time
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from androidRealDevice.IBS.functions_ARD import wait_fooditemsload, click_fooditems


class Tracking:
    dc = {}
    driver = None
    time = datetime.now()
    ct = time.strftime("%d%m%y%H%M%S")
    user_name = "ishan" + "+" + ct + "@cara.care"
    name = "ishan" + "+" + ct
    password = "Caracare@123"
    code = "CARADIGATEST1234"
    path = None
    dimension = ['width', 'height']

    def setup(self):
        self.dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu",
            "noReset": "true",
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
        self.dimension = self.driver.get_window_size()
        self.driver.implicitly_wait(50)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen password input").send_keys(self.password)
        self.driver.hide_keyboard('tapOut')
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen signin button").click()

    def test_tracking(self):
        path = '(//android.widget.TextView[@text = "Tagebuch"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "TRACKE AN DIESEM TAG"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.EditText[@text = "Benenne dein Essen, z.B. Pizza"])'
        self.driver.find_element(AppiumBy.XPATH, path).send_keys('Automation - Food Item 1')
        time.sleep(10)

        path = 'android.widget.ImageView'
        el = self.driver.find_elements(AppiumBy.XPATH, path)
        el[0].click()
        el[0].click()
        el[0].click()

        path = '(//android.widget.TextView[@text = "Zutaten hinzufügen"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Schokolade (Milch)"])'
        wait_fooditemsload(self.driver, path)

        path = '//android.widget.ImageView'
        click_fooditems(self.driver, path)

        # # self.driver.find_element(AppiumBy.XPATH, path).is_displayed()
        #
        # path = '(//android.widget.TextView[@text = "Keks"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Softdrink"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Eiscreme"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Agavendicksaft"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Kuchen"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Keks (mit Schokolade)"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Brownies"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Pudding"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Popcorn"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Marshmallow"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Cracker"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()
        #
        # path = '(//android.widget.TextView[@text = "Fruchteis"])'
        # self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "SICHERN"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "ALLE SICHERN"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        time.sleep(30)


track = Tracking()
track.setup()
track.test_tracking()
