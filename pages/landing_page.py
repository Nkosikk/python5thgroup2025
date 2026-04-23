from selenium.webdriver.support.wait import WebDriverWait


class landing_page:

    welcome_message_xpath = "//h2"

    def __init__(self, driver):
        self.driver = driver

    def get_welcome_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(self.driver.find_element("xpath", self.welcome_message_xpath)).is_displayed()