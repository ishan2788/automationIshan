import time
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from actions import wait, swipe_down, element_visible, read_article, click_element, go_next, swipe_up


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
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
        self.dimension = self.driver.get_window_size()
        self.driver.implicitly_wait(30)
        time.sleep(8)

    def testarticles(self):

        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen password input").send_keys(self.password)
        # self.driver.hide_keyboard('tapOut')
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen signin button").click()

        time.sleep(10)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Programm"])')
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Willkommen"])')
        path = "10 Fakten über Cara Care für Reizdarm"
        click_element(self.driver, index=1, path=path)

        time.sleep(5)
        swipe_down(self.driver)
        swipe_down(self.driver)
        go_next(self.driver, 0)

        wait(self.driver, self.x_path)
        read_article(self.driver, self.x_path)

        wait(self.driver, self.next_path)
        self.driver.find_element(AppiumBy.XPATH, self.next_path).click()

        wait(self.driver, self.feed_path)
        element_visible(self.feed_path, self.driver)

        wait(self.driver, self.c1_path)
        swipe_down(self.driver)

        wait(self.driver, self.c2_path)
        element_visible(self.c2_path, self.driver)

        wait(self.driver, self.x_path)
        read_article(self.driver, self.x_path)

        wait(self.driver, self.next_path)
        self.driver.find_element(AppiumBy.XPATH, self.next_path).click()

        wait(self.driver, self.feed_path)
        element_visible(self.feed_path, self.driver)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ok"])')

        go_next(self.driver, case=0)

        for x in range(7):
            swipe_down(self.driver)
            time.sleep(5)

        for x in range(3):
            swipe_up(self.driver)
            time.sleep(5)

    def teardown(self):
        self.driver.quit()
