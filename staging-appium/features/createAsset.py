import random
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LogIn import *

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
  selected_product_type = "//android.widget.TextView[@text='101010']"

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
    self.driver.find_element(By.XPATH, self.add_customer_assets_button).click()
    time.sleep(2)

  def SelectCustomer(self):
    self.driver.find_element(By.XPATH, self.select_customer_box).click()
    self.driver.find_element(By.XPATH, self.selected_customer).click()
    time.sleep(1)

  def SelectLocation(self):
    self.driver.find_element(By.XPATH, self.select_location_box).click()
    self.driver.find_element(By.XPATH, self.selected_location).click()
    time.sleep(1)

  def SelectAsset(self):
    self.driver.find_element(By.XPATH, self.select_asset).click()
    self.driver.find_element(By.XPATH, self.selected_asset).click()
    time.sleep(1)

  def SetAssetName(self, name):
    self.driver.find_element(By.XPATH, self.asset_name).send_keys(name)
    time.sleep(1)

  def SetCapacity(self, capacity):
    self.driver.find_element(By.XPATH, self.asset_capacity).send_keys(capacity)
    time.sleep(1)

  def SetPlateNum(self, platenum):
    self.driver.find_element(By.XPATH, self.plate_num).send_keys(platenum)
    # (random.choice(PlateNum))
    time.sleep(1)

  def SetProductType(self):
    self.driver.find_element(By.XPATH, self.select_product_type).click()
    self.driver.find_element(By.XPATH, self.selected_product_type).click()
    time.sleep(1)

  def ClickCreate(self):
    self.driver.find_element(By.XPATH, self.create_button).click()

  def Verify(self):
    try:
      WebDriverWait(self.driver, 5).until(EC.alert_is_present())

      alert = self.driver.switch_to.alert
      alert.accept()
      print("alert Exists in page")
    except TimeoutException:
      print("alert does not Exist in page")

    self.check = self.driver.find_element(by=AppiumBy.XPATH,
                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout").text
    assert "Asset has been successfully created" in self.check
    time.sleep(1)

