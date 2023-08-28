import time
from datetime import datetime
from appium import webdriver
from actions import click_element, send_keys, swipe_down, go_next, scroll_right, \
    newfinder


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
        self.driver = webdriver.Remote("http://localhost:4723", self.dc)
        self.driver.implicitly_wait(30)

    def test_ques(self):

        # send_keys(self.driver, index=0, path="Login screen password input", keys=self.password)
        # self.driver.hide_keyboard('tapOut')
        # time.sleep(5)
        # click_element(self.driver, index=0, path="Login screen signin button")
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Gesundheits-Fragebogen"])')
        time.sleep(5)

        go_next(self.driver, case=0)

        send_keys(self.driver, index=2, path="android.widget.EditText", keys="29")
        self.driver.hide_keyboard('swipeDown')
        go_next(self.driver, case=0)
        time.sleep(5)

        send_keys(self.driver, index=2, path="android.widget.EditText", keys="180")
        self.driver.hide_keyboard('swipeDown')
        go_next(self.driver, case=0)
        time.sleep(5)

        send_keys(self.driver, index=2, path="android.widget.EditText", keys="100")
        self.driver.hide_keyboard('swipeDown')
        go_next(self.driver, case=0)
        time.sleep(5)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "männlich"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1,
                      path='(//android.widget.TextView[@text = "das Reizdarmsyndrom verstehen"])')
        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1,
                      path='(//android.widget.TextView[@text = "Unter keinem dieser Symptome"])')
        go_next(self.driver, case=0)

        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1,
                      path='(//android.widget.TextView[@text = "Nichts davon trifft zu"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Keines"])')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        time.sleep(3)
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Keine der genannten"])')
        go_next(self.driver, case=0)

        time.sleep(3)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein."])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        scroll_right(self.driver)
        time.sleep(2)
        go_next(self.driver, case=0)

        scroll_right(self.driver)
        time.sleep(2)
        go_next(self.driver, case=0)

        time.sleep(5)
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Überhaupt nicht"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        newfinder(self.driver, path, next_path)

        go_next(self.driver, case=0)

        newfinder(self.driver, path, next_path)

        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ich gehe derzeit keiner Beschäftigung nach."])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "kein Urlaub"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "keine Veranstaltung"])')
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Nein, ich erkenne da keinen Zusammenhang."])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Keine bestimmte"])')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ich koche nicht und esse meistens auswärts."])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Nein"])')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Keine der genannten"])')
        go_next(self.driver, case=0)

        time.sleep(3)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text ="Nein, ich bin hörend."])')
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Ja, ich würde gerne meine Ernährung mithilfe des Programms ' \
               'umstellen."]) '
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        click_element(self.driver, index=1,
                      path='(//android.widget.TextView[@text = "Audio-geführte Hypnose"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Fisch"])')
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Ja, ich habe eine ärztlich diagnostizierte Fischallergie"])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Ja, gegen Pollen"])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        path = '(//android.widget.TextView[@text = "Birke und andere Baumpollen"])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Auf keine"])')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ich habe keine Allergie und keine Beschwerden"])'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ja, Laktoseintoleranz"])')
        click_element(self.driver, index=1,
                      path='(//android.widget.TextView[@text = "Ja, Fruktoseintoleranz"])')
        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Ergebnisse"])')

        path = '//android.view.ViewGroup[@content-desc="Close button"]/android.widget.ImageView'
        click_element(self.driver, index=1, path=path)
        time.sleep(10)

        # path = '(//android.view.ViewGroup[@content-desc="Close button"])[2]'
        # newfinder(driver, path, next_path)
        # time.sleep(5)
        #
        # path = '(//android.widget.TextView[@text = "Ok"])'
        # driver.find_element(AppiumBy.XPATH, path).click()
        # time.sleep(10)
        #
        # path = '(//android.widget.TextView[@text = "Weiter"])'
        # driver.find_element(AppiumBy.XPATH, path).click()

        print("All TEST CASES EXECUTED SUCCESSFULLY")
        time.sleep(30)
        self.driver.quit()
