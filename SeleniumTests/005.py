from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.get("https://qasvus.wordpress.com/")
d.maximize_window()

print(d.find_element(By.XPATH, "//p[@class='site-title']//a[@href='https://qasvus.wordpress.com/']").get_attribute(
    "href"))
print(d.find_element(By.XPATH, "//img[@class='wp-image-55']").get_attribute("src"))
assert "California Real Estate" in d.title
print(d.title)

d.implicitly_wait(5)
print(d.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]"))
d.find_element(By.XPATH, "//input[@id='g2-name']"). send_keys("DianaGali")
d.find_element(By.XPATH, "//input[@id='g2-email']"). send_keys("diane@hn.com")
d.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys("Hello,Serge!")

d.implicitly_wait(5)
d.find_element(By.XPATH, "//button[@class='pushbutton-wide']").submit()
d.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()

d.implicitly_wait(10)
d.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type")

d.quit()