import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from androidRealDevice.IBS.Doc_IBS.functions_DocIBS import wait


class Questionnaire:

    @staticmethod
    def testquestionnaire():
        desired_capabilities = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu",
            "skipDeviceInitialization": "true",
            "skipServerInstallation": "true",
            "noReset": "true"
        }

        password = "Caracare@123"

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
        driver.implicitly_wait(20)
        time.sleep(5)
        dimension = driver.get_window_size()

        v_start_x = dimension['width'] * 0.5
        v_start_y = dimension['height'] * 0.2
        v_end_x = dimension['width'] * 0.5
        v_end_y = dimension['height'] * 0.8

        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen password input").send_keys(password)
        driver.hide_keyboard('tapOut')
        time.sleep(5)

        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login screen signin button").click()
        time.sleep(15)

        path = '(//android.widget.TextView[@text = "Programm"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(30)

        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(3)
        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Gesundheits-Fragebogen"])'
        time.sleep(30)

        el = driver.find_element(AppiumBy.XPATH, path)
        el.click()
        time.sleep(30)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("29")
        driver.hide_keyboard('swipeDown')
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("180")
        driver.hide_keyboard('swipeDown')
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys("100")
        driver.hide_keyboard('swipeDown')
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "männlich"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "das Reizdarmsyndrom verstehen"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(2)
        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Unter keinem dieser Symptome"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(2)
        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nichts davon trifft zu"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(2)
        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Keines"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(5)

        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(2)
        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(2)

        path = '(//android.widget.TextView[@text = "Nein"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(3)
        driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Keine der genannten"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein."])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Nein"])'
        driver.find_element(AppiumBy.XPATH, path).click()

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "0"])'
        el = driver.find_element(AppiumBy.XPATH, path)

        loc = el.location
        x_scroll = dimension['width'] * 0.8
        time.sleep(5)

        driver.swipe(loc['x'], loc['y'], x_scroll, loc['y'])
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(3)

        path = '(//android.widget.TextView[@text = "0"])'
        el = driver.find_element(AppiumBy.XPATH, path)

        loc = el.location
        x_scroll = dimension['width'] * 0.8
        time.sleep(5)

        driver.swipe(loc['x'], loc['y'], x_scroll, loc['y'])

        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(5)

        driver.find_element(AppiumBy.XPATH, path).click()
        time.sleep(5)

        path = '(//android.widget.TextView[@text = "Überhaupt nicht"])'
        next_path = '(//android.widget.TextView[@text = "Weiter"])'
        next_screen = driver.find_element(AppiumBy.XPATH, next_path)

        next_screen.click()
        time.sleep(5)

        def validate(var):
            driver.implicitly_wait(5)
            try:
                driver.find_element(AppiumBy.XPATH, var).is_displayed()
                return True
            except NoSuchElementException:
                return False

        def find(val):
            try:
                np = True
                f_check = validate(val)
                while np:
                    if f_check:
                        try:
                            driver.find_element(AppiumBy.XPATH, val).click()
                            wait(next_path, driver)
                            driver.find_element(AppiumBy.XPATH, next_path).click()
                            f_check = validate(val)
                        except StaleElementReferenceException:
                            print("StaleElementReferenceException inside find method questionnaire (if loop) -->", path)
                            pass
                    else:
                        np = False
            except NoSuchElementException:
                print("In Method (find)-->Questionnaire Script-->NoSuchElement Exception seen for" + val + next_path)
                find(val)
            except StaleElementReferenceException:
                print("In Method (find)-->Questionnaire Script-->StaleElementException seen for" + val + next_path)
                find(val)

        def next_click(x_path):
            try:
                np = True
                value = 0
                f_check = validate(x_path)
                while np:
                    if f_check:
                        driver.find_element(AppiumBy.XPATH, x_path).click()
                        f_check = validate(x_path)
                        value = value + 1
                    if value == 5:
                        np = False
                    else:
                        np = False

            except StaleElementReferenceException:
                print("In method Next Click Exception seen for" + path)
                next_click(x_path)

        try:
            time.sleep(5)
            find(path)
            time.sleep(5)

            next_click(next_path)
            time.sleep(15)

            find(path)
            time.sleep(15)

            next_click(next_path)
            time.sleep(10)

            driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
            time.sleep(2)
            driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
            time.sleep(5)

            path = '(//android.widget.TextView[@text = "Ich gehe derzeit keiner Beschäftigung nach."])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "kein Urlaub"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Nein"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "keine Veranstaltung"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Nein, ich erkenne da keinen Zusammenhang."])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Nein"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Nein"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Keine bestimmte"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Ich koche nicht und esse meistens auswärts."])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Nein"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Keine der genannten"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Nein, ich bin hörend."])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Ja, ich würde gerne meine Ernährung mithilfe des Programms ' \
                   'umstellen."]) '
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Audio-geführte Hypnose"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Fisch"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Ja, ich habe eine ärztlich diagnostizierte Fischallergie"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Ja, gegen Pollen"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Birke und andere Baumpollen"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Auf keine"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Ich habe keine Allergie und keine Beschwerden"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Ja, Laktoseintoleranz"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Ja, Fruktoseintoleranz"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            next_click(next_path)
            time.sleep(3)

            path = '(//android.widget.TextView[@text = "Ergebnisse"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(10)

            path = '//android.view.ViewGroup[@content-desc="Close button"]/android.widget.ImageView'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(10)

            path = '(//android.view.ViewGroup[@content-desc="Close button"])[2]'
            find(path)
            time.sleep(5)

            path = '(//android.widget.TextView[@text = "Ok"])'
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(10)

            path = '(//android.widget.TextView[@text = "Weiter"])'
            driver.find_element(AppiumBy.XPATH, path).click()

            for x in range(7):
                driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)
                time.sleep(5)

            for x in range(3):
                driver.swipe(v_start_x, v_start_y, v_end_x, v_end_y, 1)
                time.sleep(5)

        except StaleElementReferenceException:
            print("StaleElementReferenceException in Questionnaire Script", path)
            pass

        print("All TEST CASES EXECUTED SUCCESSFULLY")
        time.sleep(30)
        driver.quit()
