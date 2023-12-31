from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class FormTypeOfProjectPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)
        self.type_of_project_icons = "//*[@id='StepBodyId']/div/div/div/div"
        self.type_of_project_icons_first = "//*[@id='StepBodyId']/div/div/div/div[1]"
        self.repair_section = "//*[text()='Repair ']"
        self.no_button = "//*[text()='No']"
        self.yes_button = "//*[text()='Yes']"

    def count_type_of_project_icons(self, count):
        self.driver.implicitly_wait(10)
        count_icons = count
        icons = self.driver.find_elements(By.XPATH, self.type_of_project_icons)
        assert len(icons) == count_icons, f"Expected {count_icons} elements, but found {len(icons)}"

    def click_first_type_of_project_icon(self):
        self.click_to_element(self.type_of_project_icons_first)

    def click_repair_section_icon(self):
        self.click_to_element(self.repair_section)

    def click_no_button(self):
        self.click_to_element(self.no_button)

    def click_yes_button(self):
        self.click_to_element(self.yes_button)

    def assert_no_button_visible(self):
        no_button = self.driver.find_element(By.XPATH, self.no_button)
        assert no_button.is_displayed()

    def assert_yes_button_visible(self):
        yes_button = self.driver.find_element(By.XPATH, self.yes_button)
        assert yes_button.is_displayed()
