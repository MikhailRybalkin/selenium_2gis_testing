# File contains tests related to additional pages

import pytest
import allure
from pages.main_page import MainPage
from utils.helpers import get_json_value

API_PAGE_EXPECTED_URL = get_json_value('api_info_url')


@allure.epic("Other pages tests")
class Test_other_pages_checks:
    """Class for other pages tests"""

    @allure.description("API info page test")
    @pytest.mark.run(order=7)
    def test_api_page(self, driver):
        """Test for API info page"""
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.open_api_page()

        # Switch window and check URL
        tabs = driver.window_handles
        driver.switch_to.window(tabs[-1])
        current_url = driver.current_url

        assert current_url == API_PAGE_EXPECTED_URL, "Unexpected URL for API page"
