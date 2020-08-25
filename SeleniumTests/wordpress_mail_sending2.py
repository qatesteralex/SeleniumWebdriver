
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # Use Chrome browse
driver.get("https://qasvus.wordpress.com") # 2. Go to : https://qasvus.wordpress.com
driver.maximize_window() # 4. Maximize browser window

print(driver.find_element(By.XPATH, "//p[@class='site-title']//a[@href='https://qasvus.wordpress.com/']").
      get_attribute("href")) # 5. Print link(href) for header message "California Real Estate"
print(driver.find_element(By.XPATH, "//img[@class='wp-image-55']").get_attribute("src")) # 6. Print link(src) for first
                                                                                            # home image under "About us"
assert "California Real Estate" in driver.title # 7. Verify (do assert) "California Real Estate" in  website title
print(driver.title) # 8. Print website title
driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]") # 9. Find "Send Us a Message" and verify
                                                                                    # it's present on the web page
driver.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Alex Smile") #
driver.find_element(By.NAME, "g2-email").send_keys("sqa.tester.alex@gmail.com")
driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Hello, this is SPARTA!!!")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//*[@class='pushbutton-wide']").submit()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//*[@href='/?contact-form-hash=ba2938b804d2758df7e6353f6769437bbd9049a3']").click()
driver.implicitly_wait(5)
print(driver.find_element(By.XPATH, "//button[@type='submit']").get_attribute("type")) # 12. Once you'll get the Main
                                                        # page, verify it by finding and print "type" for "Submit" button
print('Find "go back" button (link) and using one of the tags above click it to go back to the Main page') # 11. When
                                                            # the message will be send: - Find "go back" button (link)
                                                    # and using one of the tags above click it to go back to the Main page.
driver.close()
driver.quit()
