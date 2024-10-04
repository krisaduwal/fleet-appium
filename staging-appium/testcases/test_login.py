import os

import pytest
from pathlib import Path
from dotenv import load_dotenv
from appium import webdriver
from appium.options.common.base import AppiumOptions

from features.LogIn import *


@pytest.fixture(scope="class")
def driver_setup(request):
  options = AppiumOptions()
  options.load_capabilities({

    "platformName": "android",
    "appium:automationName": "uiautomator2",
    "appium:platformVersion": "12",
    "appium:deviceName": "Pixel 5 API 31",
    "appium:app": "C:\\Users\\acer\\Downloads\\app-staging-release.apk",
    "appium:newCommandTimeout": 600
  })

  dotenv_path = Path('../.venv/.env')
  load_dotenv(dotenv_path=dotenv_path)

  driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

  def teardown():
    driver.quit()

  request.addfinalizer(teardown)
  return driver


@pytest.mark.usefixtures("driver_setup")
class TestLogin:

  def test_valid_login(self, driver_setup):
    login = LogInPage(driver_setup)

    login.initial()
    login.Base("test.fleetpanda.com")
    login.Submit()
    login.Phone(os.getenv("NUM"))
    login.Password(os.getenv("PWORD"))
    login.LogIn()
    print("logged in successfully")

