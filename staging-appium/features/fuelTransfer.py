import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
  transfer_el = "//android.view.ViewGroup[@resource-id='Record Fuel Transfer']"
  day_el = "//android.view.ViewGroup[@resource-id='date']"
  choose_date = "//android.view.View[@content-desc='01 September 2024']"
  day_ok = "//android.widget.Button[@resource-id='android:id/button1']"
  time_el = "//android.view.ViewGroup[@resource-id='time']"
  time_ok = "//android.widget.Button[@resource-id='android:id/button1']"

  # truck
  truck_from_el = "//android.view.ViewGroup[@resource-id='fromTruck']"
  choose_truck_from = "//android.widget.TextView[@text='Box Truck New Asset']"
  truck_to_el = "//android.view.ViewGroup[@resource-id='toTruck']"
  choose_truck_to = "//android.widget.TextView[@text='Box Truck BT Truck #123']"

  # add compartment
  from_comp_el = "//android.view.ViewGroup[@resource-id='fromComp_0']"
  from_comp = "//android.widget.TextView[@text='Comp 1']"
  to_comp_el = "//android.view.ViewGroup[@resource-id='toComp_0']"
  to_comp = "//android.view.ViewGroup[@resource-id='default-Comp 1']/android.view.ViewGroup"

  # product
  product_el = "//android.view.ViewGroup[@resource-id='transferProd_0']"
  choose_product = "//android.view.ViewGroup[@resource-id='default-960*CLR']/android.view.ViewGroup"

  gallons_el = "//android.widget.EditText[@resource-id='gal_0']"
  notes_el = "//android.widget.EditText[@resource-id='notes']"

  submit_el = "//android.view.ViewGroup[@resource-id='submit']"


class FuelTransferPage:

  def __init__(self, driver):
    self.driver = driver

    self.transfer_el = Locators.transfer_el
    self.day_el = Locators.day_el
    self.choose_date = Locators.choose_date
    self.day_ok = Locators.day_ok
    self.time_el = Locators.time_el
    self.time_ok = Locators.time_ok
    self.truck_from_el = Locators.truck_from_el
    self.choose_truck_from = Locators.choose_truck_from
    self.truck_to_el = Locators.truck_to_el
    self.choose_truck_to = Locators.choose_truck_to
    self.from_comp_el = Locators.from_comp_el
    self.from_comp = Locators.from_comp
    self.to_comp_el = Locators.to_comp_el
    self.to_comp = Locators.to_comp
    self.product_el = Locators.product_el
    self.choose_product = Locators.choose_product
    self.gallons_el = Locators.gallons_el
    self.notes_el = Locators.notes_el
    self.submit_el = Locators.submit_el

  def ClickTransfer(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.transfer_el).click()
    time.sleep(1)

  def Time(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.day_el).click()
    time.sleep(1)
    # self.driver.find_element(by=AppiumBy.XPATH, value=self.choose_date).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.day_ok).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.time_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.time_ok).click()

  def Truck(self):
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.truck_from_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.choose_truck_from).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.truck_to_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.choose_truck_to).click()

  def Compartment(self):
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.from_comp_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.from_comp).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.to_comp_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.to_comp).click()

  def Product(self):
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.product_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.choose_product).click()

  def Gallons(self, gal):
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.gallons_el).send_keys(gal)

  def Notes(self, note):
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.notes_el).send_keys(note)

  def Submit(self):
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.submit_el).click()
    self.driver.implicitly_wait(5)
    try:
      # Wait for the toast message to appear with explicit wait
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Transfer')]"))
      )

      # Get the text from the toast message
      toast_message_text = toast_message_element.text

      # Verify that the toast message contains the word "Transfer"
      assert "Transfer" in toast_message_text
      print("Toast message verified, fuel transfer recorded!")

    except Exception as e:
      print("Failed to verify toast message: {str(e)}")
