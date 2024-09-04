import time

from selenium.webdriver.support import expected_conditions as EC


from initial import *

def load():
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.View").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Record Load Order']").click()
    time.sleep(1)

    # choose truck
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='asset-0']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='default-107 - LCR']/android.view.ViewGroup").click()
    time.sleep(1)

    # trailer
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='asset-1']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='AG Trailer 1']").click()
    time.sleep(1)

    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='asset-2']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='AG Trailer 101']").click()
    time.sleep(1)

    # terminal
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='cell-1']").click()
    time.sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='submit']").click()
    driver.implicitly_wait(20)

     # permission
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_one_time_button']").click()
    time.sleep(1)

    # add BOL
    #       BOL num
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='bol-number']").send_keys("444")
    time.sleep(1)
    #       upload photo
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='camera-btn']").click()
    driver.implicitly_wait(10)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Choose from Library']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.RelativeLayout").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc='Photo taken on Sep 3, 2024 10:52:31 AM']").click()
    time.sleep(2)
    #       card info
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='card-in-time']").send_keys("1515")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='card-out-time']").send_keys("1555")
    #       card date
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='card-in-date']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc='02 September 2024']").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='android:id/button1']").click()
    time.sleep(1)

    # supplier
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='supplier']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Dummy Supplier 3']").click()
    time.sleep(1)

    # carrier #
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='carrier']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='DOM999 / DOM999']").click()
    time.sleep(1)

    # product
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='select-product']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='101010']").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='total-gross']").send_keys(22)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='total-net']").send_keys(13)
    time.sleep(1)

    # breakdown
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-0']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-1']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-3']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-4']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-5']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-6']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-7']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-8']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-9']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-10']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-11']").send_keys("1")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-12']").send_keys("1")
    time.sleep(1)

    # next
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='next']").click()
initial()
load()