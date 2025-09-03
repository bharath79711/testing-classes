import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# ---------------- TASK 1: Verify Page Title ----------------
def test_google_title(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title
    time.sleep(5)


# ---------------- TASK 2: Verify Input Box ----------------
def test_google_search_box_present(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    assert search_box.is_displayed()
    time.sleep(5)

# ---------------- TASK 3: Search Functionality ----------------
def test_w3schools (browser):
    browser.get("https://www.w3schools.com")
    time.sleep(3)
    assert "w3schools" in browser.title.lower()
    time.sleep(3)
#----------------------TASK 4:logo search----------------------------------
def test_logo_display(browser):
    browser.get("https://www.w3schools.com")
    time.sleep(5)
    logo = browser.find_element(By.CSS_SELECTOR, "a[title='Home']")
    assert logo.is_displayed()
    time.sleep(5)

#---------------TASK 5:Search bar visibility----------------------------

def test_search_bar(browser):
    browser.get("https://www.w3schools.com")
    time.sleep(5)
    search_bar = browser.find_element(By.ID, "search2")
    search_bar.send_keys("python Tutorial")
    time.sleep(5)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(5)
    assert "Python Tutorial" in browser.title
    time.sleep(5)

#---------------TASK 5:Navigate to python Tutorial----------------------

def test_Navigate_python_tutorial(browser):
    browser.get("https://www.w3schools.com")
    time.sleep(5)
    search_bar = browser.find_element(By.ID, "search2")
    search_bar.send_keys("python Tutorial")
    time.sleep(5)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)
    python_link = browser.find_element(By.XPATH,"//*[@id='leftmenuinnerinner']/a[2]")
    python_link.click()
    time.sleep(5)
    assert "What is Python?" in browser.page_source


