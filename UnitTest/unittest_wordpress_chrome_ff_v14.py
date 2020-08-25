import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException


class ChromeSearch ( unittest.TestCase ):

    def setUp(self):
        self.driver = webdriver.Chrome ()
        self.driver.maximize_window ()

    def test_GH1(self):
        driver_chrome = self.driver
        driver_chrome.get ( 'https://qasvus.wordpress.com/' )
        wait = WebDriverWait ( driver_chrome, 3 )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//button[@class='pushbutton-wide']") ) )
        time.sleep ( 1 )
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_chrome.title
        print ( driver_chrome.title + "is present on a page after it is loaded" )
        driver_chrome.find_element ( By.XPATH, '//input[@id="g2-name"]' ).clear ()
        driver_chrome.find_element ( By.XPATH, '//input[@id="g2-email"]' ).clear ()
        driver_chrome.find_element ( By.XPATH, '//input[@id="g2-name"]' ).clear ()
        driver_chrome.find_element ( By.XPATH, '//input[@id="g2-name"]' ).send_keys ( "Anna Test1" )
        driver_chrome.find_element ( By.XPATH, '//input[@id="g2-email"]' ).send_keys ( "test@test.com" )
        driver_chrome.find_element ( By.ID, "contact-form-comment-g2-message" ).send_keys ( "Testing message element" )
        driver_chrome.find_element ( By.XPATH, "//button[@class='pushbutton-wide']" ).submit ()
        time.sleep ( 4 )
        driver_chrome.find_element ( By.LINK_TEXT, "go back" ).location_once_scrolled_into_view
        try:
            wait.until (
                (EC.visibility_of_element_located ( (By.XPATH, "//a[contains(text(),'go back')]") ))
            )
            print ( "Go back is appered" )
        except ElementNotVisibleException:
            print ( "Element not found" )

        time.sleep ( 2 )
        driver_chrome.find_element ( By.LINK_TEXT, "go back" ).send_keys ( '\n' )
        time.sleep ( 2 )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-55']") ) )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-34']") ) )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-56']") ) )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-30']") ) )
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_chrome.title
        print ( driver_chrome.title + "is present on a page after it is loaded. Which mean that we back to main page." )

    def test_GH2(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size ( 1120, 550 )
        driver_chrome.get ( 'https://qasvus.wordpress.com/' )
        wait = WebDriverWait ( driver_chrome, 3 )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//button[@class='pushbutton-wide']") ) )
        time.sleep ( 1 )
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_chrome.title
        print ( driver_chrome.title + "is present on a page after it is loaded" )
        driver_chrome.find_element ( By.XPATH, '//input[@id="g2-name"]' ).clear ()
        driver_chrome.find_element ( By.XPATH, '//input[@id="g2-email"]' ).clear ()
        driver_chrome.find_element ( By.XPATH, '//input[@id="g2-name"]' ).clear ()
        driver_chrome.find_element ( By.XPATH, '//input[@id="g2-name"]' ).send_keys ( "Anna Test1" )
        driver_chrome.find_element ( By.XPATH, '//input[@id="g2-email"]' ).send_keys ( "test@test.com" )
        driver_chrome.find_element ( By.ID, "contact-form-comment-g2-message" ).send_keys ( "Testing message element" )
        driver_chrome.find_element ( By.XPATH, "//button[@class='pushbutton-wide']" ).submit ()
        time.sleep ( 4 )
        driver_chrome.find_element ( By.LINK_TEXT, "go back" ).location_once_scrolled_into_view
        try:
            wait.until (
                (EC.visibility_of_element_located ( (By.XPATH, "//a[contains(text(),'go back')]") ))
            )
            print ( "Go back is appered" )
        except ElementNotVisibleException:
            print ( "Element not found" )

        time.sleep ( 2 )
        driver_chrome.find_element ( By.LINK_TEXT, "go back" ).send_keys ( '\n' )
        time.sleep ( 2 )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-55']") ) )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-34']") ) )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-56']") ) )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-30']") ) )
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_chrome.title
        print ( driver_chrome.title + "is present on a page after it is loaded. Which mean that we back to main page." )

    def tearDown(self):
        self.driver.quit ()


