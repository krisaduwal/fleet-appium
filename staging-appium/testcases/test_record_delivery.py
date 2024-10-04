from test_login import *
from features.RecordDelivery import RecordDeliveryPage

class TestRecordDelivery(TestLogin):

  def test_record_delivery(self, driver_setup):
    TestLogin.test_valid_login(self, driver_setup)

    record_delivery = RecordDeliveryPage(driver_setup)
    record_delivery.Delivery()
    record_delivery.Compartments("200")
    record_delivery.Submit()