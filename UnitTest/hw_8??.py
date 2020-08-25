# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# desired_cap = {
#  'os_version': '10',
#  'resolution': '1920x1080',
#  'browser': 'chrome',
#  'browser_version': '85.0 beta',
#  'os': 'Windows'
# }
# driver = webdriver.Remote(
#     command_executor='https://bsuser7500873:eNZaHFEDDuH9qbbn2bgu@hub-cloud.browserstack.com/wd/hub',
#     desired_capabilities=desired_cap)
# driver.get("https://www.google.com")
# if not "Google" in driver.title:
#     raise Exception("Unable to load google page!")
# elem = driver.find_element_by_name("q")
# elem.send_keys("BrowserStack")
# elem.submit()
# print(driver.title)
# driver.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# desired_cap = {
#  'os_version': '10',
#  'resolution': '1920x1080',
#  'browser': 'Chrome',
#  'browser_version': '83.0',
#  'os': 'Windows'
# }
# driver = webdriver.Remote(
#     command_executor='https://bsuser7500873:eNZaHFEDDuH9qbbn2bgu@hub-cloud.browserstack.com/wd/hub',
#     desired_capabilities=desired_cap)
#
# driver = webdriver.Chrome()
# driver.get("https://qasvus.wordpress.com")
# driver.maximize_window()
#
# print(driver.find_element_by_xpath("//p[@class='site-title']//a[contains(text(),'California Real Estate')]").get_attribute("href"))
#
# print(driver.find_element(By.XPATH, "//img[@class='wp-image-55']").get_attribute("src"))
#
# assert "California Real Estate" in driver.title
#
# print(driver.title)
#
# assert "Send Us a Message" in driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").text
#
#
# driver.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Asiya Tumatova")
# driver.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("AsiyaTumatova@gmail.com")
# driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys("I did it !!!")
# driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").submit()
# driver.implicitly_wait(5)
#
# driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
#
# print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))
# driver.close()


# coding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import locators_BrowserStack as lc
import xpath_BrowserStack as xpH

desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': '83.0',
 'os': 'Windows'
}
driver = webdriver.Remote(
    command_executor='https://bsuser7500873:eNZaHFEDDuH9qbbn2bgu@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)

driver = webdriver.Chrome()
driver.get(lc.url)
driver.maximize_window()

print(driver.find_element_by_xpath(xpH.cre).get_attribute("href"))

print(driver.find_element(By.XPATH, xpH.pic).get_attribute("src"))

assert "California Real Estate" in driver.title

print(driver.title)

assert "Send Us a Message" in driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").text


driver.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Asiya Tumatova")
driver.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("AsiyaTumatova@gmail.com")
driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys("I did it !!!")
driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").submit()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()

print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))
driver.close()

