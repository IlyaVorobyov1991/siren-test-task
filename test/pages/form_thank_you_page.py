from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class FormThankYouPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)

        self.final_thanks_text_container = "//*[@id='StepBodyId']/div/div/h4"
        self.for_thanks_icon = "//*[@class='T7hnQ5NuIFvlYFxvSytj']"

    def assert_thank_you_message(self, text):
        message = self.driver.find_element(By.XPATH, self.final_thanks_text_container)
        assert message.text == text

    def for_thanks_icon_visible(self):
        for_thanks_icon = self.driver.find_element(By.XPATH, self.for_thanks_icon)
        for_thanks_icon.is_displayed()







