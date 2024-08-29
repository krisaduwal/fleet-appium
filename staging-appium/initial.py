import time
import os
from pathlib import Path

from dotenv import load_dotenv
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

dotenv_path = Path('.venv/.env')

load_dotenv(dotenv_path=dotenv_path)

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "uiautomator2",
    "appium:platformVersion": "15",
    "appium:deviceName": "Pixel 7a API 35",
    "appium:app": "C:\\Users\\acer\\Downloads\\app-staging-release.apk",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(538, 2198)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()

# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(407, 1957)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()

print("started")


def initial():
    print("call bhayo?")

    # waits until fully loaded
    driver.implicitly_wait(30)
    signEl = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='SIGN IN']").text
    assert "SIGN" in signEl
    print("sign in page verified")
    time.sleep(3)

    imageClick = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView")
    print("element liyo")
    imageClick.click()

    driver.implicitly_wait(20)
    base = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='base-url']")
    base.send_keys("test.fleetpanda.com")
    time.sleep(2)

    submit = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Submit']")
    submit.click()
    time.sleep(2)

    signIn = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='signin']")
    signIn.click()
    time.sleep(2)

    num = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='phone-number-entry']")
    num.send_keys(os.getenv('NUM'))
    time.sleep(2)

    con = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Continue']")
    con.click()
    time.sleep(2)

    pword = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='password']")
    pword.send_keys(os.getenv('PWORD'))
    time.sleep(1)

    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='']").click()
    time.sleep(1)

    login = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='login']")
    login.click()
    time.sleep(2)
    print("login bhayooo?!")

    # dont allow
    driver.find_element(by=AppiumBy.XPATH,
                        value="//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']").click()
    time.sleep(1)

    # deny location access
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Deny']").click()
    time.sleep(2)

    shift = driver.find_element(by=AppiumBy.XPATH,
                                value="//android.widget.TextView[@text='Great! you do not have any tasks right now to perform']").text
    assert "Great" in shift
    print("log in successful")

    # menu
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='']").click()
    time.sleep(2)

    # settings
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Settings']").click()
    time.sleep(1)

    # darkmode
    driver.find_element(by=AppiumBy.XPATH,
                        value="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()

    time.sleep(100)
    driver.quit()


print("done")
initial()
