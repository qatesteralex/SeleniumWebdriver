from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#driver.find_element(By.NAME,"q").send_keys("ABC")

print(driver.find_element(By.XPATH, "//p[@class='site-title']//a[contains(text(),'California Real Estate')]").get_attribute("href"))
print(driver.find_element(By.CLASS_NAME, "wp-image-55").get_attribute("src"))

assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title

print(driver.title)

print(driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").text)

driver.find_element(By.NAME, "g2-name").send_keys("Sergo")
driver.implicitly_wait(5)
driver.find_element_by_id("g2-email").send_keys("radchenkofoto@mail.ru")
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
