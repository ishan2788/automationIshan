import time
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from functions_DocIBS import wait, find, swipe_down, password, element_visible


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

    def setup(self):
        self.dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu",
            "noReset": "true",
        }
        time.sleep(10)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
        self.dimension = self.driver.get_window_size()
        self.driver.implicitly_wait(30)
        time.sleep(8)

    def testarticles(self):

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen password input").send_keys(password)
        self.driver.hide_keyboard('tapOut')
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen signin button").click()

        self.path = '(//android.widget.TextView[@text = "Programm"])'
        wait(self.path, self.driver)
        self.driver.find_element(AppiumBy.XPATH, self.path).click()

        swipe_down(self.driver, self.dimension)
        wait(self.c1_path, self.driver)
        element_visible(self.c1_path, self.driver)
        element_visible(self.c1_path, self.driver)
        swipe_down(self.driver, self.dimension)

        wait(self.x_path, self.driver)
        find(self.x_path, self.driver, self.dimension)

        wait(self.next_path, self.driver)
        self.driver.find_element(AppiumBy.XPATH, self.next_path).click()

        wait(self.feed_path, self.driver)
        element_visible(self.feed_path, self.driver)

        wait(self.c1_path, self.driver)
        swipe_down(self.driver, self.dimension)

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
        swipe_down(self.driver, self.dimension)
        time.sleep(15)

    def teardown(self):
        self.driver.quit()


# articles_docIBS_iRD.py = Articles()
# articles_docIBS_iRD.py.setup()
# articles_docIBS_iRD.py.testarticles()
# articles_docIBS_iRD.py.teardown()
