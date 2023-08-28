import time
from datetime import datetime

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import InvalidSessionIdException

from androidRealDevice.IBS.Control.functions_IBS_Control import click_element, swipe_down


class Foodlist:
    dc = {}
    driver = None
    time = None
    dimension = ['width', 'height']
    path = None

    def test_setup(self):
        self.dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu",
            "skipDeviceInitialization": "true",
            "skipServerInstallation": "true",
            "noReset": "true"
        }

        self.time = datetime.now()
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
        self.driver.implicitly_wait(50)

    def foodlist(self):

        for x in range(60):
            time.sleep(20)
            click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Tool Kit"])')
            # el = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.view.ViewGroup')
            # el[3].click()
            click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Lebensmittelliste"])')
            time.sleep(3)
            click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "ALLE ANZEIGEN"])')
            time.sleep(10)
            swipe_down(self.driver)
            time.sleep(3)
            swipe_down(self.driver)
            time.sleep(3)
            self.driver.close_app()
            self.driver.activate_app('com.gohidoc.caraeu')
            print(x)
    try:
        def test_teardown(self):
            self.driver.quit()
    except InvalidSessionIdException:
        print("Error in closing the driver")
        pass
