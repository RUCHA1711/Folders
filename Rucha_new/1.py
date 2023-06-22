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

# variable(Opens a google)
url="https://www.google.com/"
driver.get(url)
time.sleep(2)

# Verify that title is Google
get_title=driver.title
title='Google'

if get_title==title:
  print('Title is verified')
else:
  print('Title is not verified')

#Check whether it is redirected to the google.com
result=driver.current_url
print(result)

if result =='https://www.google.com/':
  print('Test Pass')
else:
    print('Test Fail')
                
