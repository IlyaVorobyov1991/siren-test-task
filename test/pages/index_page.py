from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class IndexPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)
        self.zip_code_input = "//*[@id='zipCode']"
        self.zip_code_button = "//*[@id='zip_header']//button"
        self.zip_caption = "//*[text()='Unknown ZIP Code']"
        self.check_mark = "//*[@id='zip_header']//div[@class='rightIcon']"

    def enter_zip_code(self, zip_code):
        zip_code_input = self.driver.find_element(By.XPATH, self.zip_code_input)
        zip_code_input.send_keys(zip_code)

    def click_zip_code_button(self):
        zip_code_button = self.driver.find_element(By.XPATH, self.zip_code_button)
        zip_code_button.click()

    def assert_zip_caption_visible(self):
        zip_caption = self.driver.find_element(By.XPATH, self.zip_caption)
        assert zip_caption.is_displayed()

    def assert_check_mark_visible(self):
        check_mark = self.driver.find_element(By.XPATH, self.check_mark)
        assert check_mark.is_displayed()
