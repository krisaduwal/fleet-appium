from test_login import *
from features.ScheduleLoad import ScheduleLoadPage

class TestScheduleLoad(TestLogin):

  def test_schedule_load(self, driver_setup):
    TestLogin.test_valid_login(self, driver_setup)

    schedule_load = ScheduleLoadPage(driver_setup)
    schedule_load.Schedule()
    schedule_load.Terminal("terminal ocean")
    schedule_load.Product()
    schedule_load.Gross("400")
    schedule_load.Supplier()