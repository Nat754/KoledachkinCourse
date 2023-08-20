import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

"""Получить урл открытой страницы"""
driver.get('https://ria.ru/')

url = driver.current_url
time.sleep(3)
print("Url страницы: ", url)

current_title = driver.title
print("Текущий заголовок: ", current_title)

assert url == 'https://ria.ru/', 'Некоректный адрес страницы'
assert 'РИА Новости' in current_title, 'Это неправильный заголовок'
time.sleep(3)
driver.quit()
