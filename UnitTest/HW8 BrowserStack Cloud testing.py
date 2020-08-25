# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# desired_cap = {
#     'browserName': 'iPhone',
#     'device': 'iPhone 11 Pro Max',
#     'realMobile': 'true',
#     'os_version': '13',
# }
# driver = webdriver.Remote(
#     command_executor='https://reginakinchina1:ZMnRhCsDiy4q6tFmsDmb@hub-cloud.browserstack.com/wd/hub',
#     desired_capabilities=desired_cap)
#
# driver.get("https://www.google.com")
# if not "Google" in driver.title:
#     raise Exception("Unable to load google page!")
# elem = driver.find_element_by_name("q")
# elem.send_keys("BrowserStack")
# elem.submit()
# print(driver.title)
#
# driver.quit()
#
# ______________________


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# desired_cap = {
#  'os_version': '10',
#  'resolution': '1920x1080',
#  'browser': 'Firefox',
#  'browser_version': '77.0',
#  'os': 'Windows'
# }
# driver = webdriver.Remote(
#     command_executor='https://reginakinchina1:ZMnRhCsDiy4q6tFmsDmb@hub-cloud.browserstack.com/wd/hub',
#     desired_capabilities=desired_cap)
#
# driver.get("https://qasvus.wordpress.com")
#
# print(driver.find_element(By.TAG_NAME, "a").get_attribute("href"))
#
# print(driver.find_element(By.CLASS_NAME, "wp-image-55").get_attribute("src"))
#
#
# assert "California Real Estate " in driver.title
#
#
# print(driver.title)
#
#
# driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")
# print(driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").text)
#
#
# driver.find_element(By.NAME, "g2-name").send_keys("Regina")
# driver.find_element(By.ID, "g2-email").send_keys("regisha86@gmail.com")
# driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys("test")
#
# driver.implicitly_wait(10)
# driver.find_element(By.CLASS_NAME, "pushbutton-wide").submit()
# driver.implicitly_wait(10)
#
#
# driver.find_element(By.LINK_TEXT, "go back").click()
#
#
# print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))
#
# driver.implicitly_wait(10)
#
# driver.quit()
#
# ______________________


import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from ReginaKinchina import my_url
from ReginaKinchina import Locators as L


class ChromeTest(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': '85.0 beta',
            'os': 'Windows'
        }
        url = my_url.urls
        self.driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=desired_cap)

    def test_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get("https://qasvus.wordpress.com/")
        driver_chrome.maximize_window()
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(2)

        assert "California Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

        search_name = driver_chrome.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_email = driver_chrome.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_text = driver_chrome.find_element_by_xpath(L.text)
        search_text.clear()

        # Fill out all fields and click on Submit button
        driver_chrome.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Regina Kinchina")
        driver_chrome.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("regisha86@gmail.com")
        driver_chrome.find_element(By.XPATH, L.text).send_keys(
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

        def tearDown(self):
            self.driver.quit()
