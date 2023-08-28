from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "com.gohidoc.caraeu.MainActivity",
            "appPackage": "com.gohidoc.caraeu",
            "noReset": "true"

        }

time = datetime.now()
ct = time.strftime("%d%m%y%H%M%S")
user_name = "ishan" + "+" + ct + "@cara.care"
name = "ishan" + "+" + ct
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dc)
driver.implicitly_wait(45)


def vertical_swipe(d, e):
    dimension = d.get_window_size()
    v_start_x = e['x']
    v_start_y = e['y']
    v_end_x = dimension['width'] * 0.4
    v_end_y = e['y']
    driver.swipe(v_start_x, v_start_y, v_end_x, v_end_y, 1)


path = '(//android.widget.TextView[@text = "0"])'
element_location = driver.find_element(AppiumBy.XPATH, path).location

print(element_location)

vertical_swipe(driver, element_location)
path = '(//android.widget.TextView[@text = "Weiter"])'
driver.find_element(AppiumBy.XPATH, path).click()
