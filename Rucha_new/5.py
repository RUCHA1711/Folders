import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://demo-store.seleniumacademy.com/")
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="select-language"]').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="select-language"]/option[1]').click()
time.sleep(2)

language_variable='English'
print('Language is English')

driver.find_element(By.XPATH,'//*[@id="select-language"]/option[2]').click()
time.sleep(2)

language_variable1='French'
print('Language is French')

driver.find_element(By.XPATH,'//*[@id="select-language"]/option[3]').click()
time.sleep(2)

language_variable1='German'
print('Language is German')
