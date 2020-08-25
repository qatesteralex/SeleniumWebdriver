import time
import unittest

# import HtmlTestRunner
from faker import Faker
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

faker_class = Faker()

class ChromeTest(unittest.TestCase):
    def setUp(self):
        self.driver_Chrome = webdriver.Chrome()


    def test_Chrome_Max_Window(self):
        driver = self.driver_Chrome
        driver.maximize_window()
        driver.get("https://qasvus.wordpress.com/")
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,
                                                '//button[@type="submit"]')))
        self.assertIn("California Real Estate", driver.title)
        print("Page has", driver.title + " as page title")

        name_field = driver.find_element_by_id('g2-name')
        name_field.clear()
        name_field.send_keys(faker_class.name())
        email_field = driver.find_element_by_name('g2-email')
        email_field.clear()
        email_field.send_keys(faker_class.email())
        driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        message_area = driver.find_element_by_id('contact-form-comment-g2-message')
        message_area.clear()
        message_area.send_keys(faker_class.text())
        driver.implicitly_wait(5)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'pushbutton-wide')))
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        try:
            WebDriverWait(driver, 3).until((EC.visibility_of_element_located(
                        (By.XPATH, "//a[contains(text(),'go back')]"))))
            print("Go Back link is visible on the page")
        except ElementNotVisibleException:
            print("Go Back link is not visible on the page")

        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            "//a[contains(text(),'go back')]").send_keys('\n')
        driver.implicitly_wait(5)
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        driver.implicitly_wait(5)
        assert "California Real Estate" in driver.title
        print("After clicking on 'Go back' we are back to the Home page:",
                driver.title)

    def test_Chrome_Specific_Resizing(self):
        driver = self.driver_Chrome
        driver.set_window_size(1120,550)
        driver.get("https://qasvus.wordpress.com/")
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,
                                                '//button[@type="submit"]')))
        self.assertIn("California Real Estate", driver.title)
        print("Page has", driver.title + " as page title")

        name_field = driver.find_element_by_id('g2-name')
        name_field.clear()
        name_field.send_keys(faker_class.name())
        email_field = driver.find_element_by_name('g2-email')
        email_field.clear()
        email_field.send_keys(faker_class.email())
        driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        message_area = driver.find_element_by_id('contact-form-comment-g2-message')
        message_area.clear()
        message_area.send_keys(faker_class.text())
        driver.implicitly_wait(5)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'pushbutton-wide')))
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        try:
            WebDriverWait(driver, 3).until((EC.visibility_of_element_located(
                        (By.XPATH, "//a[contains(text(),'go back')]"))))
            print("Go Back link is visible on the page")
        except ElementNotVisibleException:
            print("Go Back link is not visible on the page")

        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            "//a[contains(text(),'go back')]").send_keys('\n')
        driver.implicitly_wait(5)
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        driver.implicitly_wait(5)
        assert "California Real Estate" in driver.title
        print("After clicking on 'Go back' we are back to the Home page:",
                driver.title)

    def tearDown(self):
        self.driver_Chrome.quit()


class FirefoxTest(unittest.TestCase):
    def setUp(self):
        self.driver_Firefox = webdriver.Firefox(executable_path='C:\webdriver\geckodriver.exe')

    def test_Firefox_Max_Window(self):
        driver = self.driver_Firefox
        driver.maximize_window()
        driver.get("https://qasvus.wordpress.com/")
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//button[@type="submit"]')))
        self.assertIn("California Real Estate", driver.title)
        print("Page has", driver.title + " as page title")

        name_field = driver.find_element_by_id('g2-name')
        name_field.clear()
        name_field.send_keys(faker_class.name())
        email_field = driver.find_element_by_name('g2-email')
        email_field.clear()
        email_field.send_keys(faker_class.email())
        driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        message_area = driver.find_element_by_id(
            'contact-form-comment-g2-message')
        message_area.clear()
        message_area.send_keys(faker_class.text())
        driver.implicitly_wait(5)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'pushbutton-wide')))
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        try:
            WebDriverWait(driver, 3).until((EC.visibility_of_element_located(
                (By.XPATH, "//a[contains(text(),'go back')]"))))
            print("Go Back link is visible on the page")
        except ElementNotVisibleException:
            print("Go Back link is not visible on the page")

        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            "//a[contains(text(),'go back')]").send_keys('\n')
        driver.implicitly_wait(5)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-55']")))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-34']")))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-56']")))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-30']")))

        driver.implicitly_wait(5)
        assert "California Real Estate" in driver.title
        print("After clicking on 'Go back' we are back to the Home page:",
              driver.title)

    def test_Firefox_Specific_Resizing(self):
        driver = self.driver_Firefox
        driver.set_window_size(1250, 850)
        driver.get("https://qasvus.wordpress.com/")
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//button[@type="submit"]')))
        self.assertIn("California Real Estate", driver.title)
        print("Page has", driver.title + " as page title")

        name_field = driver.find_element_by_id('g2-name')
        name_field.clear()
        name_field.send_keys(faker_class.name())
        email_field = driver.find_element_by_name('g2-email')
        email_field.clear()
        email_field.send_keys(faker_class.email())
        driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()
        time.sleep(5)
        message_area = driver.find_element_by_id(
            'contact-form-comment-g2-message')
        message_area.clear()
        message_area.send_keys(faker_class.text())
        driver.implicitly_wait(5)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'pushbutton-wide')))
        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').click()

        try:
            WebDriverWait(driver, 3).until((EC.visibility_of_element_located(
                (By.XPATH, "//a[contains(text(),'go back')]"))))
            print("Go Back link is visible on the page")
        except ElementNotVisibleException:
            print("Go Back link is not visible on the page")

        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            "//a[contains(text(),'go back')]").send_keys('\n')
        driver.implicitly_wait(5)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-55']")))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-34']")))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-56']")))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-30']")))

        driver.implicitly_wait(5)
        assert "California Real Estate" in driver.title
        print("After clicking on 'Go back' we are back to the Home page:",
              driver.title)

    def tearDown(self):
        self.driver_Firefox.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Python projects/test1/AnastasiiaDemenkova/HTMLReports'))


#class FirefoxBrowser(unittest.TestCase):