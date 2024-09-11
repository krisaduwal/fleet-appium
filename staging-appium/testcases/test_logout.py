import time

from selenium.webdriver.common.by import By

from test_login import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_inactivity():
    test_correct()
    try:

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Great! you do not have any tasks right now to perform"]'))
        )
        print("going to logout")
    except:
        print("log out successful")
        driver.quit()

