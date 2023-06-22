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

# Navigate to url:
url = "http://qatechhub.com"
driver.get(url)
time.sleep(2)

# Get title of the page
get_title = driver.title
title = "QA Automation Tools Trainings and Tutorials | QA Tech Hub"

# Method to print if the title of the page matches
if (get_title == title):
    print('pass')
else:
    print('Fail')
time.sleep(2)

# Navigate to google.com
url2 = "https://www.google.com"
driver.get(url2)
time.sleep(2)

# Navigate back to the QA Tech Hub website
driver.back()
time.sleep(2)

# Print the url of the current page
print(driver.current_url)
time.sleep(2)

# Navigate to forward
driver.forward()
time.sleep(2)

# Reload the page
driver.refresh()
time.sleep(2)

driver.quit()
