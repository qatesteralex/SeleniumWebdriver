import unittest
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get('http://www.google.com')
        wait = WebDriverWait(driver_chrome, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'hplogo')))
        time.sleep(1)  # simulate long running test

        search = driver_chrome.find_element_by_name("q")
        search.clear()
        search.send_keys("wikipedia")
        search.submit()

        assert "No results found." not in driver_chrome.page_source  # True or False

        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Wikipedia')))
        elem = driver_chrome.find_element_by_partial_link_text("Wikipedia")
        elem.click()
        self.assertIn("Wikipedia", driver_chrome.title)
        print("Page has", driver_chrome.title + " as Page title")
        print("Wikipedia Url has ", requests.get("https://www.wikipedia.org").status_code, " as status Code")

        assert "No results found." not in driver_chrome.page_source

        wait = WebDriverWait(driver_chrome, 2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "central-featured")))
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem = driver_chrome.find_element_by_id("searchInput")
        elem.send_keys("Bread")
        elem.send_keys(Keys.RETURN)
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        self.assertIn("Bread - Wikipedia", driver_chrome.title)
        print("Page has", driver_chrome.title + " as Page title")

        driver_chrome.find_element_by_xpath("//img[@alt='Loaves of bread in a basket']").click()
        delay = 3  # seconds
        try:
            WebDriverWait(driver_chrome, delay).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//*[@src='https://upload.wikimedia.org/wikipedia/commons/c/c7/Korb_mit_Br%C3%B6tchen.JPG']")))
            print("Wikipedia Bread Page is ready!")
            # driver_chrome.get_screenshot_as_file('ScreenshotBread_page.png')
        except TimeoutException:
            print("Loading took too much time!")
            # driver_chrome.get_screenshot_as_file('bread_page_loading_error.png')
        driver_chrome.implicitly_wait(10)

        assert "Korb mit Brötchen - Bread - Wikipedia" in driver_chrome.title
        print("Page has", driver_chrome.title + " as Page title")
        print("Test for Chrome is Done! Bread forever!")
        # driver_chrome.get_screenshot_as_file('bread.png')

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_chrome(self):
        driver_firefox = self.driver
        driver_firefox.get('http://www.google.com')
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'hplogo')))
        time.sleep(1)  # simulate long running test

        search = driver_firefox.find_element_by_name("q")
        search.clear()
        search.send_keys("wikipedia")
        search.submit()

        assert "No results found." not in driver_firefox.page_source  # True or False

        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Wikipedia')))
        elem = driver_firefox.find_element_by_partial_link_text("Wikipedia")
        elem.click()
        self.assertIn("Wikipedia", driver_firefox.title)
        print("Page has", driver_firefox.title + " as Page title")
        print("Wikipedia Url has ", requests.get("https://www.wikipedia.org").status_code, " as status Code")

        assert "No results found." not in driver_firefox.page_source

        wait = WebDriverWait(driver_firefox, 2)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "central-featured")))
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        elem = driver_firefox.find_element_by_id("searchInput")
        elem.send_keys("Bread")
        elem.send_keys(Keys.RETURN)
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        self.assertIn("Bread - Wikipedia", driver_firefox.title)
        print("Page has", driver_firefox.title + " as Page title")

        driver_firefox.find_element_by_xpath("//img[@alt='Loaves of bread in a basket']").click()
        delay = 3  # seconds
        try:
            WebDriverWait(driver_firefox, delay).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//*[@src='https://upload.wikimedia.org/wikipedia/commons/c/c7/Korb_mit_Br%C3%B6tchen.JPG']")))
            print("Wikipedia Bread Page is ready!")
            # driver_chrome.get_screenshot_as_file('ScreenshotBread_page.png')
        except TimeoutException:
            print("Loading took too much time!")
            # driver_chrome.get_screenshot_as_file('bread_page_loading_error.png')
        driver_firefox.implicitly_wait(10)

        assert "Korb mit Brötchen.JPG - Wikipedia" in driver_firefox.title
        print("Page has", driver_firefox.title + " as Page title")
        print("Test for Chrome is Done! Bread forever!")
        # driver_chrome.get_screenshot_as_file('bread.png')

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        self.driver.quit()
