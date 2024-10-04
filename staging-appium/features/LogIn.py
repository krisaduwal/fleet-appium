import time
# from pathlib import Path
#
# from dotenv import load_dotenv
# from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput


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
    self.driver.implicitly_wait(20)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.image_el).click()

  def Base(self, url):
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.base_url_el).send_keys(url)
    time.sleep(1)

  def Submit(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.submit_button).click()
    time.sleep(1)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.signin_button).click()

  def Phone(self, num):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.num_el).send_keys(num)
    time.sleep(1)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.continue_el).click()
    time.sleep(1)

  def Password(self, password):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.pw_el).send_keys(password)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.showpw_el).click()

  def LogIn(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.login_el).click()
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.dont_allow).click()
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.deny_location).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.menu_el).click()

print("done")
# initial()
