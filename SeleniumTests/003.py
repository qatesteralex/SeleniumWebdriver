from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from python_rucaptcha import ReCaptchaV2
from time import sleep


driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@placeholder='First']").clear()
driver.find_element_by_xpath("//input[@placeholder='First']").send_keys("Serg")

driver.find_element_by_xpath("//input[@placeholder='Last']").clear()
driver.find_element_by_xpath("//input[@placeholder='Last']").send_keys("Rad")

driver.find_element(By.XPATH,"//input[@type='email']").send_keys("rad@mail.ru")
driver.find_element_by_xpath("//input[contains(@placeholder,'### ### ####')]").send_keys("928 207 3678")

driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/div[4]/div/div[1]/div[2]/label/label").click()

driver.find_element_by_xpath("//input[@type='number']").send_keys("5")

driver.find_element_by_xpath("//body/form[@id='form']/div/div/div/div/div/div/div[2]").click()
sleep(1)
driver.find_element_by_class_name("today").click()

driver.find_element_by_xpath("//input[@placeholder='Street Address']").send_keys("red square 122")
driver.find_element_by_xpath("//input[@placeholder='City']").send_keys("Moscow")
driver.find_element_by_xpath("//input[@placeholder='Region']").send_keys("Moscow")
driver.find_element_by_xpath("//input[@placeholder='Postal / Zip Code']").send_keys("300000")
driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/div[7]/div/div[4]/div/input").click()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@placeholder='Country']").send_keys("Russian Federation")

driver.find_element_by_xpath("//option[contains(text(),'Choice1')]").click()
driver.find_element_by_xpath("//span[contains(text(),'Choice 1')]/preceding-sibling::label").click()

#подсмотрено у однокурсника
# Введите ключ от сервиса RuCaptcha, из своего аккаунта
RUCAPTCHA_KEY = "f9a24349a3217f3cd7f34046e8eab711"
# G-ReCaptcha ключ сайта
SITE_KEY = "6LdMNiMTAAAAAGr0ibqKRZc3e5Z6wfLBraX9NuOY"
# Ссылка на страницу с капчёй
PAGE_URL = "http://www.123formbuilder.com/form-5012215/online-order-form"
# Возвращается JSON содержащий информацию для решения капчи
user_answer = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(site_key=SITE_KEY, page_url=PAGE_URL)
#if not user_answer['error']:
# решение капчи
#    print('captchaSolve: ', user_answer['captchaSolve'])
#    print('taskId ', user_answer['taskId'])
#elif user_answer['error']:
# Тело ошибки, если есть
#    print(user_answer['errorBody']['text'])
#    print(user_answer['errorBody']['id'])
sleep(2)
#driver.execute_script("document.getElementById('text_field').value+='{0}'".format(foo))
capt = user_answer['captchaSolve']
#вставляем в скрытое поле
string1 = str("javascript:document.getElementById('g-recaptcha-response').value = '{0}';".format(capt))
driver.execute_script(string1)
sleep(60)

driver.find_element_by_xpath("//body/form[@id='form']/div/div/div/button[1]").click()