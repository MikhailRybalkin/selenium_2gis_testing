# Pytest-Selenium 2GIS Automation Project

This project is designed to automate the testing of the website [2GIS Rostov](https://2gis.ru/rostov) using Selenium and pytest. It demonstrates the use of Page Object Model (POM) and follows good practices for organizing test code.

## Project Structure

pages:
- base_page.py: Base class for all page objects
- main_page.py: Page object for the main page
- login_page.py: Page object for the login page
- search_results_page.py: Page object for the search results page

tests:
- test_1_search.py: Test for search functionality
- test_2_login.py: Test for login functionality
- test_3_other_pages.py: Test for additional pages 

utils:
- helpers.py: Different helper functions
- logger.py: Logging functionality
- webdriver_setup.py: Utility to setup WebDriver

logs/: Logs dirrectory

parameters.json: File with main URLs

conftest.py: Pytest configuration and fixtures

pytest.ini: Pytest configuration file

README.md: Project documentation

## Installation and Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)
- pytest
- Google Chrome
- allure-pytest

### Setting Up the Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   
4. **Install WebDriver**:

   The project uses webdriver-manager to manage WebDriver installations automatically.

## Running the Tests
### Using PyCharm
1. Open the project in PyCharm.
2. Configure pytest as your test runner.
3. Run the tests using the Run button or through the pytest configuration.

### Using Command Line
1. Activate the virtual environment:

   ```bash
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   
2. Run all tests:

   ```bash
   pytest -s -v 
   
3. Run a specific test file:

   ```bash
   pytest tests/test_search.py
   
## Project Features

### Structured and Modular Test Suite:
The tests are organized modularly, making it easy to maintain and extend the test suite. Each module is responsible for testing specific functionalities of the OSM API, ensuring clear task separation.
### Parameterized Tests:
Parameterized tests are used to test various API parameters, allowing multiple scenarios to be tested with minimal code duplication.
### Page Object Model (POM):
The project is organized using POM to separate the test code from the page-specific operations.
### Fixture-based Setup:
Fixtures in conftest.py manage WebDriver setup and teardown.

## Adding New Tests

To add new tests:

- Create a new test file in the tests/ directory.
- Define your test functions, starting with test_.
- Use existing page objects or create new ones in the pages/ directory.
- Use pytest fixtures to manage setup and teardown as needed.
