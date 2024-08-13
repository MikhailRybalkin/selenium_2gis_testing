# File contains functions related to main page

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utils.logger import Logger
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    """Class for main page functions"""
    
    SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Поиск в 2ГИС']")
    MAP_WINDOW = (By.XPATH, "//div[@id='map']")
    WHAT_HERE_CONTEXT = (By.XPATH, "//div[@id='root']/div/div/div[3]/div[1]/nav/ul/li[1]")
    LOGIN_BUTTON = (By.XPATH, "//div[@id='root']/div/div/div[2]/div[3]/div[1]/div/div/div[6]")
    MENU_BUTTON = (By.XPATH, "//div[@id='root']/div/div/div[2]/button")
    API_PAGE = (By.XPATH, "//div[@id='root']/div/div/div[2]/div[5]/div/div[2]/div/div/ul[3]/li[4]/div/a")

    def enter_search_text(self, text):
        """Enters search text"""
        try:
            with allure.step("Main page"):  # allure step
                Logger.add_start_step(method='enter_search_text')
                search_field = self.find_element(self.SEARCH_FIELD)

                # Click and enter search value
                search_field.click()
                search_field.send_keys(text)
                Logger.add_end_step(method='enter_search_text', url=self.driver.current_url)

        except Exception as ex:
            error_message = f"Can not enter search text: {ex}"
            print(error_message)
            Logger.write_log_to_file(error_message)

    def click_enter(self):
        """Clicks enter (search input field)"""
        try:
            with allure.step("Main page"):  # allure step
                Logger.add_start_step(method='click_enter')
                self.find_element(self.SEARCH_FIELD).send_keys(Keys.ENTER)
                Logger.add_end_step(method='click_enter', url=self.driver.current_url)

        except Exception as ex:
            error_message = f"Can not click enter: {ex}"
            print(error_message)
            Logger.write_log_to_file(error_message)

    def reverse_map(self):
        """Clicks on map and gets info about point"""
        try:
            with allure.step("Main page"):  # allure step
                Logger.add_start_step(method='reverse_map')
                map_element = self.find_element(self.MAP_WINDOW)

                actions = ActionChains(self.driver)

                # Click context button on the map
                actions.context_click(map_element).perform()

                # Click 'what's here' button
                whats_here_element = self.find_element(self.WHAT_HERE_CONTEXT)
                whats_here_element.click()

                Logger.add_end_step(method='reverse_map', url=self.driver.current_url)

        except Exception as ex:
            error_message = f"Can not reverse map: {ex}"
            print(error_message)
            Logger.write_log_to_file(error_message)

    def click_login(self):
        """Clicks login button"""
        try:
            with allure.step("Main page"):  # allure step
                Logger.add_start_step(method='click_login')
                login_button = self.find_element(self.LOGIN_BUTTON)
                login_button.click()
                Logger.add_end_step(method='click_login', url=self.driver.current_url)

        except Exception as ex:
            error_message = f"Can not click login: {ex}"
            print(error_message)
            Logger.write_log_to_file(error_message)

    def open_api_page(self):
        """Clicks 'API info' button"""
        try:
            with allure.step("Main page"):  # allure step
                Logger.add_start_step(method='open_api_page')

                # Menu button
                menu_button = self.find_element(self.MENU_BUTTON)
                menu_button.click()

                # Api button
                api_button = self.find_element(self.API_PAGE)
                api_button.click()

                Logger.add_end_step(method='open_api_page', url=self.driver.current_url)

        except Exception as ex:
            error_message = f"Can not open api page: {ex}"
            print(error_message)
            Logger.write_log_to_file(error_message)
