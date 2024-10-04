from features.LogIn import *

class SchedulePage:
  def __init__(self, driver):
    self.driver = driver
    self.my_schedule = "//android.widget.TextView[@text='My Schedule']"

  def Schedule(self):
    self.driver.find_element(by=AppiumBy.XPATH, value=self.my_schedule).click()
    self.driver.implicitly_wait(5)
    title = self.driver.find_element(by=AppiumBy.XPATH,
                                value="//android.widget.TextView[@text='Your Tasks in this Week']").text
    assert "your tasks in this week" in title.lower()
    print("weekly schedule verified!")
    time.sleep(5)




