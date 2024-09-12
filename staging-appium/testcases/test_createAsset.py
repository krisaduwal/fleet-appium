import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from test_login import *
from test_permissions import *

from test_menu import *


def test_createProcess():
    test_addCustomer()
    # select customer
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="100 ASSETS CUSTOMER"]').click()
    time.sleep(2)

    # select location
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="100 Assets -customer -shipto"]').click()
    time.sleep(1)

def test_tank():
    test_createProcess()
    # select asset type
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="tank"]').click()
    time.sleep(2)

    verifyEl = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Tank Unique Id *"]').text
    assert "tank unique id" in verifyEl.lower()
    print("tank asset selected")

    # asset name
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter asset name"]').send_keys('my tankkk')
    time.sleep(1)

    # fuel capacity
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter capacity"]').send_keys(655)
    time.sleep(1)

    # tank id
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter Tank ID"]').send_keys(6566)
    time.sleep(1)

    # tank length
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter Length (In feet)"]').send_keys(15)
    time.sleep(1)

    # tank diameter
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter Diamater (In feet)"]').send_keys(7)
    time.sleep(1)

    # select product type
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Choose product type"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="101- Package product"]').click()
    time.sleep(1)

    test_createButton()
    print("tank asset created")

def test_vehicle():
    test_createProcess()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Choose asset type"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="vehicle"]').click()
    time.sleep(1)

    # asset name
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter asset name"]').send_keys("my vehicle")
    time.sleep(1)

    # fuel capacity
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter capacity"]').send_keys("400")
    time.sleep(1)

    # license plate num
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Enter Licenseplate No."]').send_keys("7909")
    time.sleep(1)

    # product type
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Choose product type"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="101- Package product"]').click()
    time.sleep(2)

    test_createButton()
    print("vehicle asset added")

def test_createButton():
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Create"]').click()
    try:
        # Wait for the toast message to appear with explicit wait
        toast_message_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Asset')]"))
        )

        # Get the text from the toast message
        toast_message_text = toast_message_element.text

        # Verify that the toast message contains the word "Transfer"
        assert "asset" in toast_message_text.lower()
        print("Toast message verified, asset created!")

    except Exception as e:
        print("Failed to verify toast message: {str(e)}")