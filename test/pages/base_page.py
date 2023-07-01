import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

        self.button_next_disabled = "//button[@disabled]"
        self.button_next = "//*[text()='Next']"

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def wait_until_is_clickable(self, locator, timeout=5):
        selector = (By.XPATH, locator)
        WebDriverWait(self.driver, timeout).until(
            element_to_be_clickable(selector)
        )

    def click_to_element(self, locator):
        self.wait_until_is_clickable(locator)
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    def button_next_disabled_visible(self):
        button_next_disabled = self.driver.find_element(By.XPATH, self.button_next_disabled)
        button_next_disabled.is_displayed()

    def button_next_click(self):
        self.click_to_element(self.button_next)
