from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait


class login_page:

    email_input_id = "login-email"
    password_input_id = "login-password"
    login_button_id = "login-submit"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, self.email_input_id))).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element("id", self.password_input_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element("id", self.login_button_id).click()

