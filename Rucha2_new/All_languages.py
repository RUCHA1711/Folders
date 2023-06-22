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

driver.get("https://www.wikipedia.org/")
time.sleep(2)

all_languages=driver.find_elements(By.TAG_NAME,'a')
print(len(all_languages))


for i in all_languages:
    all_languages=i.text
    print(all_languages)
    print(i.get_attribute('href'))