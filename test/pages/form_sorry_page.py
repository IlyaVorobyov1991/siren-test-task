from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage


class FormSorryPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.BasePage = BasePage(driver, driver.current_url)

        self.go_homepage_button = "//*[text()='Go to homepage']"
        self.sorry_img = "//img[@class='rtTwREtzNqmZB_uZblKa']"
        self.text1 = "//*[@id='StepBodyId']//h3"
        self.text2 = "//div[@class='text-center h4']"

    def assert_go_homepage_button_visible(self):
        go_homepage_button = self.driver.find_element(By.XPATH, self.go_homepage_button)
        assert go_homepage_button.is_displayed()

    def assert_sorry_img_visible(self):
        go_homepage_button = self.driver.find_element(By.XPATH, self.go_homepage_button)
        assert go_homepage_button.is_displayed()

    def assert_text1(self, text):
        message = self.driver.find_element(By.XPATH, self.text1)
        assert message.text == text

    def assert_text2(self, text):
        message = self.driver.find_element(By.XPATH, self.text2)
        assert message.text == text
