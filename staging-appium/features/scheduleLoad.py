import time

from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver


from features.LogIn import *

def schedule():

    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.View").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Schedule Load Order']").click()
    time.sleep(1)

    # search for terminal
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='search']").send_keys("terminal ocean")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='cell-0']").click()
    time.sleep(1)

    # select product
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='product-0']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='default-101010']/android.view.ViewGroup").click()

    # gross
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='vol-0']").send_keys(4000)

    # select supplier
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Aditya Supplier']").click()
    time.sleep(3)

    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='submit']").click()

    # verify toast message
    try:
        # Wait for the toast message to appear with explicit wait
        toast_message_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'New')]"))
        )

        # Get the text from the toast message
        toast_message_text = toast_message_element.text

        # Verify that the toast message contains the word "Transfer"
        assert "New Order" in toast_message_text
        print("Toast message verified, new order schedule created!")

    except Exception as e:
        print("Failed to verify toast message: {str(e)}")

initial()
schedule()