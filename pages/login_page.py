# File contains functions related to login page

from selenium.webdriver.common.by import By
from utils.logger import Logger
from .base_page import BasePage


class LoginPage(BasePage):
    """Class for login page functions"""

    LOGIN_METHODS = (By.XPATH, "//div[@id='__next']/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]")
    PHONE_LOGIN = (By.XPATH, "//div[@id='__next']/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div")
    PHONE_INPUT = (By.XPATH, "//div[@id='__next']/div/div/div/div/div/div/div[2]/div/div[1]/div/form/div[1]/div/input")
    ENTER_BUTTON = (By.XPATH, "//div[@id='__next']/div/div/div/div/div/div/div[2]/div/div[1]/div/form/div[2]/button")

    def get_login_methods(self):
        """Gets available login methods number"""
        Logger.add_start_step(method='get_login_methods')
        parent_element = self.find_element(self.LOGIN_METHODS)
        child_elements = parent_element.find_elements(By.XPATH, ".//*")
        methods = set()

        # Find all non-empty methods
        for element in child_elements:
            if element.text.strip():
                methods.add(element.text)
        return methods

    def click_phone_login(self):
        """Clicks phone login method button"""
        Logger.add_start_step(method='click_phone_login')
        phone_button = self.find_element(self.PHONE_LOGIN)
        phone_button.click()
        Logger.add_end_step(method='click_phone_login', url=self.driver.current_url)

    def enter_phone(self, phone):
        """Enters phone value"""
        Logger.add_start_step(method='enter_phone')
        phone_input = self.find_element(self.PHONE_INPUT)

        phone_input.send_keys(phone)
        enter_button = self.find_element(self.ENTER_BUTTON)

        # Check if button is disabled
        is_disabled = enter_button.get_attribute('disabled') is None

        return is_disabled
