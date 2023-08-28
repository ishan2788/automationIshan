from datetime import datetime, time
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    InvalidElementStateException
from selenium.webdriver.support import expected_conditions as pause
from selenium.webdriver.support.ui import WebDriverWait

now = datetime.now()
ct = now.strftime("%d%m%y%H%M%S")
user_name = "ishan" + "+" + ct + "@cara.care"
name = "ishan" + "+" + ct
password = "Caracare@123"
code = "CARADIGATEST1234"
i = 0
j = 0
temp = True


def click_element(driver, index, path):
    try:
        if index == 0:
            WebDriverWait(driver, 60).until(pause.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, path)))
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, path).click()
        elif index == 1:
            WebDriverWait(driver, 60).until(pause.presence_of_element_located((AppiumBy.XPATH, path)))
            driver.find_element(AppiumBy.XPATH, path).click()
        elif index == 2:
            WebDriverWait(driver, 60).until(pause.presence_of_element_located((AppiumBy.CLASS_NAME, path)))
            driver.find_element(AppiumBy.CLASS_NAME, path).click()
        elif index == 3:
            WebDriverWait(driver, 60).until(pause.presence_of_element_located((AppiumBy.NAME, path)))
            driver.find_element(AppiumBy.NAME, path).click()
    except StaleElementReferenceException:
        time.sleep(10)
        print("StaleElementReferenceException seen in Send keys", path)
        click_element(driver, index, path)
    except InvalidElementStateException:
        time.sleep(10)
        print("StaleElementReferenceException seen in Send keys", path)
        click_element(driver, index, path)


def send_keys(driver, index, path, keys):
    try:
        if index == 0:
            WebDriverWait(driver, 60).until(pause.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, path)))
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, path).send_keys(keys)
        elif index == 1:
            WebDriverWait(driver, 60).until(pause.presence_of_element_located((AppiumBy.XPATH, path)))
            driver.find_element(AppiumBy.XPATH, path).send_keys(keys)
        elif index == 2:
            WebDriverWait(driver, 60).until(pause.presence_of_element_located((AppiumBy.CLASS_NAME, path)))
            driver.find_element(AppiumBy.CLASS_NAME, path).send_keys(keys)
        elif index == 3:
            WebDriverWait(driver, 60).until(pause.presence_of_element_located((AppiumBy.NAME, path)))
            driver.find_element(AppiumBy.NAME, path).send_keys(keys)
    except StaleElementReferenceException:
        time.sleep(10)
        print("StaleElementReferenceException seen in Send keys", path, keys)
        send_keys(driver, index, path, keys)
    except InvalidElementStateException:
        print("InvalidElementStateException seen in Send keys", path, keys)
        send_keys(driver, index, path, keys)


def go_next(driver, case):
    if case == 0:
        path = '//XCUIElementTypeOther[@name="Weiter"]'
        WebDriverWait(driver, 60).until(pause.presence_of_element_located((AppiumBy.XPATH, path)))
        driver.find_element(AppiumBy.XPATH, path).click()
    elif case == 1:
        path = '//XCUIElementTypeOther[@name="WEITER"]'
        WebDriverWait(driver, 60).until(pause.presence_of_element_located((AppiumBy.XPATH, path)))
        driver.find_element(AppiumBy.XPATH, path).click()
    time.sleep(3)


def swipe_up(driver):
    dimension = driver.get_window_size()
    v_start_x = dimension['width'] * 0.5
    v_start_y = dimension['height'] * 0.8
    v_end_x = dimension['width'] * 0.5
    v_end_y = dimension['height'] * 0.3
    driver.swipe(v_end_x, v_end_y, v_start_x, v_start_y, 1)


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
    path = '//XCUIElementTypeStaticText[@name="0"]'
    el = driver.find_element(AppiumBy.XPATH, path)
    loc = el.location
    x_scroll = dimension['width'] * 0.9
    time.sleep(2)
    driver.swipe(loc['x'], loc['y'], x_scroll, loc['y'])


def validate(driver, path):
    driver.implicitly_wait(5)
    try:
        for count in range(3):
            swipe_down(driver)
            time.sleep(2)
        driver.find_element(AppiumBy.XPATH, path).is_displayed()
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


def newfinder(driver, path, next_path):
    global temp
    try:
        np = True
        while np:
            if temp:
                try:
                    time.sleep(5)
                    driver.find_element(AppiumBy.XPATH, path).click()
                    driver.find_element(AppiumBy.XPATH, next_path).click()
                    temp = True
                except StaleElementReferenceException:
                    print("StaleElementReferenceException inside find method questionnaire (if loop) -->", path)
                    pass
            else:
                np = False
    except NoSuchElementException:
        print("In Method (find)-->Questionnaire Script-->NoSuchElement Exception seen for" + path + next_path)
        return

    except StaleElementReferenceException:
        print("In Method (find)-->Questionnaire Script-->StaleElementException seen for" + path + next_path)
        newfinder(driver, path, next_path)


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


def read_article(driver, path):
    try:
        np = True
        f_check = validate(driver, path)
        while np:
            if f_check:
                driver.implicitly_wait(10)
                driver.find_element(AppiumBy.XPATH, path).click()
                time.sleep(2)
                swipe_right(driver)
                f_check = validate(driver, path)
            else:
                np = False

    except StaleElementReferenceException:
        print("StaleElementReferenceException in method read article", path)
        read_article(driver, path)


def record_execution(driver):
    print(driver)


def stop_recording(driver):
    print(driver)


def enter_emailcode(driver):
    time.sleep(5)
    swipe_up(driver)
    time.sleep(10)
    path = '(//XCUIElementTypeStaticText[@name="Mail.messageList.cell.view.subjectLabel"])[1]'
    click_element(driver, index=1, path=path)
    email_code = check_integer(driver)
    driver.back()

    if email_code:
        pass
    else:
        path = '(//XCUIElementTypeStaticText[@name="Mail.messageList.cell.view.subjectLabel"])[1]'
        click_element(driver, index=1, path=path)
        email_code = check_integer(driver)
        driver.back()

    driver.activate_app('com.gohidoc.caraeu')
    time.sleep(2)

    driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="|"]').click()
    time.sleep(2)

    for p in range(len(email_code)):
        time.sleep(1)
        num = email_code[p]
        click_element(driver, index=0, path=num)


def check_integer(driver):
    time.sleep(5)
    el = driver.find_elements(AppiumBy.CLASS_NAME, "XCUIElementTypeStaticText")
    print(len(el))

    for p in range(len(el)):
        print(p, el[p].text)

    for m in range(len(el)):
        o = el[m].text
        if o.isdigit():
            return o
