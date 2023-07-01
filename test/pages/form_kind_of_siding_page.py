from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class FormKindOfSidingPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)
        self.kind_of_siding_icons = "//div[@class='kindOfSiding__item']"
        self.kind_of_siding_icons_first = "//div[@class='kindOfSiding__item'][1]"

    def count_kind_of_siding_icons(self, count):
        count_icons = count
        icons = self.driver.find_elements(By.XPATH, self.kind_of_siding_icons)
        assert len(icons) == count_icons, f"Expected {count_icons} elements, but found {len(icons)}"

    def click_first_kind_of_siding_icon(self):
        self.click_to_element(self.kind_of_siding_icons_first)
