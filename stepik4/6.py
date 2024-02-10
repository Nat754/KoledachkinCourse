from selenium import webdriver
from selenium.webdriver.firefox.options import Options


"""
Инициализировать драйвер (любой, попробуйте Firefox) p.s: не забудьте его установить.
Открыть любую страницу, например: vk.com.
Получить и вывести title в консоль.
Открыть любую другую страницу, например: ya.ru.
Получить и вывести title в консоль.
Вернуться назад и, используя assert, убедиться, что вы точно вернулись обратно.
Сделать рефреш страницы.
Получить и вывести URL-адрес текущей страницы.
Вернуться "вперед" на страницу из пункта 4.
Убедиться, что URL-адрес изменился.
"""

driver = webdriver.Firefox(options=Options())


def get_page_title(url):
    driver.get(url)
    page_title = driver.title
    return page_title


url1 = 'https://vk.com/'
print(get_page_title(url1))
url2 = 'https://ya.ru/'
print(get_page_title(url2))
driver.back()
assert driver.current_url == url1, 'Не произошел переход назад'
driver.refresh()
refresh_url = driver.current_url
print(refresh_url)
driver.forward()
forward_url = driver.current_url
print(forward_url)
assert refresh_url != forward_url, 'Не изменился адрес страницы'
driver.quit()
