from test_login import *
from features.ScheduleDelivery import ScheduleDeliveryPage

class TestScheduleDelivery(TestLogin):

  def test_schedule_delivery(self, driver_setup):
    TestLogin.test_valid_login(self, driver_setup)

    schedule_delivery = ScheduleDeliveryPage(driver_setup)
    schedule_delivery.Schedule()
    schedule_delivery.Customer("alex")
    schedule_delivery.Create()
