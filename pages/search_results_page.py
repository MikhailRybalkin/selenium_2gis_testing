# File contains functions related to search page

import allure
from selenium.webdriver.common.by import By
from utils import helpers
from utils.logger import Logger
from .base_page import BasePage


class SearchResultsPage(BasePage):
    """Class for search page functions"""

    RESULTS_PATH = "//div[@id='root']/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div"
    REVERSE_RESULTS_PATH = "//div[@id='root']/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]"
    RESULTS = (By.XPATH, RESULTS_PATH)
    REVERSE_RESULTS = (By.XPATH, REVERSE_RESULTS_PATH)
    EMPTY_RESULT = (By.XPATH, RESULTS_PATH + "/div[2]/div/h1")

    def get_search_results(self):
        """Gets search results"""
        with allure.step("Search page"):  # allure step
            Logger.add_start_step(method='get_search_results')
            return self.find_elements(self.RESULTS)

    def check_empty_result(self):
        """Checks that result is empty"""
        nothing_found = False

        try:
            with allure.step("Search page"):  # allure step
                Logger.add_start_step(method='check_empty_result')
                parent_element = self.find_element(self.RESULTS)
                nothing_found = helpers.find_text(parent_element, 'Ничего не нашлось, попробуйте уточнить запрос')  # Key text for empty result

        except Exception as ex:
            error_message = f"Can not check empty result: {ex}"
            print(error_message)
            Logger.write_log_to_file(error_message)

        return nothing_found

    def get_reverse_search_results(self):
        """Checks that reverse result is not empty"""
        nothing_found = False

        try:
            with allure.step("Search page"):  # allure step
                Logger.add_start_step(method='get_reverse_search_results')
                parent_element = self.find_element(self.REVERSE_RESULTS)
                nothing_found = helpers.find_text(parent_element, '°')  # Key text for non-empty result

        except Exception as ex:
            error_message = f"Can not get reverse results: {ex}"
            print(error_message)
            Logger.write_log_to_file(error_message)

        return nothing_found
