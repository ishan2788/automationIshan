import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import InvalidSessionIdException

from androidRealDevice.IBD.functions_IBD import finder
from iOS.IBS.functions_iRD import click_element, go_next, swipe_down, scroll_right, send_keys


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

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="meine Erkrankung verstehen"])[2]')
        go_next(self.driver, case=0)

        send_keys(self.driver, index=2, path="XCUIElementTypeTextField", keys="2005")
        time.sleep(2)
        go_next(self.driver, case=0)
        time.sleep(2)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Keine"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Verdauungsbeschwerden auch außerhalb '
                                                 'eines Schubs."])[2]')
        go_next(self.driver, case=0)

        for x in range(3):
            print(x)
            swipe_down(self.driver)
            time.sleep(2)
            swipe_down(self.driver)
            time.sleep(2)
            click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Weiß nicht"])[2]')
            go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Keine der genannten"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=2, path="XCUIElementTypeTextField")
        self.driver.find_element(AppiumBy.CLASS_NAME, "XCUIElementTypeTextField").send_keys("Test IBD")
        send_keys(self.driver, index=2, path="XCUIElementTypeTextField", keys="1")
        time.sleep(2)
        go_next(self.driver, case=0)
        time.sleep(2)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Weiß nicht"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Ich rauche zur Zeit."])[2]')
        go_next(self.driver, case=0)

        send_keys(self.driver, index=2, path="XCUIElementTypeTextField", keys="1")
        time.sleep(2)
        go_next(self.driver, case=0)
        time.sleep(2)

        for x in range(3):
            click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
            go_next(self.driver, case=0)
            time.sleep(2)

        scroll_right(self.driver)
        go_next(self.driver, case=0)

        scroll_right(self.driver)
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nie"])[2]')
        go_next(self.driver, case=0)

        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nie"])[2]')
        go_next(self.driver, case=0)

        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="keine Schwierigkeiten; die '
                                                 'Darmerkrankung hat die Freizeit- oder Sportaktivität nicht '
                                                 'eingeschränkt"])[2]')
        go_next(self.driver, case=0)

        for x in range(2):
            time.sleep(2)
            swipe_down(self.driver)
            time.sleep(2)
            swipe_down(self.driver)
            click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nie"])[2]')
            go_next(self.driver, case=0)

        for x in range(2):
            time.sleep(2)
            swipe_down(self.driver)
            time.sleep(2)
            swipe_down(self.driver)
            click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Kein Problem"])[2]')
            go_next(self.driver, case=0)

        for x in range(3):
            time.sleep(2)
            swipe_down(self.driver)
            time.sleep(2)
            swipe_down(self.driver)
            click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nie"])[2]')
            go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        time.sleep(2)
        path_loop = '(//XCUIElementTypeOther[@name="Überhaupt nicht"])'
        next_path = '(//XCUIElementTypeOther[@name="Weiter"])'
        finder(self.driver, path_loop, next_path)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Sehr gut"])[2]')
        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        path_loop = '(//XCUIElementTypeOther[@name="Gar nicht"])'
        next_path = '(//XCUIElementTypeOther[@name="Weiter"])'

        finder(self.driver, path_loop, next_path)
        time.sleep(3)

        path_loop = '(//XCUIElementTypeOther[@name="Gar keine"])[2]'
        next_path = '(//XCUIElementTypeOther[@name="Weiter"])'
        finder(self.driver, path_loop, next_path)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="0"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        path_loop = '(//XCUIElementTypeOther[@name="Überhaupt nicht"])[2]'
        next_path = '(//XCUIElementTypeOther[@name="Weiter"])'
        finder(self.driver, path_loop, next_path)
        time.sleep(3)

        go_next(self.driver, case=0)

        path_loop = '(//XCUIElementTypeOther[@name="Stimmt nicht"])[2]'
        next_path = '(//XCUIElementTypeOther[@name="Weiter"])'
        finder(self.driver, path_loop, next_path)
        time.sleep(3)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="glutenhaltiges Getreide (Weizen, '
                                                 'Roggen, Gerste, Hafer, Dinkel, '
                                                 'Kamut)"])')
        go_next(self.driver, case=0)

        swipe_down(self.driver)
        time.sleep(3)
        swipe_down(self.driver)
        time.sleep(3)
        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Krebstiere (Garnelen, Krabben, '
                                                 'Langusten und Hummer)"])')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Hühnereier"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Fisch"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1,
                      path='(//XCUIElementTypeOther[@name="Ja, ich habe eine ärztlich diagnostizierte '
                           'Weizenallergie."])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Ja, ich habe eine ärztlich '
                                                 'diagnostizierte Krebstierallergie."])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Ja, ich habe eine ärztlich '
                                                 'diagnostizierte Hühnereiweißallergie."])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Ja, ich habe eine ärztlich '
                                                 'diagnostizierte Fischallergie"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Ja, gegen Pollen"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Birke und andere Baumpollen"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nüsse (Haselnuss, Walnuss, Mandeln, '
                                                 'Erdnuss)"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Ja, gegen Naturlatex"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Obst (Kiwi, Melone, Banane, Feige, '
                                                 'Papaya, Apfel, Birne, '
                                                 'Acerola-Kirsche, Passionsfrucht)"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Ja, Laktoseintoleranz"])[2]')
        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Ja, Glutenunverträglichkeit ('
                                                 'Zöliakie)])[2]')
        go_next(self.driver, case=0)

        go_next(self.driver, case=0)

        for x in range(9):
            scroll_right(self.driver)
            go_next(self.driver, case=0)
            time.sleep(3)

        go_next(self.driver, case=0)

        click_element(self.driver, index=1, path='(//XCUIElementTypeOther[@name="Nein"])[2]')
        go_next(self.driver, case=0)

        scroll_right(self.driver)
        go_next(self.driver, case=0)

    def test_teardown(self):
        try:
            self.driver.quit()
        except InvalidSessionIdException:
            print("Error in closing the driver")
            pass
