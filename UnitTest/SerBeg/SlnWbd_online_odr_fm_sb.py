from selenium import webdriver
from selenium.webdriver.common.by import By
from SergeyBegichev.BrowserStack import locators as lc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# from python_rucaptcha import ReCaptchaV2
# import time

desired_cap = {
    # 'os_version': '10',
    # 'resolution': '1920x1080',
    # 'browser': 'Chrome',
    # 'browser_version': '84.0',
    # 'os': 'Windows'
    'os_version': 'Catalina',
    'resolution': '1920x1080',
    'browser': 'Safari',
    'browser_version': '13.1',
    'os': 'OS X'
}
url = lc.cmd_ex
# desired_cap['acceptSslCert'] = True
driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=desired_cap)

driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()

assert "Online Order Form" in driver.title
print(driver.title)

driver.find_element(By.XPATH, "//input[@placeholder='First']").send_keys("Sergey")
driver.find_element(By.XPATH, "//*[@placeholder='Last']").click()
driver.find_element(By.XPATH, "//*[@placeholder='Last']").send_keys("Begichev")
driver.find_element(By.XPATH, "//input[@aria-labelledby='email0000000a-acc email-0000000a-error-acc "
                              "email-0000000a-instr-acc']").send_keys("send@email.com")
driver.find_element(By.XPATH, "//input[contains(@placeholder,'### ### ####')]").send_keys("999 999 9999")
driver.implicitly_wait(15)
driver.find_element(By.XPATH, "//input[@id='0000000e_2']").click()
driver.implicitly_wait(15)
driver.find_element(By.XPATH, "//input[@aria-labelledby='number-00000010-acc number-00000010-error-acc "
                              "number-00000010-instr-acc']").send_keys("15")

driver.find_element(By.XPATH, "//div[@data-role='expander']").click()
driver.find_element(By.XPATH, "//div[@data-action='btn-next-month']").click()
driver.find_element(By.XPATH, "//div[@data-role='day'][@data-day='16']").click()
driver.implicitly_wait(5)

print(driver.find_element(By.XPATH, "//div[@data-ui-role='ui-element'][@data-type='date']").text)

driver.find_element(By.XPATH, "//div[@data-ui-role='ui-element'][@data-type='date']").send_keys("03\t06\t2021")
driver.implicitly_wait(5)
print(driver.find_element(By.XPATH, "//div[@data-ui-role='ui-element'][@data-type='date']").text)

driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys("123 Sergey's st.")

driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys("Big City")
driver.find_element(By.XPATH, "//input[@placeholder='Region']").send_keys("Region")
driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys("04567")
driver.find_element(By.XPATH, "//input[@placeholder='Country']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys(["United States"])
driver.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys(Keys.ENTER)

print(driver.find_element(By.XPATH, "//input[@placeholder='Country']").text)
driver.execute_script("window.scrollTo(0, 1500)")
xp = "//div[@data-ui-role='ui-element'][@data-type='dropdown']//option[@value='Choice3']"
driver.find_element(By.XPATH, xp).click()

driver.find_element(By.XPATH, "//input[@id='00000018_0']").click()
driver.find_element(By.XPATH, "//input[@id='00000018_2']").click()
driver.execute_script("window.scrollTo(0, 1000)")
# Hera have code for reCaptcha
# This solution is offered in Slack https://qasv.slack.com/files/UTAV6SYN5/F011BCN23V5/recaptchav2.py
# # Введите ключ от сервиса RuCaptcha, из своего аккаунта
# RUCAPTCHA_KEY = "Ключ"
# # G-ReCaptcha ключ сайта
# SITE_KEY = "6LdMNiMTAAAAAGr0ibqKRZc3e5Z6wfLBraX9NuOY"
# # Ссылка на страницу с капчёй
# PAGE_URL = "http://www.123formbuilder.com/form-5012215/online-order-form"
# # Возвращается JSON содержащий информацию для решения капчи
# user_answer = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(site_key=SITE_KEY, page_url=PAGE_URL)
#
# if not user_answer['error']:
#     # решение капчи
#     print('captchaSolve: ', user_answer['captchaSolve'])
#     print('taskId ', user_answer['taskId'])
# elif user_answer['error']:
#     # Тело ошибки, если есть
#     print(user_answer['errorBody']['text'])
#     print(user_answer['errorBody']['id'])
#
# time.sleep(5)
# # driver.execute_script("document.getElementById('text_field').value+='{0}'".format(foo))
#
# capt = user_answer['captchaSolve']
# # вставляем в скрытое поле
# string1 = str("javascript:document.getElementById('g-recaptcha-response').value = '{0}';".format(capt))
# driver.execute_script(string1)

driver.find_element(By.XPATH, "//button[@data-role='submit']").submit()

driver.quit()
