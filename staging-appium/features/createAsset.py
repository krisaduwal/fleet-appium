import random
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



PlateNum = [67867, 45699, 1212, 34345, 55656, 78778, 6656, 8877, 7777, 9858, 64676]


class Locators:
  add_customer_assets_button = "//android.widget.TextView[@text='Add Customer Assets']"
  select_customer_box = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup"
  selected_customer = "//android.widget.TextView[@text='alex_1']"

  select_location_box = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"
  selected_location = "//android.widget.TextView[@text='Delivery Instruction']"

  select_asset = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup"
  selected_asset = "//android.view.ViewGroup[@resource-id='default-generator']/android.view.ViewGroup"
  asset_name = "//android.widget.EditText[@text='Enter asset name']"
  asset_capacity = "//android.widget.EditText[@text='Enter capacity']"
  plate_num = "//android.widget.EditText[@text='Enter Licenseplate No.']"

  select_product_type = "//android.widget.TextView[@text='Choose product type']"
  selected_product_type = "//android.widget.TextView[@text='101- Package product']"

  create_button = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]"


class CreateAssetPage:

  def __init__(self, driver):
    self.driver = driver
    self.add_customer_assets_button = Locators.add_customer_assets_button
    self.select_customer_box = Locators.select_customer_box
    self.selected_customer = Locators.selected_customer
    self.select_location_box = Locators.select_location_box
    self.selected_location = Locators.selected_location
    self.select_asset = Locators.select_asset
    self.selected_asset = Locators.selected_asset
    self.asset_name = Locators.asset_name
    self.asset_capacity = Locators.asset_capacity
    self.plate_num = Locators.plate_num
    self.select_product_type = Locators.select_product_type
    self.selected_product_type = Locators.selected_product_type
    self.create_button = Locators.create_button

  def Create(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.add_customer_assets_button).click()
    time.sleep(2)

  def SelectCustomer(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.select_customer_box).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.selected_customer).click()
    time.sleep(1)

  def SelectLocation(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.select_location_box).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.selected_location).click()
    time.sleep(1)

  def SelectAsset(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.select_asset).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.selected_asset).click()
    time.sleep(1)

  def SetAssetName(self, name):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.asset_name).send_keys(name)
    time.sleep(1)

  def SetCapacity(self, capacity):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.asset_capacity).send_keys(capacity)
    time.sleep(1)

  def SetPlateNum(self, plate_num):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.plate_num).send_keys(plate_num)
    # (random.choice(PlateNum))
    time.sleep(1)

  def SetProductType(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.select_product_type).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.selected_product_type).click()
    time.sleep(1)

  def ClickCreate(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.create_button).click()

  def ToastMessage(self):
    try:
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Asset')]"))
      )

      toast_message_text = toast_message_element.text

      assert "Asset" in toast_message_text
      print("Toast message verified, new order schedule created!")

    except Exception as e:
      print("Failed to verify toast message: {str(e)}")

