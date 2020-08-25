from selenium import webdriver
from selenium.webdriver.common.by import By

import shortlib as sl

driver = webdriver.Chrome()
driver.get(sl.my_url)
driver.maximize_window()
driver.implicitly_wait(5)

print(driver.find_element(By.XPATH, sl.site_title).get_attribute("href"))
print(driver.find_element(By.CLASS_NAME, "wp-image-55").get_attribute("src"))

assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title

print(driver.title)

print(driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").text)

driver.find_element(By.NAME, sl.form_name).send_keys("Sergo")
driver.implicitly_wait(5)
driver.find_element_by_id(sl.form_mail).send_keys(sl.acc_mail)
driver.implicitly_wait(5)
driver.find_element(By.TAG_NAME,"textarea").send_keys("test Selenium")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").click()

assert driver.find_element_by_xpath("//div[@id='contact-form-2']//h3[1]").text == "Message Sent (go back)"
driver.find_element_by_xpath("//a[contains(text(),'go back')]").click()

assert driver.find_element_by_class_name("pushbutton-wide").text == "Submit"
print(driver.find_element_by_xpath("//button[@class='pushbutton-wide']").get_attribute("type"))

# closing browser tab
driver.close()
