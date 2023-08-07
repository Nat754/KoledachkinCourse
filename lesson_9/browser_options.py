import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

"""
- Опции:
➖ Безголовый режим "--headless"
➖ Режим инкогнито "--incognito"
➖ Игнорирование ошибок сертификатов "--ignore-certificate-errors"
➖ Размер окна браузера "--window-size=X,Y"
➖ Отключение кеширования "--disable-cache"

－Методы:
➖ Добавление новой опции - add_argument("--имя_опции")
➖ Установка размера окна - driver.set_window_size(1920, 1080)
➖ Развернуть окно браузера на весь экран - driver.maximize_window()

- Хардкдинг стратегии загрузки:
➖ chrome_options.page_load_strategy = "normal" - дожидается загрузки всех ресурсов
➖ chrome_options.page_load_strategy = "eager" - дожидается загрузки DOM
"""

"""Объект опций и сами опции д.б. объявлены до драйвера!"""
chrome_options = webdriver.ChromeOptions()
# chrome_options.page_load_strategy = 'normal'
# result = 104.11714577674866
# chrome_options.page_load_strategy = 'eager'
# result = 2.4516115188598633
# chrome_options.add_argument('--headless')
"""Запускает браузер в фоне"""

# chrome_options.add_argument('--incognito')
"""Позволяет не использовать кеш и не сохранять данные"""

# chrome_options.add_argument('--ignore-certificate-errors')
"""Игнор SSL сертификатов"""

chrome_options.add_argument('--window-size=400,400')
"""Сразу открывает в окне этого размера"""

chrome_options.add_argument('--disable-cache')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.set_window_size(400, 400)
"""Сначала открывает в окне по умолчанию, а потом в указанном"""

# driver.maximize_window()

start_time = time.time()
driver.get('https://whatismyipaddress.com')

"""for '--ignore-certificate-errors'"""
# driver.get('http://expired.badssl.com')

end_time = time.time()
result = end_time - start_time
print(result)
