# Two browsers test for https://qasvus.wordpress.com/
import unittest
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_qasvus_wp_site(self):
        driver_chrome = self.driver
        driver_chrome.get("https://qasvus.wordpress.com/")
        print("Testing Url has ", requests.get("https://qasvus.wordpress.com/").status_code, " as status Code")

        wait = WebDriverWait(driver_chrome, 3)

        # Check that an element is present on the DOM of a page and visible.
        try:
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "custom-logo")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
            print("First Chrome Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        # Checking page title for "California Real Estate – QA at Silicon Valley Real Estate" then print it
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver_chrome.title)
        print("Page has", driver_chrome.title + " as Page title")

        # Checking Site description on the page
        self.assertIn("QA at Silicon Valley Real Estate",
                      driver_chrome.find_element(By.CLASS_NAME, "site-description").text)
        print("Page has", driver_chrome.find_element(By.CLASS_NAME, "site-description").text + " Site description")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "custom-logo")))
        print("Page has Logo and it's clickable")

        self.assertIn("California Real Estate",
                      driver_chrome.find_element(By.XPATH, "//p/a[contains(text(),'California Real Estate')]").text)
        # wait.until(EC.element_located_selection_state_to_be(By.XPATH, "//p/a[contains(text(),'California Real
        # Estate')]"))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p/a[contains(text(),'California Real Estate')]")))
        print("Page has Name 'California Real Estate' and it's clickable")

        # Section About Us
        self.assertIn("About Us",
                      driver_chrome.find_element(By.XPATH, "//h2[contains(text(), 'About Us')]").text)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'About Us')]")))
        print("Section ",
              driver_chrome.find_element(By.XPATH,
                                         "//h2[contains(text(), 'About Us')]").text + " is present on the page")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        print("Picture with house 1 visible")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        print("Picture with house 2 visible")

        # Section Our Services
        self.assertIn("Our Services",
                      driver_chrome.find_element(By.XPATH, "//h2[contains(text(),'Our Services')]").text)
        print("Section ",
              driver_chrome.find_element(By.XPATH,
                                         "// h2[contains(text(), 'Our Services')]").text + " is present on the page")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        print("Picture with house 3 visible")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        print("Picture with house 4 visible")

        driver_chrome.find_element(By.ID, "g2-name").clear()
        driver_chrome.find_element(By.ID, "g2-email").clear()
        driver_chrome.find_element(By.ID, "contact-form-comment-g2-message").clear()
        print("Form cleared")

        driver_chrome.find_element(By.ID, "g2-name").send_keys("Sergey Begichev")
        driver_chrome.find_element(By.ID, "g2-email").send_keys("send@email.com")
        driver_chrome.find_element(By.ID, "contact-form-comment-g2-message").send_keys(
            "Send message from Chrome with max size window.")
        print("Form completed")
        try:
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "accept")))
            driver_chrome.find_element(By.CLASS_NAME, "accept").click()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bottom-sticky__ad-close-btn")))
            driver_chrome.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()
            print("Accept window and AD banner closed")
        except ElementNotInteractableException:
            print("Accept window and AD banner not found")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='pushbutton-wide']")))
        # driver_chrome.find_element(By.CLASS_NAME, "pushbutton-wide").click()
        # elem = driver_chrome.find_element_by_link_text("Submit")
        elem = driver_chrome.find_element_by_xpath("//*[@class='pushbutton-wide']")
        elem.click()

        print("Press button 'Submit'")
        time.sleep(3)

        try:
            driver_chrome.execute_script("window.scrollTo(0, 350)")
            self.assertIn("Message Sent (",
                          driver_chrome.find_element(By.XPATH, "//h3[contains(text(),'Message Sent (')]").text)
            print("Text 'Message Sent' is present")
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bottom-sticky__ad-close-btn")))
            driver_chrome.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()
            print("AD banner closed")

            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "go back")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "go back")))
            driver_chrome.find_element(By.LINK_TEXT, "go back").click()
            print("Main Page is ready!")
            wait.until(EC.visibility_of_element_located((By.ID, "g2-name")))
            print("Name input field is present")
        except TimeoutException:
            print("Loading took too much time!")
        except ElementNotInteractableException:
            print("AD banner not found")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

    def test_qasvus_wp_site_1120x550(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 550)
        driver_chrome.get("https://qasvus.wordpress.com/")
        print("Testing Url has ", requests.get("https://qasvus.wordpress.com/").status_code, " as status Code")

        wait = WebDriverWait(driver_chrome, 3)

        # Check that an element is present on the DOM of a page and visible.
        try:
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "custom-logo")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
            print("First Chrome Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        # Checking page title for "California Real Estate – QA at Silicon Valley Real Estate" then print it
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver_chrome.title)
        print("Page has", driver_chrome.title + " as Page title")

        # Checking Site description on the page
        self.assertIn("QA at Silicon Valley Real Estate",
                      driver_chrome.find_element(By.CLASS_NAME, "site-description").text)
        print("Page has", driver_chrome.find_element(By.CLASS_NAME, "site-description").text + " Site description")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "custom-logo")))
        print("Page has Logo and it's clickable")

        self.assertIn("California Real Estate",
                      driver_chrome.find_element(By.XPATH, "//p/a[contains(text(),'California Real Estate')]").text)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p/a[contains(text(),'California Real Estate')]")))
        print("Page has Name 'California Real Estate' and it's clickable")

        # Section About Us
        self.assertIn("About Us",
                      driver_chrome.find_element(By.XPATH, "//h2[contains(text(), 'About Us')]").text)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'About Us')]")))
        print("Section ",
              driver_chrome.find_element(By.XPATH,
                                         "//h2[contains(text(), 'About Us')]").text + " is present on the page")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        print("Picture with house 1 visible")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        print("Picture with house 2 visible")

        # Section Our Services
        self.assertIn("Our Services",
                      driver_chrome.find_element(By.XPATH, "//h2[contains(text(),'Our Services')]").text)
        print("Section ",
              driver_chrome.find_element(By.XPATH,
                                         "// h2[contains(text(), 'Our Services')]").text + " is present on the page")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        print("Picture with house 3 visible")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        print("Picture with house 4 visible")

        driver_chrome.find_element(By.ID, "g2-name").clear()
        driver_chrome.find_element(By.ID, "g2-email").clear()
        driver_chrome.find_element(By.ID, "contact-form-comment-g2-message").clear()
        print("Form cleared")

        driver_chrome.find_element(By.ID, "g2-name").send_keys("Sergey Begichev")
        driver_chrome.find_element(By.ID, "g2-email").send_keys("send@email.com")
        driver_chrome.find_element(By.ID, "contact-form-comment-g2-message").send_keys(
            "Send message from Chrome with 1120x550 resolution window")
        print("Form completed")

        driver_chrome.find_element(By.CLASS_NAME, "accept").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='pushbutton-wide']")))
        elem = driver_chrome.find_element_by_xpath("//*[@class='pushbutton-wide']")
        elem.click()
        print("Press button 'Submit'")
        time.sleep(3)

        try:
            self.assertIn("Message Sent (",
                          driver_chrome.find_element(By.XPATH, "//h3[contains(text(),'Message Sent (')]").text)
            print("Text 'Message Sent' is present")
            driver_chrome.execute_script("window.scrollTo(0, 350)")
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "go back")))
            driver_chrome.find_element(By.LINK_TEXT, "go back").click()
            print("Main Page is ready!")

            wait.until(EC.visibility_of_element_located((By.ID, "g2-name")))
            print("Name input field is present")
            time.sleep(3)
        except TimeoutException:
            print("Loading took too much time!")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_qasvus_wp_site(self):
        driver_firefox = self.driver
        driver_firefox.get("https://qasvus.wordpress.com/")
        print("Testing Url has ", requests.get("https://qasvus.wordpress.com/").status_code, " as status Code")

        wait = WebDriverWait(driver_firefox, 5)

        # Check that an element is present on the DOM of a page and visible.
        try:
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "custom-logo")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
            print("First Firefox Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        # Checking page title for "California Real Estate – QA at Silicon Valley Real Estate" then print it
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver_firefox.title)
        print("Page has", driver_firefox.title + " as Page title")

        # Checking Site description on the page
        self.assertIn("QA at Silicon Valley Real Estate",
                      driver_firefox.find_element(By.CLASS_NAME, "site-description").text)
        print("Page has", driver_firefox.find_element(By.CLASS_NAME, "site-description").text + " Site description")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "custom-logo")))
        print("Page has Logo and it's clickable")

        self.assertIn("California Real Estate",
                      driver_firefox.find_element(By.XPATH, "//p/a[contains(text(),'California Real Estate')]").text)
        # wait.until(EC.element_located_selection_state_to_be(By.XPATH, "//p/a[contains(text(),'California Real
        # Estate')]"))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p/a[contains(text(),'California Real Estate')]")))
        print("Page has Name 'California Real Estate' and it's clickable")

        # Section About Us
        self.assertIn("About Us",
                      driver_firefox.find_element(By.XPATH, "//h2[contains(text(), 'About Us')]").text)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'About Us')]")))
        print("Section ",
              driver_firefox.find_element(By.XPATH,
                                          "//h2[contains(text(), 'About Us')]").text + " is present on the page")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        print("Picture with house 1 visible")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        print("Picture with house 2 visible")

        # Section Our Services
        self.assertIn("Our Services",
                      driver_firefox.find_element(By.XPATH, "//h2[contains(text(),'Our Services')]").text)
        print("Section ",
              driver_firefox.find_element(By.XPATH,
                                          "// h2[contains(text(), 'Our Services')]").text + " is present on the page")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        print("Picture with house 3 visible")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        print("Picture with house 4 visible")

        driver_firefox.find_element(By.ID, "g2-name").clear()
        driver_firefox.find_element(By.ID, "g2-email").clear()
        driver_firefox.find_element(By.ID, "contact-form-comment-g2-message").clear()
        print("Form cleared")

        driver_firefox.find_element(By.ID, "g2-name").send_keys("Sergey Begichev")
        driver_firefox.find_element(By.ID, "g2-email").send_keys("send@email.com")
        driver_firefox.find_element(By.ID, "contact-form-comment-g2-message").send_keys(
            "Send message from Firefox with max size window.")
        print("Form completed")
        try:
            driver_firefox.find_element(By.CLASS_NAME, "accept").click()
            driver_firefox.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()
            print("Accept window and AD banner closed")
        except ElementNotInteractableException:
            print("Accept window and AD banner not found")
        time.sleep(3)
        driver_firefox.find_element(By.CLASS_NAME, "pushbutton-wide").click()

        print("Press button 'Submit'")
        time.sleep(3)

        try:
            self.assertIn("Message Sent (",
                          driver_firefox.find_element(By.XPATH, "//h3[contains(text(),'Message Sent (')]").text)
            print("Text 'Message Sent' is present")
            driver_firefox.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()
            print("AD banner closed")

            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "go back")))
            driver_firefox.find_element(By.LINK_TEXT, "go back").click()
            print("Main Page is ready!")
            # driver_chrome.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()
            # print("AD banner closed")
            wait.until(EC.visibility_of_element_located((By.ID, "g2-name")))
            print("Name input field is present")
        except TimeoutException:
            print("Loading took too much time!")
        except ElementNotInteractableException:
            print("AD banner not found")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)
        time.sleep(1)

    def test_qasvus_wp_site_1120x550(self):
        driver_firefox = self.driver
        driver_firefox.set_window_size(1120, 550)
        driver_firefox.get("https://qasvus.wordpress.com/")
        print("Testing Url has ", requests.get("https://qasvus.wordpress.com/").status_code, " as status Code")

        wait = WebDriverWait(driver_firefox, 5)

        # Check that an element is present on the DOM of a page and visible.
        try:
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "custom-logo")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
            print("First Firefox Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        # Checking page title for "California Real Estate – QA at Silicon Valley Real Estate" then print it
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver_firefox.title)
        print("Page has", driver_firefox.title + " as Page title")

        # Checking Site description on the page
        self.assertIn("QA at Silicon Valley Real Estate",
                      driver_firefox.find_element(By.CLASS_NAME, "site-description").text)
        print("Page has", driver_firefox.find_element(By.CLASS_NAME, "site-description").text + " Site description")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "custom-logo")))
        print("Page has Logo and it's clickable")

        self.assertIn("California Real Estate",
                      driver_firefox.find_element(By.XPATH, "//p/a[contains(text(),'California Real Estate')]").text)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p/a[contains(text(),'California Real Estate')]")))
        print("Page has Name 'California Real Estate' and it's clickable")

        # Section About Us
        self.assertIn("About Us",
                      driver_firefox.find_element(By.XPATH, "//h2[contains(text(), 'About Us')]").text)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'About Us')]")))
        print("Section ",
              driver_firefox.find_element(By.XPATH,
                                          "//h2[contains(text(), 'About Us')]").text + " is present on the page")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        print("Picture with house 1 visible")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        print("Picture with house 2 visible")

        # Section Our Services
        self.assertIn("Our Services",
                      driver_firefox.find_element(By.XPATH, "//h2[contains(text(),'Our Services')]").text)
        print("Section ",
              driver_firefox.find_element(By.XPATH,
                                          "// h2[contains(text(), 'Our Services')]").text + " is present on the page")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        print("Picture with house 3 visible")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        print("Picture with house 4 visible")

        driver_firefox.find_element(By.ID, "g2-name").clear()
        driver_firefox.find_element(By.ID, "g2-email").clear()
        driver_firefox.find_element(By.ID, "contact-form-comment-g2-message").clear()
        print("Form cleared")

        driver_firefox.find_element(By.ID, "g2-name").send_keys("Sergey Begichev")
        driver_firefox.find_element(By.ID, "g2-email").send_keys("send@email.com")
        driver_firefox.find_element(By.ID, "contact-form-comment-g2-message").send_keys(
            "Send message from Firefox with 1120x550 resolution window")
        print("Form completed")

        driver_firefox.find_element(By.CLASS_NAME, "accept").click()
        time.sleep(1)
        driver_firefox.find_element(By.CLASS_NAME, "pushbutton-wide").click()
        print("Press button 'Submit'")
        time.sleep(3)

        try:
            self.assertIn("Message Sent (",
                          driver_firefox.find_element(By.XPATH, "//h3[contains(text(),'Message Sent (')]").text)
            print("Text 'Message Sent' is present")
            driver_firefox.execute_script("window.scrollTo(0, 250)")
            driver_firefox.find_element(By.LINK_TEXT, "go back").click()
            print("Main Page is ready!")

            wait.until(EC.visibility_of_element_located((By.ID, "g2-name")))
            print("Name input field is present")
            time.sleep(3)
        except TimeoutException:
            print("Loading took too much time!")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()