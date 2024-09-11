import time

from initial import *

def orderWell():
    print("order well started.....")
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Order Well"]').click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@text="Jay-c ship-to"])[1]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Edit"]').click()
    time.sleep(1)

def edit():

    # date
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup').click()
    time.sleep(3)
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="11 September 2024"]').click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]').click()
    time.sleep(1)

    # time
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup').click()
    # driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="14"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="android:id/button1"]').click()
    time.sleep(1)

    # save changes
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Save Changes"]').click()
    print("saved")


initial()
orderWell()
edit()