from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class FormPhoneNumberPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)
        self.phone_number_input = "//*[@id='phoneNumber']"
        self.submit_button = "//*[text()='Submit my request']"

    def click_submit_button(self):
        self.click_to_element(self.submit_button)

    def enter_phone_number(self, phone_number):
        phone_number_input = self.driver.find_element(By.XPATH, self.phone_number_input)
        phone_number_input.send_keys(phone_number)
