from datetime import datetime, timedelta
from features.initial import *

def load():
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.View").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Record Load Order']").click()
    time.sleep(1)

    # choose truck
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='asset-0']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='default-107 - LCR']/android.view.ViewGroup").click()
    time.sleep(4)

    # trailer
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='asset-1']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='AG Trailer 1']").click()
    time.sleep(1)

    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='asset-2']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='AG Trailer 101']").click()
    time.sleep(1)

    # terminal
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='cell-2']").click()
    time.sleep(2)

    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='submit']").click()
    print("load selection done")
    driver.implicitly_wait(20)

def addBOL():

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

    #       card date
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='card-in-date']").click()
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc='02 September 2024']").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='android:id/button1']").click()
    time.sleep(1)

    # card out time
    current_time = datetime.now()

    # Add 5 minutes to the current time
    new_time = current_time + timedelta(minutes=5)

    # Format the time to display only hours, minutes, and seconds
    outTime = new_time.strftime("%H%M")
    # time.sleep(1)

    # print(outTime)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='card-out-time']").click()

    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='card-out-time']").send_keys(outTime)

    time.sleep(5)

    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup').click()
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
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='comp-0']").send_keys("13")
    # time.sleep(1)
    time.sleep(1)

    # next
    driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='next']").click()
    print("BOL details added")


def delayCheck():

    # delay check
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@resource-id="delay-yes"]').click()
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="delay-reason"]').send_keys("technical problem")
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Done Loading"]').click()

    # verify toast message
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
        assert "record was successfully created" in toast_message_text.lower()
        print("Toast message verified, load order recorded!")

    except Exception as e:
        print("Failed to verify toast message: {str(e)}")



initial()
load()
addBOL()
delayCheck()