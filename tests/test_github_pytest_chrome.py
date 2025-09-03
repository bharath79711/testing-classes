import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Variables
GITHUB_URL = "https://github.com/login"
GITHUB_USERNAME = "bharathkumartalari70@gmail.com"
GITHUB_PASSWORD = "Bharath@326"
REPO_NAME = "python-classes"

@pytest.fixture(scope="function")
def driver():
    # Setup Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_login_to_github(driver):
    # Step 1: Open GitHub login page
    driver.get(GITHUB_URL)

    # Step 2: Login
    driver.find_element(By.ID, "login_field").send_keys(GITHUB_USERNAME)
    driver.find_element(By.ID, "password").send_keys(GITHUB_PASSWORD)
    driver.find_element(By.NAME, "commit").click()

    # Step 3: Wait for dashboard
    assert driver.find_element(By.ID, "dashboard-repos-filter-left")

    # Step 4: Go to profile settings
    driver.get("https://github.com/settings/profile")
    profile_input = driver.find_element(By.XPATH, "//input[@id='user_profile_name']")
    assert profile_input.is_displayed()

    # Step 5: Extract username from header
    header_text = driver.find_element(By.ID, "settings-header").text
    cleaned_username = header_text.strip().split()[0]

    # Step 6: Go to dashboard and search repo
    driver.get("https://github.com/dashboard")
    time.sleep(5)
    search_box = driver.find_element(By.ID, "dashboard-repos-filter-left")
    search_box.send_keys(REPO_NAME)

    combined = f"{cleaned_username}/{REPO_NAME}"
    assert combined in driver.page_source

    # Step 7: Click the repo link
    repo_url = f"/{combined}"
    repo_link = driver.find_element(By.XPATH, f"//a[@href='{repo_url}']")
    repo_link.click()

    # Step 8: Capture screenshot
    time.sleep(5)
    driver.save_screenshot("github_repo.png")

