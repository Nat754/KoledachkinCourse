import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=0.3)

driver.get("https://www.freeconferencecall.com/en/us/login")
# print(driver.get_cookie("country_code"))

print(driver.get_cookies())


"""
－Методы для работы с cookies:
➖ get_cookie(name) - Получить куку по имени
➖ get_cookies() - Получить все куки
➖ add_cookie({"name": "example", "value": "123"}) - Добавление 
➖ delete_cookie(name) - Удаление куки по имени
➖ delete_all_cookies() - Удаление всех куков

"""

driver.quit()