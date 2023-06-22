import selenium
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()



driver.get("https://www.amazon.com/")
time.sleep(2)
# links = driver.find_elements(By.TAG_NAME,'a')
# for i in links:
#     link_text = i.text
#     print(link_text)
#     print(i.get_attribute("href"))




links = driver.find_elements(By.TAG_NAME,"a")
for link in links:
    print(link.get_attribute("href")) 
    r = requests.head(link.get_attribute('href'))
    print(link.get_attribute('href'), r.status_code)

if links.status_code != 200:
    print('No broken link')
else:
    print('Link is broken')
