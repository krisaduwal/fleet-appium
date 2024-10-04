import time
import pytest

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from test_login import *
# from test_permissions import *
# from test_menu import *
from features.CreateAsset import CreateAssetPage

class TestCreateAsset(TestLogin):

    def test_create_asset(self, driver_setup):
        TestLogin.test_valid_login(self, driver_setup)

        create_asset = CreateAssetPage(driver_setup)
        create_asset.Create()
        create_asset.SelectCustomer()
        create_asset.SelectLocation()
        create_asset.SelectAsset()
        create_asset.SetAssetName("myasset")
        create_asset.SetCapacity("200")
        create_asset.SetPlateNum("9800")
        create_asset.SetProductType()
        create_asset.ClickCreate()
        create_asset.ToastMessage()
