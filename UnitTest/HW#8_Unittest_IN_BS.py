import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ChromeOrgSearch(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '81.0 beta',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1366x768'
        }

        self.driver = webdriver.Remote(command_executor='https://sergeyradchenko1:teiv7hQafZzri3E1Cbkx@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)

    def test_search_in_python_org(self):
        driver_t = self.driver
        driver_t.get("http://www.google.com")
        elem = driver_t.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.submit()
        self.assertIn("Google", driver_t.title)

    def tearDown(self):
        self.driver.quit()

class FFOrgSearch(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Firefox',
            'browser_version': '75.0 beta',
            'os': 'OS X',
            'os_version': 'Catalina',
            'resolution': '1600x1200'
        }

        self.driver = webdriver.Remote(command_executor='https://sergeyradchenko1:teiv7hQafZzri3E1Cbkx@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)

    def test_search_in_python_org(self):
        driver_t = self.driver
        driver_t.get("http://www.yandex.ru")
        elem = driver_t.find_element_by_id("text")
        elem.send_keys("selenium")
        elem.submit()
        self.assertIn("selenium", driver_t.title)

    def tearDown(self):
        self.driver.quit()

