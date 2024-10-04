from test_login import *
from features.MySchedule import SchedulePage

class TestMySchedule(TestLogin):

  def test_my_schedule(self, driver_setup):
    TestLogin.test_valid_login(self, driver_setup)

    my_schedule = SchedulePage(driver_setup)
    my_schedule.Schedule()