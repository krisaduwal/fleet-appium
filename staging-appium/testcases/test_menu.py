import time

from test_permissions import *

def test_menu():
    test_deny()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text=""]').click()
    time.sleep(1)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Fuelpanda"]').text
    assert "fuelpanda" in title.lower()
    print("menu.. ")

def test_today():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.View').click()
    driver.implicitly_wait(5)
    try:
        body = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Great! you do not have any tasks right now to perform"]').text
        assert "great" in body.lower()
        print("no tasks today")

    except:
        print("some tasks")

def test_schedule():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="My Schedule"]').click()
    driver.implicitly_wait(5)
    body = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Your Tasks in this Week"]').text
    assert "your tasks in this week" in body.lower()
    print("Your weekly schedule")
    try:
        list = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Your list is empty"]').text
        assert "your list is empty" in list.lower()
        print("you don't have any tasks")
    except:
        print("your task list!")

def test_recordLoad():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Record Load Order"]').click()
    driver.implicitly_wait(5)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Record Load Order"]').text
    assert "record load order" in title.lower()
    print("record load order page loaded")

def test_recordDelivery():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Record Delivery Order"]').click()
    driver.implicitly_wait(5)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Select Customer"]').text
    assert "select customer" in title.lower()
    print("record delivery order page loaded")

def test_scheduleLoad():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Schedule Load Order"]').click()
    driver.implicitly_wait(5)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Schedule Load Order"]').text
    assert "schedule load order" in title.lower()
    print("schedule load order page loaded")

def test_scheduleDelivery():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Schedule Delivery Order"]').click()
    driver.implicitly_wait(5)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Schedule Delivery Order"]').text
    assert "schedule delivery order" in title.lower()
    print("schedule delivery order page loaded")

def test_orderWell():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Order Well"]').click()
    driver.implicitly_wait(5)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Order Well"]').text
    assert "order well" in title.lower()
    print("order well page loaded")


def test_recordFuel():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Record Fuel Transfer"]').click()
    driver.implicitly_wait(5)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Record Fuel Transfer"]').text
    assert "record fuel transfer" in title.lower()
    print("record fuel transfer page loaded")

def test_addCustomer():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Add Customer Assets"]').click()
    driver.implicitly_wait(5)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Create Asset"]').text
    assert "create asset" in title.lower()
    print("add customer asset page loaded")

def test_assignBarcode():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Assign QR/Barcode to assets"]').click()
    driver.implicitly_wait(5)
    body = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Stick the QR/Barcode code onto the Asset and Scan"]').text
    assert "stick the qr" in body.lower()
    print("QR assign page loaded")

def test_blendCalculator():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Blend Calculator"]').click()
    driver.implicitly_wait(5)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Blend Calculator"]').text
    assert "blend calculator" in title.lower()
    print("blend calculator page loaded")
    #
    # try:
    #     body = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='You either don't have active shift or haven't taken any vehicle']").text
    #     assert "you either" in body.lower()
    #     print("no active shift or vehicle")
    #
    # finally:
    #     print("shifts available")

def test_settings():
    test_menu()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Settings"]').click()
    driver.implicitly_wait(5)
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@text="Settings"]').text
    assert "settings" in title.lower()
    print("settings page loaded")
