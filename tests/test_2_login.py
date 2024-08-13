# File contains tests related to login page

import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.epic("Login tests")
class Test_login_checks:
    """Class for login page tests"""

    @allure.description("Login page test")
    @pytest.mark.run(order=4)
    def test_login_page(self, driver):
        """Test for login page (general)"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_site()
        main_page.click_login()

        # Check available login methods number
        available_methods = login_page.get_login_methods()

        assert len(available_methods) == 7, "7 login methods should be available"

    @allure.description("Phone positive test")
    @pytest.mark.run(order=5)
    def test_phone_login_positive(self, driver):
        """Test for correct phone format"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_site()
        main_page.click_login()

        login_page.click_phone_login()

        # Check valid format
        result = login_page.enter_phone('12345678901')
        assert result, "11 digits input should be available"

    @allure.description("Phone negative test")
    @pytest.mark.run(order=6)
    def test_phone_login_negative(self, driver):
        """Test for invalid phone format"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_site()
        main_page.click_login()

        login_page.click_phone_login()

        # Check invalid format
        result = login_page.enter_phone('abbbccceerr')
        assert not result, "Only 11 digits input should be available"
