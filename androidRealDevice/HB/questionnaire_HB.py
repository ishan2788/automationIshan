import time
from datetime import datetime
from appium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from actions import click_element, send_keys, swipe_down, go_next, scroll_right, newfinder


class Questionnaire:
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
    next_path = None
    phone = '+49123456789'

    def test_setup(self):
        self.dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu",
            "skipDeviceInitialization": "true",
            "skipServerInstallation": "true",
            "noReset": "true",
            "automationName": "UiAutomator2"
        }

        self.time = datetime.now()
        self.ct = time.strftime("%d%m%y%H%M%S")
        self.user_name = "ishan" + "+" + self.ct + "@cara.care"
        self.name = "ishan" + "+" + self.ct
        self.driver = webdriver.Remote("http://127.0.0.1:4723", self.dc)
        self.driver.implicitly_wait(30)

    def test_ques(self):

        # send_keys(self.driver, index=0, path="Login screen password input", keys=self.password)
        # self.driver.hide_keyboard('tapOut')
        # time.sleep(5)
        # click_element(self.driver, index=0, path="Login screen signin button")

        # click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Gesundheits-Fragebogen"])')
        # time.sleep(2)

        go_next(self.driver, case=0)

        send_keys(self.driver, index=2, path="android.widget.EditText", keys="29")
        self.driver.hide_keyboard('swipeDown')
        go_next(self.driver, case=0)
        time.sleep(2)

        send_keys(self.driver, index=2, path="android.widget.EditText", keys="180")
        self.driver.hide_keyboard('swipeDown')
        go_next(self.driver, case=0)
        time.sleep(2)

        send_keys(self.driver, index=2, path="android.widget.EditText", keys="100")
        self.driver.hide_keyboard('swipeDown')
        go_next(self.driver, case=0)
        time.sleep(2)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "männlich"])')
        go_next(self.driver, case=0)

        time.sleep(2)
        swipe_down(self.driver)
        swipe_down(self.driver)
        path = '(//android.widget.TextView[@text = "neue Behandlungsoptionen kennenlernen"])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        send_keys(self.driver, index=0, path="Questionnaire input", keys="1990")
        self.driver.hide_keyboard('swipeDown')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ich rauche zur Zeit."])')
        go_next(self.driver, case=0)

        send_keys(self.driver, index=0, path="Questionnaire input", keys="1")
        self.driver.hide_keyboard('swipeDown')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nie"])')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        swipe_down(self.driver)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Keine der genannten"])')
        go_next(self.driver, case=0)

        send_keys(self.driver, index=2, path="android.widget.EditText", keys="Test HB Questionnaire")
        self.driver.hide_keyboard('swipeDown')
        go_next(self.driver, case=0)
        time.sleep(2)
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Gar nicht aufgetreten"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        newfinder(self.driver, path, next_path)

        time.sleep(3)
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Gar nicht aufgetreten"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        newfinder(self.driver, path, next_path)

        time.sleep(3)
        go_next(self.driver, case=0)

        scroll_right(self.driver)
        go_next(self.driver, case=0)

        scroll_right(self.driver)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Keine oder leichte Schmerzen"])')
        go_next(self.driver, case=0)

        scroll_right(self.driver)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Keine Schmerzen"])')
        go_next(self.driver, case=0)

        scroll_right(self.driver)
        go_next(self.driver, case=0)

        time.sleep(2)
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Kein Problem"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        newfinder(self.driver, path, next_path)

        time.sleep(2)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Sehr zufrieden"])')
        go_next(self.driver, case=0)

        time.sleep(2)
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Trifft vollkommen zu"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        newfinder(self.driver, path, next_path)

        scroll_right(self.driver)
        go_next(self.driver, case=0)

        time.sleep(3)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ständig"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ständig"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Sehr stark"])')
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Ständig"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        newfinder(self.driver, path, next_path)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Sehr stark"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ständig"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ständig"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Sehr stark"])')
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Ständig"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        newfinder(self.driver, path, next_path)

        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Keine bestimmte"])')
        go_next(self.driver, case=0)

        time.sleep(2)
        swipe_down(self.driver)
        swipe_down(self.driver)
        path = '(//android.widget.TextView[@text = "Ich gehe derzeit keiner Beschäftigung nach."])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        time.sleep(2)
        go_next(self.driver, case=0)

        time.sleep(2)
        swipe_down(self.driver)
        swipe_down(self.driver)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Keine"])')
        go_next(self.driver, case=0)

        time.sleep(2)
        swipe_down(self.driver)
        swipe_down(self.driver)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Keines"])')
        go_next(self.driver, case=0)

        time.sleep(2)
        swipe_down(self.driver)
        swipe_down(self.driver)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein."])')
        go_next(self.driver, case=0)

        for i in range(5):
            time.sleep(2)
            go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Ich möchte mich mit meiner "mentalen Gesundheit" befassen."])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Audio-geführte Hypnose"])')
        go_next(self.driver, case=0)

        time.sleep(2)
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Überhaupt nicht"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        newfinder(self.driver, path, next_path)

        time.sleep(3)
        swipe_down(self.driver)
        swipe_down(self.driver)
        swipe_down(self.driver)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "auf keines"])')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        swipe_down(self.driver)
        swipe_down(self.driver)
        path = '(//android.widget.TextView[@text = "Ich habe keine Allergie und keine Beschwerden"])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        swipe_down(self.driver)
        swipe_down(self.driver)
        path = '(//android.widget.TextView[@text = "Ich habe keine Allergie und keine Beschwerden"])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        swipe_down(self.driver)
        swipe_down(self.driver)
        path = '(//android.widget.TextView[@text = "Keine"])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Trifft überhaupt nicht zu"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        newfinder(self.driver, path, next_path)

        for i in range(6):
            click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
            go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nie/selten"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ergebnisse"])')
        time.sleep(50)

    def test_teardown(self):
        try:
            self.driver.quit()
        except InvalidSessionIdException:
            print("Error in closing the driver")
            pass
