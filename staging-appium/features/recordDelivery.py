import time

from features.LogIn import *
class RecordDeliveryPage:

  def __init__(self, driver):
    self.driver = driver

    self.record_delivery_el = "//android.widget.TextView[@text='Record Delivery Order']"
    self.select_customer = "//android.view.ViewGroup[@resource-id='cell-0']"
    self.truck_el = "(//android.view.ViewGroup[@resource-id='asset-0'])[1]"
    self.truck_name = "//android.widget.TextView[@text='107 - LCR']"
    self.trailer1_el = "(//android.view.ViewGroup[@resource-id='asset-1'])[1]"
    self.trailer1 = "//android.widget.TextView[@text='AG Trailer 1']"
    self.trailer2_el = "(//android.view.ViewGroup[@resource-id='asset-2'])[1]"
    self.trailer2 = "//android.widget.TextView[@text='AG Trailer 101']"
    self.asset_box = "(//android.view.ViewGroup[@resource-id='asset-0'])[2]"
    self.locked_el = '//android.view.ViewGroup[@resource-id="locked"]'
    self.submit_el = '//android.view.ViewGroup[@resource-id="submit-button"]'
    self.another_asset = '//android.view.ViewGroup[@resource-id="asset-4"]'

    # comp
    self.comp0_el = '//android.widget.EditText[@resource-id="compartment-0"]'
    self.continue_el = '//android.widget.TextView[@text="Continue"]'
    self.comp1_el = '//android.widget.EditText[@resource-id="compartment-1"]'
    self.comp2_el = '//android.widget.EditText[@resource-id="compartment-2"]'
    self.comp3_el = '//android.widget.EditText[@resource-id="compartment-3"]'
    self.comp4_el = '//android.widget.EditText[@resource-id="compartment-4"]'
    self.comp5_el = '//android.widget.EditText[@resource-id="compartment-5"]'
    self.comp6_el = '//android.widget.EditText[@resource-id="compartment-6"]'
    self.comp7_el = '//android.widget.EditText[@resource-id="compartment-7"]'

    self.submit_button = '//android.widget.TextView[@text="Submit"]'
    self.record_el = '(//android.widget.TextView[@text="Record Delivery Order"])[2]'

  def Delivery(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.record_delivery_el).click()
    time.sleep(1)

    # select customer
    self.driver.find_element(by=AppiumBy.XPATH, value=self.select_customer).click()

    # truck
    self.driver.find_element(by=AppiumBy.XPATH, value=self.truck_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.truck_name).click()

    # trailer
    self.driver.find_element(by=AppiumBy.XPATH, value=self.trailer1_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.trailer1).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.trailer2_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.trailer2).click()

    # asset
    self.driver.find_element(by=AppiumBy.XPATH, value=self.asset_box).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.locked_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.submit_el).click()
    time.sleep(1)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.another_asset).click()
    time.sleep(1)

  def Compartments(self, key1):

    self.driver.find_element(by=AppiumBy.XPATH, value=self.comp0_el).click()
    time.sleep(2)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.continue_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.comp0_el).send_keys(key1)
    time.sleep(2)

  def Submit(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.submit_button).click()
    self.driver.implicitly_wait(5)
    # record
    self.driver.find_element(by=AppiumBy.XPATH, value=self.record_el).click()

    # verify
    self.driver.implicitly_wait(10)
    try:
      # Wait for the toast message to appear with explicit wait
      from selenium.webdriver.support.wait import WebDriverWait
      self.toast_message_element = self.driver.find_element(by=AppiumBy.XPATH, value= ".//*[contains(@text, 'Record')]")

      # Get the text from the toast message
      toast_message_text = self.toast_message_element.text

      # Verify that the toast message contains the word "Transfer"
      assert "Record" in toast_message_text
      print("Toast message verified,  recorded!")

    except Exception as e:
      print("Failed to verify toast message: {str(e)}")
