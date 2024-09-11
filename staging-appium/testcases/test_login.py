import pytest

from features.initial import *

dotenv_path = Path('../.venv/.env')

load_dotenv(dotenv_path=dotenv_path)

def setUp():
    driver.implicitly_wait(30)

    # waits until fully loaded
    driver.implicitly_wait(30)
    signEl = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='SIGN IN']").text
    assert "SIGN" in signEl
    print("sign in page verified")
    time.sleep(3)

    imageClick = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView")
    imageClick.click()

    driver.implicitly_wait(20)
    base = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='base-url']")
    base.send_keys("test.fleetpanda.com")
    time.sleep(2)

    submit = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Submit']")
    submit.click()
    time.sleep(2)

    signIn = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='signin']")
    signIn.click()
    time.sleep(2)

@pytest.mark.xfail
def test_incorrectPassword():
    setUp()

    num = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='phone-number-entry']")
    num.send_keys(os.getenv('NUM'))
    time.sleep(2)

    con = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Continue']")
    con.click()
    time.sleep(2)

    pword = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='password']")
    pword.send_keys(os.getenv('WRONGPW'))
    time.sleep(1)

    driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='']").click()
    time.sleep(1)

    login = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='login']")
    login.click()
    time.sleep(2)

    #  verification
    title = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Wrong password. Try again or click Forgot password to reset it.']").text
    assert "wrong password" in title.lower()
    print("wrong password detected")


@pytest.mark.xfail
def test_incorrectNum():
    setUp()

    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="phone-number-entry"]').send_keys(os.getenv('WRONGNUM'))
    time.sleep(2)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue"]').click()

    # verify
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="This phone number is not registered in the system. Please contact your administrator to set it up."]').text
    assert "this phone number is not registered in the system" in title.lower()
    print("phone number not registered")

@pytest.mark.skip
def test_correct():
    setUp()

    num = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='phone-number-entry']")
    num.send_keys(os.getenv('NUM'))
    time.sleep(2)

    con = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Continue']")
    con.click()
    time.sleep(2)

    pword = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='password']")
    pword.send_keys(os.getenv('PWORD'))
    time.sleep(1)

    # driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='']").click()
    # time.sleep(1)

    login = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id='login']")
    login.click()
    time.sleep(2)

    #  verification
    title = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.android.permissioncontroller:id/permission_message"]').text
    assert "allow staging fleetpanda" in title.lower()
    print("login successfull!")
