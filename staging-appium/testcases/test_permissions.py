import time

from test_login import *

def test_permission():
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
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="Back"]').click()

    title = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@text='Today's Shift']").text
    assert "today's shift" in title.lower()
    print("main page loaded")

