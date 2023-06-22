import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.amazon.com/")

element = driver.find_element(By.XPATH, '//*[@id="searchDropdownBox"]')
drop = Select(element)

for i in drop.options:
    print(i.text)
