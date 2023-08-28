from datetime import datetime, time
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    InvalidElementStateException

now = datetime.now()
ct = now.strftime("%d%m%y%H%M%S")
user_name = "ishan" + "+" + ct + "@cara.care"
name = "ishan" + "+" + ct
password = "Caracare@123"
code = "CARADIGATEST1234"
i = 0


def click_element(driver, index, path):
    try:
        if index == 0:
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, path).click()
        elif index == 1:
            driver.find_element(AppiumBy.XPATH, path).click()
        elif index == 2:
            driver.find_element(AppiumBy.CLASS_NAME, path).click()
    except StaleElementReferenceException:
        time.sleep(10)
        print("StaleElementReferenceException seen in Send keys", path)
        click_element(driver, index, path)
    except InvalidElementStateException:
        time.sleep(10)
        print("StaleElementReferenceException seen in Send keys", path)
        click_element(driver, index, path)
    time.sleep(3)


def send_keys(driver, index, path, keys):
    try:
        if index == 0:
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, path).send_keys(keys)
        elif index == 1:
            driver.find_element(AppiumBy.XPATH, path).send_keys(keys)
        elif index == 2:
            driver.find_element(AppiumBy.CLASS_NAME, path).send_keys(keys)
    except StaleElementReferenceException:
        time.sleep(10)
        print("StaleElementReferenceException seen in Send keys", path, keys)
        send_keys(driver, index, path, keys)
    except InvalidElementStateException:
        print("InvalidElementStateException seen in Send keys", path, keys)
        send_keys(driver, index, path, keys)
    time.sleep(3)


def go_next(driver, case):
    if case == 0:
        path = '(//android.widget.TextView[@text = "Weiter"])'
        driver.find_element(AppiumBy.XPATH, path).click()
    elif case == 1:
        path = '(//android.widget.TextView[@text = "WEITER"])'
        driver.find_element(AppiumBy.XPATH, path).click()
    time.sleep(3)


def swipe_up(driver):
    dimension = driver.get_window_size()
    v_start_x = dimension['width'] * 0.5
    v_start_y = dimension['height'] * 0.2
    v_end_x = dimension['width'] * 0.5
    v_end_y = dimension['height'] * 0.6
    driver.swipe(v_start_x, v_start_y, v_end_x, v_end_y, 1)


def swipe_down(driver):
    try:
        dimension = driver.get_window_size()
        v_start_x = dimension['width'] * 0.5
        v_start_y = dimension['height'] * 0.8
        v_end_x = dimension['width'] * 0.2
        v_end_y = dimension['height'] * 0.2
        driver.swipe(v_start_x, v_start_y, v_end_x, v_end_y, 1)

    except InvalidElementStateException:
        swipe_down(driver)
    except StaleElementReferenceException:
        swipe_down(driver)


def swipe_right(driver):
    dimension = driver.get_window_size()
    start_x = dimension['width'] * 0.9
    start_y = dimension['height'] * 0.2
    end_x = dimension['width'] * 0.1
    end_y = dimension['height'] * 0.4
    driver.swipe(start_x, start_y, end_x, end_y, 1)
    time.sleep(1)


def scroll_right(driver):
    dimension = driver.get_window_size()
    path = '(//android.widget.TextView[@text = "0"])'
    el = driver.find_element(AppiumBy.XPATH, path)
    loc = el.location
    x_scroll = dimension['width'] * 0.9
    time.sleep(2)
    driver.swipe(loc['x'], loc['y'], x_scroll, loc['y'])


def validate(driver, var):
    driver.implicitly_wait(5)
    try:
        driver.find_element(AppiumBy.XPATH, var).is_displayed()
        return True
    except NoSuchElementException:
        return False


def wait(driver, path):
    global i
    try:
        check = False
        while not check:
            i = i + 1
            if i == 10:
                print("Element Not Found " + str(i) + " " + path)
                i = 0
                break
            check = driver.find_element(AppiumBy.XPATH, path).is_displayed()
            if check:
                i = 0
                break
    except NoSuchElementException:
        print("No Such Element --> wait method " + str(i) + " " + path)
        wait(driver, path)
    except StaleElementReferenceException:
        print("StaleElementReferenceException --> wait method " + str(i) + " " + path)
        wait(driver, path)


def find(driver, path, next_path):
    try:
        np = True
        print(next_path)
        f_check = validate(driver, path)
        while np:
            if f_check:
                try:
                    driver.find_element(AppiumBy.XPATH, path).click()
                    wait(driver, next_path)
                    driver.find_element(AppiumBy.XPATH, next_path).click()
                    f_check = validate(driver, path)
                except StaleElementReferenceException:
                    print("StaleElementReferenceException inside find method questionnaire (if loop) -->", path)
                    pass
            else:
                np = False
    except NoSuchElementException:
        print("In Method (find)-->Questionnaire Script-->NoSuchElement Exception seen for" + path + next_path)
        find(driver, path, next_path)
    except StaleElementReferenceException:
        print("In Method (find)-->Questionnaire Script-->StaleElementException seen for" + path + next_path)
        find(driver, path, next_path)


def next_click(driver, path):
    try:
        np = True
        value = 0
        f_check = validate(driver, path)
        while np:
            if f_check:
                driver.find_element(AppiumBy.XPATH, path).click()
                f_check = validate(driver, path)
                value = value + 1
            if value == 5:
                np = False
            else:
                np = False

    except StaleElementReferenceException:
        print("In method Next Click Exception seen for" + path)
        next_click(driver, path)
