import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_firstpage(self):
        driver_chrome = self.driver
        driver_chrome.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver_chrome, 3)

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,'//button[@class="pushbutton-wide"]')))
            print("First Page in Chrome is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver_chrome.get_screenshot_as_file('page_loading_error.png')
        time.sleep(1)

# find and clear elements
        elem = driver_chrome.find_element_by_name("g2-name")
        elem.clear()
        elem.send_keys("San Jose")

        elem1 = driver_chrome.find_element_by_name("g2-email")
        elem1.clear()
        elem1.send_keys("San_Jose@gmail.com")

        elem2 = driver_chrome.find_element_by_name("g2-message")
        elem2.clear()
        elem2.send_keys("San Jose tests sending form")

        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="pushbutton-wide"]')))
        driver_chrome.find_element_by_xpath("//button[@class='pushbutton-wide']").click()
        time.sleep(1)
        print("Message sent")
        driver_chrome.find_element_by_xpath("//a[contains(text(),'go back')]").click()
        time.sleep(1.5)

        assert "Submit" in driver_chrome.find_element_by_xpath("//button[@class='pushbutton-wide']").text
        assert "California Real" in driver_chrome.title
        print("all right! title is: " + driver_chrome.title)
        time.sleep(1)

    def test_firstpage_1120x550(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 550)
        driver_chrome.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver_chrome, 3)

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="pushbutton-wide"]')))
            print("First Page in Chrome is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver_chrome.get_screenshot_as_file('page_loading_error.png')
        time.sleep(1)

        elem = driver_chrome.find_element_by_name("g2-name")
        elem.clear()
        elem.send_keys("San Jose")

        elem1 = driver_chrome.find_element_by_name("g2-email")
        elem1.clear()
        elem1.send_keys("San_Jose@gmail.com")

        elem2 = driver_chrome.find_element_by_name("g2-message")
        elem2.clear()
        elem2.send_keys("San Jose tests sending form")

        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="pushbutton-wide"]')))
        driver_chrome.find_element_by_xpath("//button[@class='pushbutton-wide']").click()
        time.sleep(1)
        print("Message sent")

        # this is a scroll for display item
        driver_chrome.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)

        target = driver_chrome.find_element_by_link_text('go back')
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"go back")]')))
        target.click()
        time.sleep(1.5)

        assert "Submit" in driver_chrome.find_element_by_xpath("//button[@class='pushbutton-wide']").text
        assert "California Real" in driver_chrome.title
        print("all right! title is: " + driver_chrome.title)
        time.sleep(1)

    def tearDown(self):
        # Close the browser.
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_firstpage_ff(self):
        driver_ff = self.driver
        driver_ff.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver_ff, 5)

        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'contact-form-comment-g2-message')))
            print("First Page in Chrome is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver_ff.get_screenshot_as_file('page_loading_error.png')
        time.sleep(1)  # simulate long running test

        elem = driver_ff.find_element_by_name("g2-name")
        elem.clear()
        elem.send_keys("San Jose")

        elem1 = driver_ff.find_element_by_name("g2-email")
        elem1.clear()
        elem1.send_keys("San_Jose@gmail.com")

        elem2 = driver_ff.find_element_by_name("g2-message")
        elem2.clear()
        elem2.send_keys("San Jose tests sending form")

        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="pushbutton-wide"]')))
        driver_ff.find_element_by_xpath("//button[@class='pushbutton-wide']").click()
        time.sleep(1)
        print("Message sent")
        driver_ff.find_element_by_xpath("//a[contains(text(),'go back')]").click()
        time.sleep(1.5)

        assert "Submit" in driver_ff.find_element_by_xpath("//button[@class='pushbutton-wide']").text
        assert "California Real" in driver_ff.title
        print("all right! title is: " + driver_ff.title)
        time.sleep(1)

    def test_test_firstpage_ff_1250x850(self):
        driver = self.driver
        driver_ff = self.driver
        driver.set_window_size(1250, 850)
        driver_ff.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver_ff, 5)

        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'contact-form-comment-g2-message')))
            print("First Page in Chrome is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            driver_ff.get_screenshot_as_file('page_loading_error.png')
        time.sleep(1)  # simulate long running test

        elem = driver_ff.find_element_by_name("g2-name")
        elem.clear()
        elem.send_keys("San Jose")

        elem1 = driver_ff.find_element_by_name("g2-email")
        elem1.clear()
        elem1.send_keys("San_Jose@gmail.com")

        elem2 = driver_ff.find_element_by_name("g2-message")
        elem2.clear()
        elem2.send_keys("San Jose tests sending form")

        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="pushbutton-wide"]')))
        driver_ff.find_element_by_xpath("//button[@class='pushbutton-wide']").click()
        time.sleep(1)
        print("Message sent")
        target = driver_ff.find_element_by_link_text('go back')
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"go back")]')))
        target.click()
        time.sleep(1.5)

        assert "Submit" in driver_ff.find_element_by_xpath("//button[@class='pushbutton-wide']").text
        assert "California Real" in driver_ff.title
        print("all right! title is: " + driver_ff.title)
        time.sleep(1)

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        self.driver.quit()
