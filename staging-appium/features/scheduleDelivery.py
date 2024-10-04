from selenium.webdriver.support.wait import WebDriverWait

from features.LogIn import *

class ScheduleDeliveryPage:
  def __init__(self, driver):
    self.driver = driver
    self.click_schedule_delivery = "//android.widget.TextView[@text='Schedule Delivery Order']"
    self.search_el = "//android.widget.EditText[@resource-id='search']"
    self.select_customer = "//android.view.ViewGroup[@resource-id='cell-0']"
    self.create_el = "//android.view.ViewGroup[@resource-id='customer']"
    self.name_el = "//android.widget.TextView[@text='Jay-c ship-to']"
    self.submit_el = "//android.view.ViewGroup[@resource-id='submit']"

  def Schedule(self):
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.click_schedule_delivery).click()
    time.sleep(1)

  def Customer(self, name):
    # search for customer
    self.driver.find_element(by=AppiumBy.XPATH, value=self.search_el).send_keys(name)
    self.driver.implicitly_wait(5)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.select_customer).click()
    time.sleep(1)

  def Create(self):
    # create order
    self.driver.find_element(by=AppiumBy.XPATH, value=self.create_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.name_el).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.submit_el).click()

    # verify
    try:
      # Wait for the toast message to appear with explicit wait
      from telnetlib import EC
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'New')]"))
      )

      # Get the text from the toast message
      toast_message_text = toast_message_element.text

      # Verify that the toast message contains the word "Transfer"
      assert "New Order" in toast_message_text
      print("Toast message verified, new order created!")

    except Exception as e:
      print("Failed to verify toast message: {str(e)}")





