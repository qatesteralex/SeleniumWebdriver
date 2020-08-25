import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Chrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
        self.driver.maximize_window()

    def test_FillForm(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        assert "California Real Estate" in driver.title
        print("Title " + driver.title)
        name = driver.find_element(By.TAG_NAME, "input")
        massage = driver.find_element(By.NAME, "g2-message")
        name.clear()
        massage.clear()
        name.send_keys("Madina")
        massage.send_keys("Hello")
        driver.find_element(By.NAME, "g2-email").send_keys("ddd@gmail.com")
        driver.find_element_by_xpath("//button[@class='pushbutton-wide']").send_keys(Keys.ENTER)
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, " //a[contains(text(),'go back')]")))
            print("Go Back Button clickable")
        except TimeoutException:
            print("Loading took to much time!")
        driver.find_element_by_xpath(" //a[contains(text(),'go back')]").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        assert "California Real Estate" in driver.title
        print("Title after go back  " + driver.title)

    def test_FillForm_1120x550(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        driver.set_window_size(1120, 550)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        assert "California Real Estate" in driver.title
        print("Title " + driver.title)
        name = driver.find_element(By.TAG_NAME, "input")
        massage = driver.find_element(By.NAME, "g2-message")
        name.clear()
        massage.clear()
        name.send_keys("Madina")
        massage.send_keys("Hello")
        driver.find_element(By.NAME, "g2-email").send_keys("ddd@gmail.com")
        driver.find_element_by_xpath("//button[@class='pushbutton-wide']").send_keys(Keys.ENTER)
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, " //a[contains(text(),'go back')]")))
            print("Go Back Button clickable")
        except TimeoutException:
            print("Loading took to much time!")
        driver.execute_script("window.scroll(0, 0);")
        driver.find_element_by_xpath(" //a[contains(text(),'go back')]").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        assert "California Real Estate" in driver.title
        print("Title after go back  " + driver.title)


class Firefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\webdriver\geckodriver.exe")

    def test_FillForm(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-comment-g2-message")))
        assert "California Real Estate" in driver.title
        print("Title " + driver.title)
        name = driver.find_element(By.TAG_NAME, "input")
        massage = driver.find_element(By.NAME, "g2-message")
        name.clear()
        massage.clear()
        name.send_keys("Madina")
        massage.send_keys("Hello")
        driver.find_element(By.NAME, "g2-email").send_keys("ddd@gmail.com")
        driver.find_element_by_xpath("//button[@class='pushbutton-wide']").send_keys(Keys.ENTER)
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, " //a[contains(text(),'go back')]")))
            print("Go Back Button clickable")
        except TimeoutException:
            print("Loading took to much time!")
        driver.find_element_by_xpath(" //a[contains(text(),'go back')]").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        assert "California Real Estate" in driver.title
        print("Title after go back  " + driver.title)

    def test_FillForm_1250x850(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        driver.set_window_size(1250, 850)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        assert "California Real Estate" in driver.title
        print("Title " + driver.title)
        name = driver.find_element(By.TAG_NAME, "input")
        massage = driver.find_element(By.NAME, "g2-message")
        name.clear()
        massage.clear()
        name.send_keys("Madina")
        massage.send_keys("Hello")
        driver.find_element(By.NAME, "g2-email").send_keys("ddd@gmail.com")
        driver.find_element_by_xpath("//button[@class='pushbutton-wide']").send_keys(Keys.ENTER)
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, " //a[contains(text(),'go back')]")))
            print("Go Back Button clickable")
        except TimeoutException:
            print("Loading took to much time!")
        driver.find_element_by_xpath(" //a[contains(text(),'go back')]").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))
        assert "California Real Estate" in driver.title
        print("Title after go back  " + driver.title)

    def tearDown(self):
        self.driver.quit()
