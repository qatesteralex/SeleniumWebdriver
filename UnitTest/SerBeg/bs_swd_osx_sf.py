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
from SergeyBegichev.BrowserStack import locators as lc
from SergeyBegichev.BrowserStack import xpath_var as xpv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SafariSearch(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Catalina',
            'resolution': '1920x1080',
            'browser': 'Safari',
            'browser_version': '13.1',
            'os': 'OS X'
        }
        url = lc.cmd_ex
        # desired_cap['acceptSslCert'] = True
        self.driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=desired_cap)

    def test_qsvs_wp_site(self):
        driver_safari = self.driver
        driver_safari.set_window_size(1920, 1080)
        driver_safari.get(lc.ga_url)
        print("Testing Url has ", requests.get(lc.ga_url).status_code, " as status Code")

        wait = WebDriverWait(driver_safari, 3)
        time.sleep(3)
        try:
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, xpv.qa_cl_ad)))
            driver_safari.find_element(By.CLASS_NAME, xpv.qa_cl_ad).click()
            print("Accept window and AD banner closed")
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "accept")))
            driver_safari.find_element(By.CLASS_NAME, "accept").click()
        except ElementNotInteractableException:
            print("Accept window and AD banner not found")

        # Check that an element is present on the DOM of a page and visible.
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
            print("First Chrome Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        # Checking page title for "California Real Estate – QA at Silicon Valley Real Estate" then print it
        self.assertIn(xpv.qa_title, driver_safari.title)
        print("Page has", driver_safari.title + " as Page title")

        # Checking Site description on the page
        self.assertIn("QA at Silicon Valley Real Estate",
                      driver_safari.find_element(By.CLASS_NAME, "site-description").text)
        print("Page has", driver_safari.find_element(By.CLASS_NAME, "site-description").text + " Site description")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-logo")))
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "custom-logo")))
        print("Page has Logo and it's clickable")

        self.assertIn("California Real Estate",
                      driver_safari.find_element(By.XPATH, xpv.qa_sb_title).text)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpv.qa_sb_title)))
        print("Page has Name 'California Real Estate' and it's clickable")
        EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55"))
        # Section About Us
        driver_safari.find_element_by_xpath(xpv.qa_about).click()
        self.assertIn("About Us",
                      driver_safari.find_element(By.XPATH, xpv.qa_about).text)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpv.qa_about)))
        print("Section ",
              driver_safari.find_element(By.XPATH,
                                         xpv.qa_about).text + " is present on the page")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        print("Picture with house 1 visible")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        print("Picture with house 2 visible")

        # Section Our Services
        driver_safari.find_element_by_xpath(xpv.qa_oserv).click()
        self.assertIn("Our Services",
                      driver_safari.find_element(By.XPATH, xpv.qa_oserv).text)
        print("Section ",
              driver_safari.find_element(By.XPATH,
                                         xpv.qa_oserv).text + " is present on the page")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        print("Picture with house 3 visible")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        print("Picture with house 4 visible")

        # driver_safari.find_element_by_xpath(xpv.qa_snd_m).click()
        driver_safari.find_element(By.ID, "g2-name").clear()
        driver_safari.find_element(By.ID, "g2-email").clear()
        driver_safari.find_element(By.ID, "contact-form-comment-g2-message").clear()
        print("Form cleared")

        driver_safari.find_element(By.ID, "g2-name").send_keys("Sergey Begichev")
        driver_safari.find_element(By.ID, "g2-email").send_keys("send@email.com")
        driver_safari.find_element_by_xpath("//h2[contains(.,'Message')]").click()
        driver_safari.find_element(By.ID, "contact-form-comment-g2-message").send_keys(
            "Send message from Chrome with max size window.")
        print("Form completed")
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='pushbutton-wide']")))
        driver_safari.execute_script("window.scrollTo(0, 700)")
        elem = driver_safari.find_element_by_xpath("//*[@class='pushbutton-wide']")
        elem.click()

        print("Press button 'Submit'")
        time.sleep(3)

        try:
            driver_safari.execute_script("window.scrollTo(0, 350)")
            # self.assertIn("Message Sent (",
            #               driver_safari.find_element(By.XPATH, xpv.qa_snd_m).text)
            wait.until(EC.text_to_be_present_in_element((By.XPATH, xpv.qa_snd_m), "Message Sent ("))

            print("Text 'Message Sent' is present")
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, xpv.qa_cl_ad)))
            driver_safari.find_element(By.CLASS_NAME, xpv.qa_cl_ad).click()
            print("AD banner closed")

            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "go back")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "go back")))
            driver_safari.find_element(By.LINK_TEXT, "go back").click()
            print("Main Page is ready!")
            wait.until(EC.visibility_of_element_located((By.ID, "g2-name")))
            print("Name input field is present")
        except TimeoutException:
            print("Loading took too much time!")
        except ElementNotInteractableException:
            print("AD banner not found")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_safari.title
        print("Page title in Safari is:", driver_safari.title)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()