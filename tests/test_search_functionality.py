import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# URL of the Selenium Playground Table Search Demo
BASE_URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"

@pytest.fixture(scope="function")
def browser():
    # Setup ChromeDriver (ensure it's in your PATH or specify its location)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_search_functionality(browser):
    browser.get(BASE_URL)

    # Wait until the search box is visible
    wait = WebDriverWait(browser, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='example_filter']/label/input")))

    # Locate the search box and input "New York"
    search_box.send_keys("New York")

    # Wait for the rows to update after the search
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="example"]/tbody/tr')))

    # Validate the number of results
    rows = browser.find_elements(By.XPATH, '//*[@id="example"]/tbody/tr')
    visible_rows = [row for row in rows if row.is_displayed()]
    assert len(visible_rows) == 5, f"Expected 5 entries, but got {len(visible_rows)}"
    print(f"Visible rows count: {len(visible_rows)}")
