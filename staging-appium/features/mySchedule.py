from features.initial import *
def schedule():
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.View").click()
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='My Schedule']").click()
    time.sleep(1)

    title = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Your Tasks in this Week']").text
    assert "your tasks in this week" in title.lower()
    print("weekly schedule verified!")
    time.sleep(5)

initial()
schedule()