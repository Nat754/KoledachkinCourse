import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1280,960")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, "
                     "like Gecko) Chrome/115.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

# скриншот
# driver.get("https://dzen.ru")
# driver.save_screenshot("screen.png")

# Сайт для проверки WebDriver мода и user-agent:
# driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
# time.sleep(3)
# Список user-agents:  https://www.useragents.me/
driver.get("https://whatismyipaddress.com/")
driver.save_screenshot("screen.png")      
wait.until(es.title_is("What Is My IP Address - See Your Public Address - IPv4 & IPv6"))

# в безголовом режиме дает ошибку:
# Traceback (most recent call last):
#
#   File "C:\Users\natam\PycharmProjects\KoledachkinCourse\lesson_12\become_human.py", line 30, in <module>
#     wait.until(es.title_is("What Is My IP Address - See Your Public Address - IPv4 & IPv6"))
#   File "C:\Users\natam\PycharmProjects\KoledachkinCourse\venv\Lib\site-packages\selenium\webdriver\support\wait.py",
#   line 95, in until
#       raise TimeoutException(message, screen, stacktrace)
# selenium.common.exceptions.TimeoutException: Message:
#  --user-agent=Mozilla/5.0... решает эту проблему  good.png
time.sleep(5)
