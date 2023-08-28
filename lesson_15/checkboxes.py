import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")
CHECKBOX_2 = ("xpath", "(//input[@type='checkbox'])[2]")

driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(3)
print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))  # None - нет атрибута
driver.find_element(*CHECKBOX_1).click()
print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))
print(type(driver.find_element(*CHECKBOX_1).get_attribute("checked")))  # Тип str - true (assert == "true)
time.sleep(3)



"""
－Ссылки на тренажеры из видео:
➖ Простые чек-боксы: https://the-internet.herokuapp.com/checkboxes
➖ Чек-боксы с нюансами: https://demoqa.com/checkbox
➖ Современные чек-боксы: https://demoqa.com/selectable
➖ Радио-кнопки: https://demoqa.com/radio-button
"""

driver.close()
