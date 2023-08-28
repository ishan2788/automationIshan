import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import InvalidSessionIdException
from actions import newfinder, scroll_right, go_next, click_element, swipe_down


class Questionnaire:
    password = "Caracare@123"
    dc = {}
    driver = None
    dimension = ['width', 'height']
    path = ''

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

        self.driver = webdriver.Remote("http://localhost:4723", self.dc)
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.dimension = self.driver.get_window_size()

    def test_questionnaire(self):

        # # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen password input").send_keys(self.password)
        # # self.driver.hide_keyboard('tapOut')
        # # time.sleep(5)
        # #
        # # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen signin button").click()
        # #
        # # time.sleep(10)

        path = '(//android.widget.TextView[@text = "Programm"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(5)

        swipe_down(self.driver)
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Gesundheits-Fragebogen"])'
        time.sleep(3)

        el = self.driver.find_element(AppiumBy.XPATH, path)
        el.click()
        time.sleep(10)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("29")
        self.driver.hide_keyboard('swipeDown')
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("180")
        self.driver.hide_keyboard('swipeDown')
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("100")
        self.driver.hide_keyboard('swipeDown')
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "männlich"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "meine Erkrankung verstehen"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("2008")
        self.driver.hide_keyboard('swipeDown')
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Keine"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Verdauungsbeschwerden auch außerhalb eines Schubs."])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Weiß nicht"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Weiß nicht"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Weiß nicht"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(2)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Weiß nicht"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Keine der genannten"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("1")
        self.driver.hide_keyboard('swipeDown')
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Weiß nicht"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ich rauche zur Zeit."])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("1")
        self.driver.hide_keyboard('swipeDown')
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Nie"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Nie"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "keine Schwierigkeiten; die Darmerkrankung hat die Freizeit- oder ' \
               'Sportaktivität nicht eingeschränkt"]) '
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Nie"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Nie"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        path = '(//android.widget.TextView[@text = "Kein Problem"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)
        path = '(//android.widget.TextView[@text = "Kein Problem"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Nie"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Nie"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(2)
        swipe_down(self.driver)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Nie"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Überhaupt nicht"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        newfinder(self.driver, path, next_path)

        path = '(//android.widget.TextView[@text = "Sehr gut"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path_loop = '(//android.widget.TextView[@text = "Gar nicht"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'

        newfinder(self.driver, path_loop, next_path)
        time.sleep(3)

        path_loop = '(//android.widget.TextView[@text = "Gar keine"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'

        newfinder(self.driver, path_loop, next_path)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "0"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path_loop = '(//android.widget.TextView[@text = "Überhaupt nicht"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'

        newfinder(self.driver, path_loop, next_path)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path_loop = '(//android.widget.TextView[@text = "Stimmt nicht"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'

        newfinder(self.driver, path_loop, next_path)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "glutenhaltiges Getreide (Weizen, Roggen, Gerste, Hafer, Dinkel, ' \
               'Kamut)"]) '
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Krebstiere (Garnelen, Krabben, Langusten und Hummer)"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Hühnereier"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Fisch"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ja, ich habe eine ärztlich diagnostizierte Weizenallergie."])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ja, ich habe eine ärztlich diagnostizierte Krebstierallergie."])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ja, ich habe eine ärztlich diagnostizierte Hühnereiweißallergie."])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ja, ich habe eine ärztlich diagnostizierte Fischallergie"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ja, gegen Pollen"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        go_next(self.driver, 0)

        path = '(//android.widget.TextView[@text = "Birke und andere Baumpollen"])'
        click_element(self.driver, 1, path)
        go_next(self.driver, 0)

        path = '(//android.widget.TextView[@text = "Nüsse (Haselnuss, Walnuss, Mandeln, Erdnuss)"])'
        click_element(self.driver, 1, path)
        go_next(self.driver, 0)

        path = '(//android.widget.TextView[@text = "Ja, gegen Naturlatex"])'
        click_element(self.driver, 1, path)
        go_next(self.driver, 0)

        path = '(//android.widget.TextView[@text = "Obst (Kiwi, Melone, Banane, Feige, Papaya, Apfel, Birne, ' \
               'Acerola-Kirsche, Passionsfrucht)"]) '
        click_element(self.driver, 1, path)
        go_next(self.driver, 0)

        path = '(//android.widget.TextView[@text = "Ja, Laktoseintoleranz"])'
        click_element(self.driver, 1, path)
        path = '(//android.widget.TextView[@text = "Ja, Fruktoseintoleranz"])'
        click_element(self.driver, 1, path)
        path = '(//android.widget.TextView[@text = "Ja, Glutenunverträglichkeit (Zöliakie)"])'
        click_element(self.driver, 1, path)
        go_next(self.driver, 0)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)
        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ich gehe derzeit keiner Beschäftigung nach."])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Keine bestimmte"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(3)

        swipe_down(self.driver)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Ich koche nicht und esse meistens auswärts."])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        self.driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        scroll_right(self.driver)

    def test_teardown(self):
        try:
            self.driver.quit()
        except InvalidSessionIdException:
            print("Error in closing the driver")
            pass
