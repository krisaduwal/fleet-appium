import time
from features.LogIn import *
from appium.webdriver.common.appiumby import AppiumBy


class OrderWellPage:
  def __init__(self, driver):
    self.driver = driver

    self.elem = '//android.widget.TextView[@text="Order Well"]'
    self.ver_text = '//android.view.View[@text="Order Well"]'

  def Order(self):
    elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.elem)
    elem.click()
    time.sleep(1)

  def VerifyText(self):
    ver_text = self.driver.find_element(by=AppiumBy.XPATH, value=self.ver_text).text
    assert "Order" in ver_text
    print("STAGE: ORDER! ")




