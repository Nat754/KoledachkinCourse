import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# для 1 и 2
# driver.get('https://demoqa.com/dynamic-properties')

# 1)
# VISIBLE_AFTER_BUTTON = ('xpath', '//button[@id="visibleAfter"]')
# BUTTON = wait.until(es.visibility_of_element_located(VISIBLE_AFTER_BUTTON))
# BUTTON.click()

# 2)
# ENABLE_IN_SECONDS = ('xpath', '//button[@id="enableAfter"]')
# BUTTON = wait.until(es.element_to_be_clickable(ENABLE_IN_SECONDS))
# BUTTON.click()

# для 3, 4
driver.get('https://the-internet.herokuapp.com/dynamic_controls')

# 3)
# REMOVE_BUTTON = ('xpath', '//button[text()="Remove"]')
# driver.find_element(*REMOVE_BUTTON).click()
# wait.until(es.invisibility_of_element_located(REMOVE_BUTTON))
# print('Все ОК!')

# 4
ENABLE_BUTTON = ('xpath', '//button[text()="Enable"]')
TEXT_FIELD = ('xpath', '//input[@type="text"]')

wait.until(es.element_to_be_clickable(ENABLE_BUTTON)).click()
time.sleep(2)
wait.until(es.element_to_be_clickable(TEXT_FIELD)).send_keys('Привет!')
time.sleep(2)
wait.until(es.text_to_be_present_in_element_value(TEXT_FIELD, 'Привет!'))
time.sleep(2)
print('Все ОК!')
