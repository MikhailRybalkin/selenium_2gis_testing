# File contains general helper functions

import json
from selenium.webdriver.common.by import By
from utils.logger import Logger


def find_text(parent_element, text):
    """Finds specified text inside the parent element"""
    nothing_found = False

    try:
        child_elements = parent_element.find_elements(By.XPATH, ".//*")

        # Check child elements
        for element in child_elements:
            if text in element.text:
                nothing_found = True
                break

    except Exception as ex:
        error_message = f"Can not find text: {ex}"
        print(error_message)
        Logger.write_log_to_file(error_message)

    return nothing_found


def get_json_value(value):
    """Function gets specific item (by value input) fom json file"""
    res_value = ''
    try:
        # Open and read file
        with open('parameters.json') as f:
            json_data = json.load(f)

        # Get necessary item
        res_value = json_data[value]

    except Exception as ex:
        error_message = f"Can not open file: {ex}"
        print(error_message)
        Logger.write_log_to_file(error_message)

    return res_value
