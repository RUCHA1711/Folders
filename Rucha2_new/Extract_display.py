import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1.Goto Url
driver.get("https://en.m.wikipedia.org/wiki/Maharana_Pratap")
time.sleep(2)

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))
time.sleep(2)

for i in links:
    link_text=i.text
    print(link_text)
    print(i.get_attribute('href'))

    