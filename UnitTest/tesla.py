# import unittest
# import HtmlTestRunner
# import time
# import unittest
#
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from faker import Faker


class ChromeTest(unittest.TestCase):
    def setUp(self):
        self.driver_Chrome = webdriver.Chrome()

    def test_Chrome_Max_Window(self):
        driver = self.driver_Chrome
        driver.maximize_window()
        driver.get("https://www.tesla.com/cybertruck")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                         '//a[contains(text(),"Privacy & Legal")]')))
        self.assertIn("Tesla Cybertruck", driver.title)
        print("Page has", driver.title + " as page title")

        # name_field = driver.find_element_by_id('g2-name')
        # name_field.clear()
        # name_field.send_keys(faker_class.name())
        # email_field = driver.find_element_by_name('g2-email')
        # email_field.clear()
        # email_field.send_keys(faker_class.email())
        # driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        # message_area = driver.find_element_by_id('contact-form-comment-g2-message')
        # message_area.clear()
        # message_area.send_keys(faker_class.text())
        # driver.implicitly_wait(5)
        # WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'pushbutton-wide')))
        # driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()


print(driver.title)
print(driver.current_url)

driver.quit()
