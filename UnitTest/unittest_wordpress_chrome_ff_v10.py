import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Unit test for Chrome browser:
class ChromeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get("https://qasvus.wordpress.com/")
        driver_chrome.maximize_window()
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(2)

        # Do assertions for driver title

        assert "California Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

        # Clear fields: text area, first and last name

        search_name = driver_chrome.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_email = driver_chrome.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_text = driver_chrome.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_text.clear()

        # Fill out all fields and click on Submit button
        driver_chrome.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Regina Kinchina")
        driver_chrome.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("regisha86@gmail.com")
        driver_chrome.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys(
            "This is the first unit test")
        driver_chrome.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_chrome.implicitly_wait(6)

        # Use "try/except" method to wait "go back" link is VISIBLE and click it after

        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
        time.sleep(2)

        driver_chrome.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()

        # Use "wait.until" method for visibility of all 4 houses images on the main page

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))
        driver_chrome.implicitly_wait(4)

        # Do assertion for page title and print it with custom string

        assert "California Real Estate" in driver_chrome.title
        print("Title after go back is " + driver_chrome.title)
        time.sleep(1)

    # Unit test for Chrome for 1120x550 pixels

    def test_chrome_1120x550(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 550)
        driver_chrome.get("https://qasvus.wordpress.com")
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)

        assert "California Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

        search_name = driver_chrome.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_name.send_keys("Regina Kinchina")
        search_email = driver_chrome.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_email.send_keys("regisha86@gmail.com")
        search_message = driver_chrome.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_message.clear()
        search_message.send_keys(
            "This is the first unit test")
        driver_chrome.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_chrome.implicitly_wait(6)

        html = driver_chrome.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2)

        driver_chrome.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
        driver_chrome.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        assert "California Real Estate" in driver_chrome.title
        print("Title after go back is ", driver_chrome.title)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


class FirefoxTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_fire_fox(self):
        driver_firefox = self.driver
        driver_firefox.get("https://qasvus.wordpress.com/")
        driver_firefox.maximize_window()
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(3)

        assert "California Real Estate" in driver_firefox.title
        print("Title after go back is ", driver_firefox.title)
        time.sleep(3)

        search_name = driver_firefox.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_email = driver_firefox.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_text = driver_firefox.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_text.clear()

        driver_firefox.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Regina Kinchina")
        driver_firefox.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("regisha86@gmail.com")
        driver_firefox.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys(
            "This is the second unit test")
        driver_firefox.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_firefox.implicitly_wait(6)

        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
        time.sleep(3)

        driver_firefox.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))
        driver_firefox.implicitly_wait(4)

        assert "California Real Estate" in driver_firefox.title
        print("Title after go back is " + driver_firefox.title)
        time.sleep(3)

    def test_fire_fox_default(self):
        driver_firefox = self.driver
        driver_firefox.get("https://qasvus.wordpress.com")
        driver_firefox.set_window_size(1250, 850)
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)

        assert "California Real Estate" in driver_firefox.title
        print("Page title in Fire fox is:", driver_firefox.title)
        time.sleep(1)

        search_name = driver_firefox.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_name.send_keys("Regina Kinchina")
        search_email = driver_firefox.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_email.send_keys("regisha86@gmail.com")
        search_message = driver_firefox.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_message.clear()
        search_message.send_keys(
            "This is the second unit test")
        driver_firefox.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_firefox.implicitly_wait(6)

        html = driver_firefox.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2)

        driver_firefox.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
        driver_firefox.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        assert "California Real Estate" in driver_firefox.title
        print("Title after go back is ", driver_firefox.title)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()