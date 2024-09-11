import time

from test_login import *

def test_inactivity():
    try:
        test_correct()
        inactivity = 20
        print(f"waiting for {inactivity} seconds before logout")
        time.sleep(inactivity)
        try:
            driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='')
        except :

    finally:
        print("logged out")
