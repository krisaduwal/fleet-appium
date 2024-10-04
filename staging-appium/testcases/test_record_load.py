from test_login import *
from features.RecordLoad import RecordLoadPage

class TestRecordLoad(TestLogin):

  def test_record_load(self, driver_setup):
    TestLogin.test_valid_login(self, driver_setup)

    record_load = RecordLoadPage(driver_setup)
    record_load.Load()
    record_load.AddBOL()
    record_load.BolNum("5567")
    record_load.CardTime()
    record_load.Supplier()
    record_load.Carrier()
    record_load.Product()
    record_load.Gross("12")
    record_load.Net("12")
    record_load.Breakdown("12")
    record_load.Next()
