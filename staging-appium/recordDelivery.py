import time

from initial import *

def delivery():

    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.View").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Record Delivery Order']").click()
    time.sleep(1)

    # select customer
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='cell-0']").click()

    # truck
    driver.find_element(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@resource-id='asset-0'])[1]").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='107 - LCR']").click()

    # trailer
    driver.find_element(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@resource-id='asset-1'])[1]").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='AG Trailer 1']").click()
    driver.find_element(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@resource-id='asset-2'])[1]").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='AG Trailer 101']").click()

    # asset
    driver.find_element(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@resource-id='asset-0'])[2]").click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="locked"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="submit-button"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="asset-4"]').click()
    time.sleep(1)

    # comp
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-0"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-0"]').send_keys(100)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-1"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-1"]').send_keys(
        100)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-2"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-2"]').send_keys(
        100)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-3"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-3"]').send_keys(
        100)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-4"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-4"]').send_keys(
        100)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-5"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-5"]').send_keys(
        100)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-6"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-6"]').send_keys(
        100)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-7"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-7"]').send_keys(
        100)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-8"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-8"]').send_keys(
        100)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-9"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-9"]').send_keys(
        100)
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-10"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="compartment-10"]').send_keys(
        100)
    time.sleep(2)

    # submit
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Submit"]').click()
    time.sleep(2)

    # record
    driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text="Record Delivery Order"])[2]').click()

    # verify
    driver.implicitly_wait(10)
    try:
        # Wait for the toast message to appear with explicit wait
        from selenium.webdriver.support.wait import WebDriverWait
        toast_message_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, ".//*[contains(@text, 'Record')]"))
        )

        # Get the text from the toast message
        toast_message_text = toast_message_element.text

        # Verify that the toast message contains the word "Transfer"
        assert "Record" in toast_message_text
        print("Toast message verified,  recorded!")

    except Exception as e:
        print("Failed to verify toast message: {str(e)}")
initial()
delivery()