from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class FormConfirmPhoneNumberPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)
        self.submit_correct_button = "//*[text()='Phone number is correct']"

    def click_submit_correct_button(self):
        self.click_to_element(self.submit_correct_button)








