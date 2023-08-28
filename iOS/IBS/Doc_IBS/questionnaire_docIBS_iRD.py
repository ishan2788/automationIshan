import time
from appium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from iOS.IBS.functions_iRD import click_element, go_next, swipe_down, send_keys, scroll_right, find


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
            "platformName": "iOS",
            "xcodeOrgId": "5K7J2838R5",
            "xcodeSigningId": "iPhone Developer",
            "deviceName": "Cara's iPhone",
            "automationName": "XCUITest",
            "bundleId": "com.gohidoc.caraeu",
            "udid": "cebfcd519bbf550c384f2fa30c201c86926ab935",
            "platformVersion": "15.3",
            "noReset": "true"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
        self.driver.implicitly_wait(50)

    def test_questionnaire(self):

        # time.sleep(15)
        #
        # click_element(self.driver, index=1, path='//XCUIElementTypeOther[@name="FRAGEBOGEN Gesundheits-Fragebogen"]')

        go_next(self.driver, case=0)

        send_keys(self.driver, index=2, path="XCUIElementTypeTextField", keys="29")
        time.sleep(5)
        go_next(self.driver, case=0)
        time.sleep(5)

        send_keys(self.driver, index=2, path="XCUIElementTypeTextField", keys="180")
        time.sleep(5)
        go_next(self.driver, case=0)
        time.sleep(5)

        send_keys(self.driver, index=2, path="XCUIElementTypeTextField", keys="100")
        time.sleep(5)
        go_next(self.driver, case=0)
        time.sleep(5)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="männlich"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="das Reizdarmsyndrom verstehen"])[2]')
        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Unter keinem dieser Symptome"])[2]')
        go_next(self.driver, case=0)

        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nichts davon trifft zu"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Keines"])[2]')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Keine der genannten"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein."])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        scroll_right(self.driver)
        go_next(self.driver, case=0)

        scroll_right(self.driver)
        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        path = '(//XCUIElementTypeOther[@name="Überhaupt nicht"])[2]'
        next_path = '//XCUIElementTypeOther[@name="Weiter"]'
        find(self.driver, path, next_path)

        go_next(self.driver, case=0)

        find(self.driver, path, next_path)

        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        path = '(//XCUIElementTypeOther[@name="Ich gehe derzeit keiner Beschäftigung nach."])[2]'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="kein Urlaub"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="keine Veranstaltung"])[2]')
        go_next(self.driver, case=0)

        path = '(//XCUIElementTypeOther[@name="Nein, ich erkenne da keinen Zusammenhang."])[2]'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Keine bestimmte"])[2]')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        path = '(//XCUIElementTypeOther[@name="Ich koche nicht und esse meistens auswärts."])[2]'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Keine der genannten"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein, ich bin hörend."])')
        go_next(self.driver, case=0)

        path = '(//XCUIElementTypeOther[@name="Ja, ich würde gerne meine Ernährung mithilfe des Programms ' \
               'umstellen."])[2] '
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Audio-geführte Hypnose"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Fisch"])[2]')
        go_next(self.driver, case=0)

        path = '(//XCUIElementTypeOther[@name="Ja, ich habe eine ärztlich diagnostizierte Fischallergie"])[2]'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        path = '(//XCUIElementTypeOther[@name="Ja, gegen Pollen"])[2]'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        path = '(//XCUIElementTypeOther[@name="Birke und andere Baumpollen"])[2]'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Auf keine"])[2]')
        go_next(self.driver, case=0)

        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)

        path = '(//XCUIElementTypeOther[@name="Ich habe keine Allergie und keine Beschwerden"])[2]'
        click_element(self.driver, index=1, path=path)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Ja, Laktoseintoleranz"])[2]')
        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Ja, Fruktoseintoleranz"])[2]')
        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        time.sleep(10)
        click_element(self.driver, index=0, path='questionnaire_complete_button')

        time.sleep(5)
        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="close_button"])[2]')

        click_element(self.driver, index=1, path='//XCUIElementTypeOther[@name="Ok"]')

        go_next(self.driver, case=0)

        for x in range(7):
            swipe_down(self.driver)
            time.sleep(5)

        for x in range(3):
            swipe_down(self.driver)
            time.sleep(5)

    def test_teardown(self):
        try:
            self.driver.quit()
        except InvalidSessionIdException:
            print("Error in closing the driver")
            pass
