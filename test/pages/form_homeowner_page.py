from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class FormHomeownerPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)
        self.yes_and_no_icons = "//label[@class='vOpnsIJOviPTVA47miqg']"
        self.yes_icons = "//*[text()='Yes']"

    def count_yes_and_no_icons(self, count):
        count_icons = count
        icons = self.driver.find_elements(By.XPATH, self.yes_and_no_icons)
        assert len(icons) == count_icons, f"Expected {count_icons} elements, but found {len(icons)}"

    def click_icon(self):
        yes_icons = self.driver.find_element(By.XPATH, self.yes_icons)
        yes_icons.click()
