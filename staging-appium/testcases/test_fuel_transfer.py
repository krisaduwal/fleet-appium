from test_login import *
from features.FuelTransfer import FuelTransferPage

class TestFuelTransfer(TestLogin):

  def test_fuel_transfer(self, driver_setup):
    TestLogin.test_valid_login(self, driver_setup)

    fuel_transfer = FuelTransferPage(driver_setup)
    fuel_transfer.ClickTransfer()
    fuel_transfer.Time()
    fuel_transfer.Truck()
    fuel_transfer.Compartment()
    fuel_transfer.Product()
    fuel_transfer.Gallons("88")
    fuel_transfer.Notes("this is a note")
    fuel_transfer.Submit()