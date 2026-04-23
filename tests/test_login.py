import pytest

from pages.home_page import home_page
from utils.config_userInfo_properties import ReadConfig_UserInfo


class Test_login:

    dev_url = ReadConfig_UserInfo().getUrl()
    username = ReadConfig_UserInfo().getUsername()
    password = ReadConfig_UserInfo().getPassword()



    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.driver.maximize_window()

        self.hp = home_page(self.driver)
        self.hp.click_main_login_button()
