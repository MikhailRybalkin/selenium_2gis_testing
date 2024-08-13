# File contains functionality to save logs

import datetime
import os


class Logger:
    """Class for logging functions"""
    file_name = f"logs\\log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_log_to_file(cls, data: str):
        """Writes text to log file"""
        try:
            with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
                logger_file.write(data)

        except Exception as ex:
            error_message = f"Can not write to log: {ex}"
            print(error_message)

    @classmethod
    def add_start_step(cls, method: str):
        """Logs necessary info before test"""
        try:
            test_name = os.environ.get('PYTEST_CURRENT_TEST')

            data_to_add = f"\n-----\n"
            data_to_add += f"Test: {test_name}\n"
            data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
            data_to_add += f"Start name method: {method}\n"
            data_to_add += "\n"

            cls.write_log_to_file(data_to_add)

        except Exception as ex:
            error_message = f"Can not log start step: {ex}"
            print(error_message)

    @classmethod
    def add_end_step(cls, url: str, method: str):
        """Logs necessary info after test"""
        try:
            data_to_add = f"End time: {str(datetime.datetime.now())}\n"
            data_to_add += f"End name method: {method}\n"
            data_to_add += f"URL: {url}\n"
            data_to_add += f"\n-----\n"

            cls.write_log_to_file(data_to_add)

        except Exception as ex:
            error_message = f"Can not log end step: {ex}"
            print(error_message)
