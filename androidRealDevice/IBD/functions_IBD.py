from datetime import datetime, time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

now = datetime.now()
ct = now.strftime("%d%m%y%H%M%S")
user_name = "ishan" + "+" + ct + "@cara.care"
name = "ishan" + "+" + ct
password = "Caracare@123"
code = "CARADIGATEST1234"

i = 0
j = 0
k = 0
n = 0


def vertical_swipe(driver, element_location):
    dimension = driver.get_window_size()
    v_start_x = element_location['x']
    v_start_y = element_location['y']
    v_end_x = dimension['width'] * 0.4
    v_end_y = element_location['y']
    driver.swipe(v_start_x, v_start_y, v_end_x, v_end_y, 1)
    time.sleep(2)
    driver.swipe(v_start_x, v_start_y, v_end_x, v_end_y, 1)


def wait(path, driver):
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
        wait(path, driver)
    except StaleElementReferenceException:
        print("StaleElementReferenceException --> wait method " + str(i) + " " + path)
        wait(path, driver)


def validate(path, driver, dimension):
    driver.implicitly_wait(1)
    try:
        swipe_down(driver, dimension)
        time.sleep(1)
        swipe_down(driver, dimension)
        time.sleep(1)
        swipe_down(driver, dimension)
        time.sleep(1)
        swipe_down(driver, dimension)
        time.sleep(1)
        driver.find_element(AppiumBy.XPATH, path).is_displayed()
        return True
    except NoSuchElementException:
        return False


def find(path, driver, dimension):
    np = True
    f_check = validate(path, driver, dimension)
    while np:
        if f_check:
            driver.implicitly_wait(10)
            driver.find_element(AppiumBy.XPATH, path).click()
            time.sleep(2)
            swipe_right(driver, dimension)
            f_check = validate(path, driver, dimension)
        else:
            np = False


def swipe_right(driver, dimension):
    start_x = dimension['width'] * 0.9
    start_y = dimension['height'] * 0.2
    end_x = dimension['width'] * 0.1
    end_y = dimension['height'] * 0.4
    driver.swipe(start_x, start_y, end_x, end_y, 1)
    time.sleep(1)


def swipe_down(driver, dimension):
    v_start_x = dimension['width'] * 0.3
    v_start_y = dimension['height'] * 0.3
    v_end_x = dimension['width'] * 0.3
    v_end_y = dimension['height'] * 0.1
    driver.swipe(v_start_x, v_start_y, v_end_x, v_end_y, 1)


def swipe_up(driver, dimension):
    v_start_x = dimension['width'] * 0.3
    v_start_y = dimension['height'] * 0.3
    v_end_x = dimension['width'] * 0.3
    v_end_y = dimension['height'] * 0.1
    driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)


# Performs 3 Clicks on the element
def element_visible(path, driver):
    global j
    try:
        check = True
        while check:
            j = j + 1
            check = driver.find_element(AppiumBy.XPATH, path).is_displayed()
            driver.find_element(AppiumBy.XPATH, path).click()
            if j == 3:
                j = 0
                break
    except NoSuchElementException:
        j = 0
        return
    except StaleElementReferenceException:
        print("StaleElementReferenceException in method element_visible", path)
        element_visible(path, driver)


def article_loads(path, driver):
    try:
        time.sleep(10)
        check = driver.find_element(AppiumBy.XPATH, path).is_displayed()
        if check:
            return True
    except NoSuchElementException:
        print("Unable to find the first article. Need to reset and repeat the Sign Up flow again.")
        return False
    except StaleElementReferenceException:
        print("StaleElementReferenceException in method article_loads", path)
        article_loads(path, driver)


def wait_article(path, driver):
    global n
    driver.implicitly_wait(15)
    try:
        check = False
        while not check:
            if n == 3:
                print("Element Not Found " + str(n) + " " + path)
                n = 0
                break
            n = n + 1
            check = driver.find_element(AppiumBy.XPATH, path).is_displayed()
            if check:
                n = 0
                break
    except NoSuchElementException:
        print("No Such Element --> wait_article method " + str(n) + " " + path)
        wait_article(path, driver)
    except StaleElementReferenceException:
        print("StaleElementReferenceException in method wait_article", str(n), path)
        wait_article(path, driver)


def scroll_right(driver, dimension):
    path = '(//android.widget.TextView[@text = "0"])'
    el = driver.find_element(AppiumBy.XPATH, path)
    loc = el.location
    x_scroll = dimension['width'] * 0.9
    time.sleep(2)
    driver.swipe(loc['x'], loc['y'], x_scroll, loc['y'])


def valid(driver, path):
    driver.implicitly_wait(5)
    try:
        driver.find_element(AppiumBy.XPATH, path).is_displayed()
        return True
    except NoSuchElementException:
        return False


def finder(driver, path, next_path):
    try:
        np = True
        f_check = valid(driver, path)
        while np:
            if f_check:
                try:
                    time.sleep(5)
                    driver.find_element(AppiumBy.XPATH, path).click()
                    wait(next_path, driver)
                    driver.find_element(AppiumBy.XPATH, next_path).click()
                    f_check = valid(driver, path)
                except StaleElementReferenceException:
                    print("StaleElementReferenceException inside find method questionnaire (if loop) -->", path)
                    pass
            else:
                np = False
    except NoSuchElementException:
        print("In Method (find)-->Questionnaire Script-->NoSuchElement Exception seen for" + path + next_path)
        finder(driver, path, next_path)
    except StaleElementReferenceException:
        print("In Method (find)-->Questionnaire Script-->StaleElementException seen for" + path + next_path)
        finder(driver, path, next_path)


def next_click(driver, next_path):
    try:
        np = True
        value = 0
        f_check = valid(driver, next_path)
        while np:
            if f_check:
                driver.find_element(AppiumBy.XPATH, next_path).click()
                f_check = valid(driver, next_path)
                value = value + 1
            if value == 5:
                np = False
            else:
                np = False

    except StaleElementReferenceException:
        print("In method Next Click Exception seen for" + next_path)
        next_click(driver, next_path)


def go_next(driver):
    path = '(//android.widget.TextView[@text = "Weiter"])'
    driver.find_element(AppiumBy.XPATH, path).click()
    time.sleep(2)


def click_element(driver, path):
    driver.find_element(AppiumBy.XPATH, path).click()
    time.sleep(2)
