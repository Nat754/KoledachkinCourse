"""
На странице https://testautomationpractice.blogspot.com/

Найти иконку Wikipedia по имени класса
Найти поле ввода Wikipedia по id
Найти кнопку поиска Wikipedia по классу
Найти любой другой элемент на странице по тегу
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(options=Options())


url = 'https://testautomationpractice.blogspot.com/'
driver.get(url)
driver.find_element('class name', 'wikipedia-icon')
driver.find_element('id', 'Wikipedia1_wikipedia-search-input')
driver.find_element('class name', 'wikipedia-search-button')
driver.find_element('tag name', 'span')
driver.quit()
