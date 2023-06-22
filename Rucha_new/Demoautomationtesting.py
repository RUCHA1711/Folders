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

driver.get("https://demo.automationtesting.in/FileDownload.html") 
time.sleep(2)
# Write something in input box
driver.find_element(By.ID,'textbox').send_keys('Automation Testing')
time.sleep(2)
#Click on generate file button
driver.find_element(By.ID,'createTxt').click()
time.sleep(2)
# Download file
driver.find_element(By.ID,'link-to-download').click()
time.sleep(2)