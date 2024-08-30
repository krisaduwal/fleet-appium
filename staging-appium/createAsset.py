import random
import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from initial import *

PlateNum = [67867, 45699, 1212, 34345, 55656, 78778, 6656, 8877, 7777, 9858, 64676]
# driver.quit()

def create():
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='']").click()
    time.sleep(2)

    # create
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Add Customer Assets']").click()
    time.sleep(2)

    # select customer
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup").click()
    customerSelect = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='alex_1']")
    customerSelect.click()
    time.sleep(2)

    # select location
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Delivery Instruction']").click()
    time.sleep(2)

    # select asset
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='default-generator']/android.view.ViewGroup").click()
    time.sleep(2)

    # asset name
    setName = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Enter asset name']")
    setName.send_keys("my asset")
    time.sleep(1)

    # capacity
    capacity = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Enter capacity']")
    capacity.send_keys("400")
    time.sleep(1)

    # plate num
    plate = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Enter Licenseplate No.']")
    plate.send_keys(random.choice(PlateNum))
    time.sleep(1)

    # product type
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Choose product type']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='101010']").click()
    time.sleep(1)

    # create
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]").click()

    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())

        alert = driver.switch_to.alert
        alert.accept()
        print("alert Exists in page")
    except TimeoutException:
        print("alert does not Exist in page")

    check = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout").text
    assert "Asset has been successfully created" in check
    time.sleep(1)

    driver.quit()



initial()
create()