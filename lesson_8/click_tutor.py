import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.freeconferencecall.com/global/gl')

login_button = driver.find_element('xpath', '//a[@id="login-desktop"]')
login_button.click()

email_field = driver.find_element('xpath', '//input[@id="login_email"]')
email_field.send_keys('test@test.ru')

print(email_field.get_attribute('value'))
print(email_field.get_attribute('maxlength'))
time.sleep(3)
email_field.send_keys('aaaaa')
print(email_field.get_attribute('value'))
time.sleep(3)
email_field.clear()
time.sleep(3)
email_field.send_keys('correct_email@mail.com')
print(email_field.get_attribute('value'))
time.sleep(3)
driver.quit()
