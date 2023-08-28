import time
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# from get_AccessCode import AccessCodes
from iOS.IBS.functions_iRD import click_element, send_keys

Desired_Capabilities = {
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

now = datetime.now()
ct = now.strftime("%d%m%y%H%M%S")
user_name = "ishan" + "+" + ct + "@cara.care"
name = "ishan" + "+" + ct
password = "Caracare@123"
access_code = '77AAAAAAAAAAAAAX'
print(user_name)
phone = '+4912345678'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Desired_Capabilities)
driver.implicitly_wait(30)

time.sleep(5)
driver.close_app()
time.sleep(5)

driver.launch_app()
time.sleep(5)

driver.find_element(AppiumBy.ACCESSIBILITY_ID, "new_account").click()
path = '(//XCUIElementTypeOther[@name="select_IBS_program"])[1]'
driver.find_element(AppiumBy.XPATH, path).click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "continue").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "confirm").click()

path = '//XCUIElementTypeStaticText[@name="Ich bin mindestens 18 Jahre alt."]'
driver.find_element(AppiumBy.XPATH, path).click()

path = '//XCUIElementTypeStaticText[@name="Ich bin unter 70 Jahre alt."]'
driver.find_element(AppiumBy.XPATH, path).click()

path = '//XCUIElementTypeStaticText[@name="Ich bin nicht schwanger."]'
driver.find_element(AppiumBy.XPATH, path).click()

driver.find_element(AppiumBy.ACCESSIBILITY_ID, "confirm").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "accessCodeReminderScreen_next").click()


driver.find_element(AppiumBy.ACCESSIBILITY_ID, "registrationScreen_email_input").send_keys(user_name)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "registrationScreen_password_input").send_keys(password)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "registrationScreen_repeat_password_input").send_keys(password)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "registrationScreen_access_code_input").send_keys(access_code)
time.sleep(3)
driver.hide_keyboard('tapOut')
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "registrationScreen_termsOfUse_checkbox").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "registrationScreen_privacyPolicy_checkbox").click()
dimension = driver.get_window_size()

start_x = dimension['width'] * 0.5
start_y = dimension['height'] * 0.8
end_x = dimension['width'] * 0.2
end_y = dimension['height'] * 0.4

time.sleep(5)
driver.swipe(start_x, start_y, end_x, end_y, 1)

time.sleep(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "registrationScreen_register_button").click()
time.sleep(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "emailVerificationScreen_open_email_button").click()
time.sleep(10)
driver.swipe(end_x, end_y, start_x, start_y, 1)
time.sleep(10)

path = '(//XCUIElementTypeStaticText[@name="Mail.messageList.cell.view.subjectLabel"])[1]'
driver.find_element(AppiumBy.XPATH, path).click()

path = '//XCUIElementTypeStaticText[@name="E-Mail-Adresse bestätigen"]'
driver.find_element(AppiumBy.XPATH, path).click()

time.sleep(10)
driver.launch_app()
time.sleep(5)

click_element(driver, index=0, path='appUsageScreen_next_button')
send_keys(driver, index=0, path="setNicknameScreen_name_input", keys=name)

driver.hide_keyboard('tapOut')
click_element(driver, index=0, path='setNicknameScreen_next_button')

send_keys(driver, index=0, path="mobilePhoneScreen.numberInput", keys=phone)
click_element(driver, index=0, path='confirm')

time.sleep(30)
driver.quit()
