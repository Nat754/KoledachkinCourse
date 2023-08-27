import os
import pickle
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=0.3)

driver.get("https://www.freeconferencecall.com/en/us/login")

# print(driver.get_cookie("country_code"))

# print(driver.get_cookies())

# driver.add_cookie({
#     "name": "Example",
#     "value": "My_cooka"
# })
#
# print(driver.get_cookie("Example"))

# before = driver.get_cookie("split")
# print(before)
# driver.delete_cookie("split")
# driver.add_cookie({
#     "name": "split",
#     "value": "SOMETHING"
# })
# after = driver.get_cookie("split")
# print(after)

# before = driver.get_cookies()
# print(before)
# driver.delete_all_cookies()
# # driver.add_cookie({
# #     "name": "split",
# #     "value": "SOMETHING"
# # })
# after = driver.get_cookies()
# print(after)

# LOGIN_FIELD = ("id", "login_email")
# PASSWORD_FIELD = ("id", "password")
# SUBMIT_BUTTON = ("id", "loginformsubmit")
# # Логинимся в аккаунт
# driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
# driver.find_element(*PASSWORD_FIELD).send_keys("123")
# driver.find_element(*SUBMIT_BUTTON).click()
# pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookies.pkl", "wb"))

driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)
driver.refresh()
time.sleep(5)


"""
－Методы для работы с cookies:
➖ get_cookie(name) - Получить куку по имени
➖ get_cookies() - Получить все куки
➖ add_cookie({"name": "example", "value": "123"}) - Добавление 
➖ delete_cookie(name) - Удаление куки по имени
➖ delete_all_cookies() - Удаление всех куков

"""

driver.quit()