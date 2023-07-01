from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class FormFullnameEmailPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)
        self.full_name_input = "//*[@id='fullName']"
        self.email_input = "//*[@id='email']"

    def enter_full_name(self, full_name):
        full_name_input = self.driver.find_element(By.XPATH, self.full_name_input)
        full_name_input.send_keys(full_name)

    def enter_email(self, email):
        email_input = self.driver.find_element(By.XPATH, self.email_input)
        email_input.send_keys(email)

