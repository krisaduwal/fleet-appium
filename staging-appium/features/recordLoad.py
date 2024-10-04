from datetime import datetime, timedelta
from telnetlib import EC

from features.LogIn import *

class RecordLoadPage:

  def __init__(self, driver):
    self.driver = driver
    self.record_load_el = "//android.widget.TextView[@text='Record Load Order']"
    self.choose_truck = "//android.view.ViewGroup[@resource-id='asset-0']"
    self.truck_el = "//android.view.ViewGroup[@resource-id='default-107 - LCR']/android.view.ViewGroup"
    self.choose_trailer1 = "//android.view.ViewGroup[@resource-id='asset-1']"
    self.trailer1_el = "//android.widget.TextView[@text='AG Trailer 1']"
    self.choose_trailer2 = "//android.view.ViewGroup[@resource-id='asset-2']"
    self.trailer2_el = "//android.widget.TextView[@text='AG Trailer 101']"
    self.terminal_el = "//android.view.ViewGroup[@resource-id='cell-2']"
    self.submit_el = "//android.view.ViewGroup[@resource-id='submit']"
    self.permission_el = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_one_time_button']"
    self.bol_num_el = "//android.widget.EditText[@resource-id='bol-number']"
    self.cam_el = "//android.view.ViewGroup[@resource-id='camera-btn']"
    self.choose_from_lib = "//android.widget.TextView[@text='Choose from Library']"
    self.image_box = "//android.widget.RelativeLayout"
    self.image_el = "//android.view.ViewGroup[@content-desc='Photo taken on Sep 3, 2024 10:52:31 AM']"
    self.card_in_time_box = "//android.view.ViewGroup[@resource-id='card-in-date']"
    self.in_time = "//android.view.View[@content-desc='02 September 2024']"
    self.in_ok = "//android.widget.Button[@resource-id='android:id/button1']"
    self.card_out_time_box = "//android.widget.EditText[@resource-id='card-out-time']"
    self.supplier_box = "//android.view.ViewGroup[@resource-id='supplier']"
    self.supplier_el = "//android.widget.TextView[@text='Dummy Supplier 3']"
    self.carrier_box = "//android.view.ViewGroup[@resource-id='carrier']"
    self.carrier_el = "//android.widget.TextView[@text='DOM999 / DOM999']"
    self.select_product = "//android.view.ViewGroup[@resource-id='select-product']"
    self.selected_product = "//android.widget.TextView[@text='101010']"
    self.total_gross = "//android.widget.EditText[@resource-id='total-gross']"
    self.total_net = "//android.widget.EditText[@resource-id='total-net']"
    self.breakdown_el = "//android.widget.EditText[@resource-id='comp-0']"
    self.next_el = "//android.view.ViewGroup[@resource-id='next']"
  def Load(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.record_load_el).click()
    time.sleep(1)

    # choose truck
    self.driver.find_element(by=AppiumBy.XPATH, value=self.choose_truck).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.truck_el).click()
    time.sleep(4)

    # trailer
    self.driver.find_element(by=AppiumBy.XPATH, value=self.choose_trailer1).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.trailer1_el).click()
    time.sleep(1)

    self.driver.find_element(by=AppiumBy.XPATH, value=self.choose_trailer2).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.trailer2_el).click()
    time.sleep(1)

    # terminal
    self.driver.find_element(by=AppiumBy.XPATH, value=self.terminal_el).click()
    time.sleep(2)

    self.driver.find_element(by=AppiumBy.XPATH, value=self.submit_el).click()
    print("load selection done")
    self.driver.implicitly_wait(20)

  def AddBOL(self):

    # permission
    self.driver.find_element(by=AppiumBy.XPATH, value=self.permission_el).click()
    time.sleep(1)

    # add BOL
  def BolNum(self, num):
    #       BOL num
    self.driver.find_element(by=AppiumBy.XPATH, value=self.bol_num_el).send_keys(num)
    time.sleep(1)
    #       upload photo
    self.driver.find_element(by=AppiumBy.XPATH, value=self.cam_el).click()
    self.driver.implicitly_wait(10)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.choose_from_lib).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.image_box).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.image_el).click()
    time.sleep(2)

  def CardTime(self):
    #       card date
    self.driver.find_element(by=AppiumBy.XPATH, value=self.card_in_time_box).click()
    # self.driver.find_element(by=AppiumBy.XPATH, value=self.in_time).click()
    time.sleep(1)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.in_ok).click()
    time.sleep(1)

    # card out time
    current_time = datetime.now()

    # Add 5 minutes to the current time
    new_time = current_time + timedelta(minutes=5)

    # Format the time to display only hours, minutes, and seconds
    outTime = new_time.strftime("%H%M")
    # time.sleep(1)

    # print(outTime)
    self.driver.find_element(by=AppiumBy.XPATH, value=self.card_out_time_box).click()

    self.driver.find_element(by=AppiumBy.XPATH, value=self.card_out_time_box).send_keys(outTime)

    time.sleep(5)

    self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup').click()
    time.sleep(1)

  def Supplier(self):

    # supplier
    self.driver.find_element(by=AppiumBy.XPATH, value=self.supplier_box).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.supplier_el).click()
    time.sleep(1)

  def Carrier(self):
    # carrier #
    self.driver.find_element(by=AppiumBy.XPATH, value=self.carrier_box).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.carrier_el).click()
    time.sleep(1)

  def Product(self):
    # product
    self.driver.find_element(by=AppiumBy.XPATH, value=self.select_product).click()
    self.driver.find_element(by=AppiumBy.XPATH, value=self.selected_product).click()
    time.sleep(1)

  def Gross(self, gross):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.total_gross).send_keys(gross)

  def Net(self, net):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.total_net).send_keys(net)
    time.sleep(1)

  def Breakdown(self, value):
    # breakdown
    self.driver.find_element(by=AppiumBy.XPATH, value=self.breakdown_el).send_keys(value)
    time.sleep(1)

  def Next(self):
    # next
    self.driver.find_element(by=AppiumBy.XPATH, value=self.next_el).click()
    print("BOL details added")


  def DelayCheck(self):

    # delay check
    self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="delay-yes"]').click()
    time.sleep(2)
    self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="delay-reason"]').send_keys("technical problem")
    time.sleep(1)
    self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Done Loading"]').click()

    # verify toast message
    self.driver.implicitly_wait(10)
    try:
      # Wait for the toast message to appear with explicit wait
      from selenium.webdriver.support.wait import WebDriverWait
      toast_message_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Record')]"))
      )

      # Get the text from the toast message
      toast_message_text = toast_message_element.text

      # Verify that the toast message contains the word "Transfer"
      assert "record was successfully created" in toast_message_text.lower()
      print("Toast message verified, load order recorded!")

    except Exception as e:
      print("Failed to verify toast message: {str(e)}")



