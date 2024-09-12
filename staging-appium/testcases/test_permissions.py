import time

from test_login import *

def test_allow():
    # setUp()
    test_correct()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]').click()

    driver.implicitly_wait(10)
    element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Location Access"]').text
    assert "location access" in element.lower()
    print("asks for location access")

    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Allow"]').click()
    time.sleep(3)

    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/permission_location_accuracy_radio_coarse"]').click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_one_time_button"]').click()


    # verify
    driver.implicitly_wait(10)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Use precise location"]').text
    assert "use precise location" in title.lower()
    print("location permission granted")

    # back
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="Back"]').click()
    print("back to main page")
    test_verifyMain()


def test_deny():
    test_correct()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Deny"]').click()
    test_verifyMain()

def test_verifyMain():
    driver.implicitly_wait(10)
    title = driver.find_element(by=AppiumBy.XPATH,
                                value='//android.widget.TextView[@text="Great! you do not have any tasks right now to perform"]').text
    assert "great! you do not have" in title.lower()
    print("main page loaded")