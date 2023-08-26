import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=0.3)

driver.get("https://demoqa.com/alerts")

# BUTTON_1 = ("xpath", "//button[@id='alertButton']")
# wait.until(es.element_to_be_clickable(BUTTON_1)).click()
#
# alert = wait.until(es.alert_is_present())
# time.sleep(3)
# driver.switch_to.alert
# time.sleep(3)
# alert.accept()

# BUTTON_3 = ("xpath", "//button[@id='confirmButton']")
# wait.until(es.element_to_be_clickable(BUTTON_3)).click()
#
# alert = wait.until(es.alert_is_present())
#
# time.sleep(3)
#
# driver.switch_to.alert
#
# time.sleep(3)
# print(alert.text)
# alert.dismiss()
#
# time.sleep(3)

BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(es.element_to_be_clickable(BUTTON_4)).click()

alert = wait.until(es.alert_is_present())

time.sleep(3)

driver.switch_to.alert

time.sleep(3)

alert.send_keys('Wow!!!')

time.sleep(3)

alert.accept()

time.sleep(3)

driver.quit()
