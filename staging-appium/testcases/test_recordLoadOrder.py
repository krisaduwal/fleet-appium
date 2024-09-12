import time

from test_menu import *

def test_load():
    test_recordLoad()
    time.sleep(1)

    # date
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="date"]').click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="10 September 2024"]').click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]').click()
    time.sleep(1)

    # time
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="time"]').click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]').click()
    time.sleep(1)

    # truck
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="asset-0"]').click()
    driver.implicitly_wait(5)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="107 - LCR"]').click()
    time.sleep(1)

    # trailer
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="asset-1"]').click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="AG Trailer 1"]').click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="asset-2"]').click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="AG Trailer 101"]').click()
    time.sleep(1)

    