class FFsearch ( unittest.TestCase ):

    def setUp(self):
        self.driver = webdriver.Firefox ()

    def test_FF1(self):
        driver_ff = self.driver
        driver_ff.get ( 'https://qasvus.wordpress.com/' )
        wait = WebDriverWait ( driver_ff, 3 )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//button[@class='pushbutton-wide']") ) )
        time.sleep ( 1 )
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_ff.title
        print ( driver_ff.title + "is present on a page after it is loaded" )
        driver_ff.find_element ( By.XPATH, '//input[@id="g2-name"]' ).clear ()
        driver_ff.find_element ( By.XPATH, '//input[@id="g2-email"]' ).clear ()
        driver_ff.find_element ( By.XPATH, '//input[@id="g2-name"]' ).clear ()
        driver_ff.find_element ( By.XPATH, '//input[@id="g2-name"]' ).send_keys ( "Anna Test1" )
        driver_ff.find_element ( By.XPATH, '//input[@id="g2-email"]' ).send_keys ( "test@test.com" )
        driver_ff.find_element ( By.ID, "contact-form-comment-g2-message" ).send_keys ( "Testing message element" )
        driver_ff.find_element ( By.XPATH, "//button[@class='pushbutton-wide']" ).submit ()
        time.sleep ( 4 )
        driver_ff.find_element ( By.LINK_TEXT, "go back" ).location_once_scrolled_into_view
        try:
            wait.until (
                (EC.visibility_of_element_located ( (By.XPATH, "//a[contains(text(),'go back')]") ))
            )
            print ( "Go back is appered" )
        except ElementNotVisibleException:
            print ( "Element not found" )

        time.sleep ( 2 )
        driver_ff.find_element ( By.LINK_TEXT, "go back" ).send_keys ( '\n' )
        time.sleep ( 2 )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-55']") ) )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-34']") ) )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-56']") ) )
        wait.until ( EC.visibility_of_element_located ( (By.XPATH, "//img[@class='wp-image-30']") ) )
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_ff.title
        print ( driver_ff.title + "is present on a page after it is loaded. Which mean that we back to main page." )

    def test_FF2(self):
        driver_ff = self.driver
        driver_ff.set_window_size ( 1120, 850 )
        driver_ff.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait ( driver_ff, 3 )
        wait.until ( EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_ff.title
        print ( driver_ff.title + "is present on a page after it is loaded" )
        driver_ff.find_element(By.XPATH, '//input[@id="g2-name"]').clear()
        driver_ff.find_element(By.XPATH, '//input[@id="g2-email"]' ).clear()
        driver_ff.find_element(By.XPATH, '//input[@id="g2-name"]' ).clear()
        driver_ff.find_element(By.XPATH, '//input[@id="g2-name"]').send_keys("Anna Test1")
        driver_ff.find_element(By.XPATH, '//input[@id="g2-email"]' ).send_keys("test@test.com")
        driver_ff.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Testing message element")
        driver_ff.find_element ( By.XPATH, "//button[@class='pushbutton-wide']").submit()
        time.sleep(4)
#        driver_ff.find_element(By.LINK_TEXT, "go back").location_once_scrolled_into_view()
        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            )
            print("Go back is appered")
        except ElementNotVisibleException:
            print("Element not found")

        time.sleep(2)
        driver_ff.find_element(By.LINK_TEXT, "go back").send_keys('\n')
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))
        time.sleep(2)
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_ff.title
        print(driver_ff.title + "is present on a page after it is loaded. Which mean that we back to main page.")

    def tearDown(self):
        self.driver.quit ()