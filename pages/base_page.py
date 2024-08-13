# File contains functions related to base page class

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import get_json_value


class BasePage:
    """Class for base page (parent page class)"""
    def __init__(self, driver):
        self.driver = driver
        self.base_url = get_json_value('base_url')  # Ger base url from parameters

    def go_to_site(self):
        """Opens base URL"""
        self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """Returns specified element with delay"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """Returns specified elements with delay"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
