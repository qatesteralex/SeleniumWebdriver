from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
faker_class = Faker()

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com")
driver.maximize_window()

print(driver.find_element(By.XPATH,'//*[@class="site-title"]//*[text()="California Real Estate"]')
                          .get_attribute("href"))
print(driver.find_element(By.XPATH,'(//*[text()="About Us"]/..//img)[1]')
                          .get_attribute("src"))
assert "California Real Estate" in driver.title
print(driver.title)

driver.find_element(By.XPATH,'//*[text()="Send Us a Message"]')
driver.find_element(By.ID,'g2-name').send_keys(faker_class.name())
driver.find_element(By.NAME, 'g2-email').send_keys(faker_class.email())

driver.find_element(By.XPATH,'//*[@value="Close and accept"]').click()
driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys(faker_class.text())

driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME,'pushbutton-wide').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").send_keys('\n')
print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))
driver.quit()