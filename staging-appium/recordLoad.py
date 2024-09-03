import time

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

     # permission deny
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']").click()
initial()