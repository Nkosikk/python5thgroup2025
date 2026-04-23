import time

import pytest
from selenium import webdriver


class TestBasicLogin:

    @pytest.mark.basic
    def test_genericTest(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://ndosisimplifiedautomation.vercel.app/")
        time.sleep(20)
        self.driver.maximize_window()
        self.driver.find_element("xpath", "//div[@class='nav-user-section']").click()
        self.driver.find_element("id", "login-email").send_keys("nkwanyana@gmail.com")
        self.driver.find_element("id", "login-password").send_keys("@12345678")
        self.driver.find_element("id", "login-submit").click()

        time.sleep(30)

# basic_login = TestBasicLogin()
# basic_login.genericTest()