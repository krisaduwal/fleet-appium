import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LogIn import *

def transfer():

  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.View").click()
  time.sleep(2)
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='Record Fuel Transfer']").click()
  time.sleep(1)

  # choose day
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='date']").click()
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc='01 September 2024']").click()
  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='android:id/button1']").click()

  #  choose time
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='time']").click()
  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='android:id/button1']").click()
  # driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='android:id/numberpicker_input' and @text='12']")
  # print("time liyo")
  # timeElement.send_keys("11")
  # driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='time']").click()
  # timeElement = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='44']")
  # actions = ActionChains(driver)
  # actions.move_to_element(timeElement).perform()
  time.sleep(2)

  # choose from truck
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='fromTruck']").click()
  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Box Truck New Asset']").click()
  time.sleep(1)

  # choose to truck
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='toTruck']").click()
  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Box Truck BT Truck #123']").click()
  time.sleep(2)

  # add compartments
  #      from compartment
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='fromComp_0']").click()
  time.sleep(1)
  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Comp 1']").click()
  time.sleep(1)
  #     to compartment
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='toComp_0']").click()
  time.sleep(1)
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='default-Comp 1']/android.view.ViewGroup").click()
  time.sleep(1)
  #    product
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='transferProd_0']").click()
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='default-960*CLR']/android.view.ViewGroup").click()
  time.sleep(1)
  #     gallons
  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='gal_0']").send_keys("500")
  time.sleep(2)

  # notes
  notes = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='notes']")
  notes.send_keys("big transfer")
  time.sleep(2)

  # submit
  driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='submit']").click()
  time.sleep(1)

  # verify
  # driver.implicitly_wait(10)
  # toast_message = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Toast")
  #
  # assert "Transfer" in toast_message.text
  # print("verified")

  try:
    # Wait for the toast message to appear with explicit wait
    toast_message_element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Transfer')]"))
    )

    # Get the text from the toast message
    toast_message_text = toast_message_element.text

    # Verify that the toast message contains the word "Transfer"
    assert "Transfer" in toast_message_text
    print("Toast message verified, fuel transfer recorded!")

  except Exception as e:
    print("Failed to verify toast message: {str(e)}")

  # toast = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Toast[1]")
  # print("verifyyyinggg")
  #
  # if toast.text == "Hello":
  #     print("toast")


  driver.quit()

initial()
transfer()