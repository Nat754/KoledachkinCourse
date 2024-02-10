import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


"""
－Методы из урока:
➖ is_selected() - Возвращает статус чекбокса и радио-кнопки
➖ is_enabled() - Проверяет доступен ли элемент для взаиодействия
➖ get_attribute(атрибут) - Получает указанный атрибут элемента
"""

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")
CHECKBOX_HOME = ("xpath", "//input[@id='tree-node-home")
CHECKBOX_HOME_STATUS = ("xpath", "//input[@id='tree-node-home']")
CHECKBOX_HOME_ACTION = ("xpath", "//span[@class='rct-checkbox']")
ELEMENT_ONE = ("xpath", "//li[text()='Cras justo odio']")
YES_RADIO_STATUS = ("id", "yesRadio")
YES_RADIO_ACTION = ("xpath", "//label[@for='yesRadio']")
NO_RADIO_STATUS = ("id", "noRadio")
NO_RADIO_ACTION = ("xpath", "//label[@for='noRadio']")

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# time.sleep(3)
# # print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))  # None - нет атрибута
# # driver.find_element(*CHECKBOX_1).click()
# # print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))
# # print(type(driver.find_element(*CHECKBOX_1).get_attribute("checked")))  # Тип str - true (assert == 'true')
#
# print(driver.find_element(*CHECKBOX_1).is_selected())
# """Возвращает выбран или нет чек-бокс (False или True)"""
# driver.find_element(*CHECKBOX_1).click()
# print(driver.find_element(*CHECKBOX_1).is_selected())

# driver.get("https://demoqa.com/checkbox")
# # driver.find_element(*CHECKBOX_HOME).click()
# """
# # ElementIsNotInteractible - элемент перекрыт другими элементами на странице и не может быть выбран!
# Используем этот элемент для получения статуса
# """
# print(driver.find_element(*CHECKBOX_HOME_STATUS).get_attribute("checked"))
# driver.find_element(*CHECKBOX_HOME_ACTION).click()
# print(driver.find_element(*CHECKBOX_HOME_STATUS).get_attribute("checked"))

# driver.get("https://demoqa.com/selectable")
# before = driver.find_element(*ELEMENT_ONE).get_attribute("class")  # mt-2 list-group-item list-group-item-action
# # print(before)
# driver.find_element(*ELEMENT_ONE).click()
# after = driver.find_element(*ELEMENT_ONE).get_attribute("class")  # mt-2 list-group-item active list-group-item-action
# # print(after)
# assert 'active' in after, 'Элемент не выбран'

"""
для того чтобы заморозить выполнение джаваскрипта в консоле браузера введите вот этот код: setTimeout(function(){debugger;}, 5000) и нажмите энтер
"""

driver.get("https://demoqa.com/radio-button")
print('YES выбрана?', driver.find_element(*YES_RADIO_STATUS).is_selected())
driver.find_element(*YES_RADIO_ACTION).click()
print('YES выбрана?', driver.find_element(*YES_RADIO_STATUS).is_selected())

print('YES доступна для взаимодействия?', driver.find_element(*YES_RADIO_STATUS).is_enabled())
print('NO доступна для взаимодействия?', driver.find_element(*NO_RADIO_STATUS).is_enabled())


time.sleep(3)
driver.close()
