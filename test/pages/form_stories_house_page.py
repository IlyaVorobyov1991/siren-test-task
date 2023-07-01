from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class FormStoriesHousePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)
        self.count_stories_icons_locator = "//div[@class='QWb89qL6CSRSH4U1BmAQ']"
        self.stories_icons_first = "//div[@class='QWb89qL6CSRSH4U1BmAQ'][1]"

    def count_stories_icons(self, count):
        count_icons = count
        icons = self.driver.find_elements(By.XPATH, self.count_stories_icons_locator)
        assert len(icons) == count_icons, f"Expected {count_icons} elements, but found {len(icons)}"

    def click_first_count_stories_icon(self):
        self.click_to_element(self.stories_icons_first)
