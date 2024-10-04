from test_login import *
from features.OrderWell import OrderWellPage

class TestOrderWell(TestLogin):

  def test_order_well(self, driver_setup):
    TestLogin.test_valid_login(self, driver_setup)

    order_well = OrderWellPage(driver_setup)
    order_well.Order()
    order_well.VerifyText()