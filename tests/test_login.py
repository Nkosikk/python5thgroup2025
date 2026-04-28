import time

import allure
import pytest

from pages.home_page import home_page
from pages.landing_page import landing_page
from pages.login_page import login_page
from utils.config_userInfo_properties import ReadConfig_UserInfo


class Test_login:

    dev_url = ReadConfig_UserInfo().getUrl()
    username = ReadConfig_UserInfo().getUsername()
    password = ReadConfig_UserInfo().getPassword()



    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.driver.maximize_window()

        self.hp = home_page(self.driver)
        self.hp.click_main_login_button()

        self.lp = login_page(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="login_page", attachment_type=allure.attachment_type.PNG)
        self.lp.click_login_button()

        time.sleep(5)
        self.landing_p = landing_page(self.driver)
        self.landing_p.get_welcome_message()
        allure.attach(self.driver.get_screenshot_as_png(), name="Landing_page", attachment_type=allure.attachment_type.PNG)
