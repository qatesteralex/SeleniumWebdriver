from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '81.0 beta',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '1366x768'
}
driver = webdriver.Remote(
    command_executor='https://sergeyradchenko1:teiv7hQafZzri3E1Cbkx@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)

driver.get("https://yandex.ru/")
if not "Яндекс" in driver.title:
    raise Exception("It's not our page!")
elem = driver.find_element_by_id("text")
elem.clear()
elem.send_keys("BrowserStack")
elem.submit()

print(driver.title)
driver.quit()