import time
import os
from pathlib import Path

from dotenv import load_dotenv
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

dotenv_path = Path('../.venv/.env')

load_dotenv(dotenv_path=dotenv_path)

options = AppiumOptions()
options.load_capabilities({
  "platformName": "Android",
  "appium:automationName": "uiautomator2",
  "appium:platformVersion": "12",
  "appium:deviceName": "Pixel 5 API 31",
  "appium:app": "C:\\Users\\acer\\Downloads\\app-staging-release.apk",
  "appium:ensureWebviewsHavePages": True,
  "appium:nativeWebScreenshot": True,
  "appium:newCommandTimeout": 3600,
  "appium:connectHardwareKeyboard": True
})
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

class Locators:
  signin_el = "//android.widget.TextView[@text='SIGN IN']"
  image_el = "//android.widget.ImageView"
  base_url_el = "//android.widget.EditText[@resource-id='base-url']"
  submit_button = "//android.widget.TextView[@text='Submit']"
  signin_button = "//android.view.ViewGroup[@resource-id='signin']"
  num_el = "//android.widget.EditText[@resource-id='phone-number-entry']"
  continue_el = "//android.widget.TextView[@text='Continue']"
  pw_el = "//android.widget.EditText[@resource-id='password']"
  showpw_el = "//android.widget.TextView[@text='']"
  login_el = "//android.view.ViewGroup[@resource-id='login']"
  dont_allow = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']"
  deny_location = "//android.widget.TextView[@text='Deny']"
  menu_el = "//android.widget.TextView[@text='']"


class LogInPage:

  def __init__(self, driver):
    self.driver = driver
    self.signin_el = Locators.signin_el
    self.image_el = Locators.image_el
    self.base_url_el = Locators.base_url_el
    self.submit_button = Locators.submit_button
    self.signin_button = Locators.signin_button
    self.num_el = Locators.num_el
    self.continue_el = Locators.continue_el
    self.pw_el = Locators.pw_el
    self.showpw_el = Locators.showpw_el
    self.login_el = Locators.login_el
    self.dont_allow = Locators.dont_allow
    self.deny_location = Locators.deny_location
    self.menu_el = Locators.menu_el

  def initial(self):
    print("call bhayo?")

    # waits until fully loaded
    self.driver.implicitly_wait(30)
    self.title = self.driver.find_element(By.XPATH, self.signin_el).text
    print(f"element: {self.title}")
    assert "SIGN" in self.title
    print("sign in page verified")
    time.sleep(1)

    self.driver.find_element(By.XPATH, self.image_el).click()

  def Base(self, url):
    self.driver.find_element(By.XPATH, self.base_url_el).send_keys(url)
    time.sleep(1)

  def Submit(self):
    self.driver.find_element(By.XPATH, self.submit_button).click()
    time.sleep(1)
    self.driver.find_element(By.XPATH, self.signin_button).click()

  def Phone(self, num):
    self.driver.find_element(By.XPATH, self.num_el).send_keys(num)
    time.sleep(1)
    self.driver.find_element(By.XPATH, self.continue_el).click()
    time.sleep(1)

  def Password(self, password):
    self.driver.find_element(By.XPATH, self.pw_el).send_keys(password)

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
  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']").click()
  time.sleep(1)

  # deny location access
  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Deny']").click()
  time.sleep(2)


  # menu
  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='']").click()
  time.sleep(2)



def wrong():

  # waits until fully loaded
  driver.implicitly_wait(30)
  signEl = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='SIGN IN']").text
  assert "SIGN" in signEl
  print("sign in page verified")
  time.sleep(3)

  imageClick = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView")
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
  pword.send_keys(os.getenv('WRONGPW'))
  time.sleep(1)

  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='']").click()
  time.sleep(1)

  login = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='login']")
  login.click()
  time.sleep(2)

  #  verification
  title = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Wrong password. Try again or click Forgot password to reset it.']").text
  assert "wrong password" in title.lower()
  print("wrong password detected")


print("done")
# initial()
