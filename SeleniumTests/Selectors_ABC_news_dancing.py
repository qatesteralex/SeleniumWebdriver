from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()

# driver.find_element_by_name("q").send_keys("abc")
driver.find_element(By.NAME, "q").send_keys("abc")

print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))
print(driver.find_element(By.NAME, "btnK").get_attribute("value"))
print(driver.find_element(By.NAME, "btnI").get_attribute("value"))

driver.implicitly_wait(5)
driver.find_element(By.NAME, "btnK").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
assert "ABC Home Page - ABC.com" in driver.title
print(driver.title)

driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//span[@class='Searchlist__icon__search']").click()
driver.find_element(By.XPATH, "//input[@placeholder='search for a show']").send_keys("Dancing")
driver.implicitly_wait(10)
# Find el Dancing
driver.find_element(By.XPATH, "//*[@title='Dancing with the Stars']").click()
assert "Watch Dancing with the Stars TV Show - ABC.com" in driver.title
print(driver.find_element_by_xpath("//img[@class='Header__Logo__img']").get_attribute("title"))

# closing browser tab
driver.close()

# quit from browser
# driver.quit()
