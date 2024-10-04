import time

from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from features.LogIn import *

class ScheduleLoadPage:

  def __init__(self, driver):
    self.driver = driver
    self.click_el = "//android.widget.TextView[@text='Schedule Load Order']"
    self.search_terminal = "//android.widget.EditText[@resource-id='search']"
    self.select_terminal = "//android.view.ViewGroup[@resource-id='cell-0']"
    self.product_el = "//android.view.ViewGroup[@resource-id='product-0']"
    self.select_product = "//android.view.ViewGroup[@resource-id='default-101010']/android.view.ViewGroup"
    self.gross_el = "//android.widget.EditText[@resource-id='vol-0']"
    self.supplier_el = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]"
    self.select_supplier = "//android.widget.TextView[@text='Aditya Supplier']"
    self.submit_el = "//android.view.ViewGroup[@resource-id='submit']"

  def Schedule(self):
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.click_el).click()
    time.sleep(1)

  def Terminal(self, terminal):
    # search for terminal
    self.driver.find_element(by=AppiumBy.XPATH, value=self.search_terminal).send_keys(terminal)
    # terminal ocean value
    time.sleep(1)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.select_terminal).click()
    time.sleep(1)

  def Product(self):
    # select product
    self.driver.find_element(by=AppiumBy.XPATH, value=self.product_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.select_product).click()

  def Gross(self, gross):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.gross_el).send_keys(gross)
    time.sleep(1)

  def Supplier(self):
    # select supplier
    self.driver.find_element(by=AppiumBy.XPATH, value=self.supplier_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.select_supplier).click()
    time.sleep(2)

    self.driver.find_element(by=AppiumBy.XPATH, value=self.submit_el).click()

    # verify toast message
    try:
      # Wait for the toast message to appear with explicit wait
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'New')]"))
      )

      # Get the text from the toast message
      toast_message_text = toast_message_element.text

      # Verify that the toast message contains the word "Transfer"
      assert "New Order" in toast_message_text
      print("Toast message verified, new order schedule created!")

    except Exception as e:
      print("Failed to verify toast message: {str(e)}")

