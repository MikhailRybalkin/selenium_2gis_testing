# File contains tests related to search page

import pytest
import allure
from selenium.common import TimeoutException
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


@allure.epic("Search tests")
class Test_search_checks:
    """Class for search page tests"""

    @allure.description("Positive search test")
    @pytest.mark.run(order=1)
    def test_positive_search(self, driver):
        """Test for correct search input"""
        main_page = MainPage(driver)
        search_results_page = SearchResultsPage(driver)

        main_page.go_to_site()
        main_page.enter_search_text("аптека")
        main_page.click_enter()

        # Expect non-empty result
        results = search_results_page.get_search_results()
        assert len(results) > 0, "Search results should not be empty"

        empty_result = search_results_page.check_empty_result()
        assert not empty_result, "Something should be found"

    @allure.description("Negative search test")
    @pytest.mark.run(order=2)
    def test_negative_search(self, driver):
        """Test for incorrect search input"""
        main_page = MainPage(driver)
        search_results_page = SearchResultsPage(driver)

        main_page.go_to_site()
        main_page.enter_search_text("!!!")
        main_page.click_enter()

        # Expect empty result
        empty_result = search_results_page.check_empty_result()
        assert empty_result, "Nothing should be found"

    @allure.description("Reverse search test")
    @pytest.mark.run(order=3)
    def test_reverse_search(self, driver):
        """Test for reverse search"""
        main_page = MainPage(driver)
        search_results_page = SearchResultsPage(driver)

        main_page.go_to_site()
        main_page.reverse_map()

        try:
            # Get result for reverse search (map click)
            reverse_result = search_results_page.get_reverse_search_results()
        except TimeoutException:
            reverse_result = False

        assert reverse_result, "Reverse search results should not be empty"
