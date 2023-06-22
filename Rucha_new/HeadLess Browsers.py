from turtle import title
from requests import options
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
options=webdriver.ChromeOptions()
# options.headless=False
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
options.add_argument('--headless')

# options=webdriver.FirefoxOptions()
# options.headless=True
# driver=webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
driver.implicitly_wait(10)
driver.get("http://amazon.in")
print(driver.title)
time.sleep(5)