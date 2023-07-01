from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class FormSquareFeetPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)
        self.square_feet_input = "//*[@id='squareFeet']"

    def enter_square_feet(self, square_feet):
        square_feet_input = self.driver.find_element(By.XPATH, self.square_feet_input)
        square_feet_input.send_keys(square_feet)

