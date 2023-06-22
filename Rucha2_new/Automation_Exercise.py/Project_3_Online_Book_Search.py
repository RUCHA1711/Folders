from unittest import result
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#1.Verify te site url 
driver.get("https://automationbookstore.dev/")
time.sleep(1)
if(driver.get==driver.current_url):
    print('Url is verified')
else:
    print('Url is verified')
time.sleep(1)

# 2. Verify that the site title and heading is Automation Bookstore
title=driver.find_element(By.ID,'page-title')
if(title):
    print('Title is Verified')
else:
    print('Title is not verified')
time.sleep(1)

# 3. Verify that placeholder in the search box is Filter books
placeholder=driver.find_element(By.ID,'searchBar')
if(placeholder):
    print('Placeholder is verified')
else:
    print('Placeholder is not verified')

# 4. Verify that there are total 8 books in the page
total_books=driver.find_element(By.ID,'productList')
print(len(total_books))

for i in total_books:
    


# 5. Print the name of the books
name1=driver.find_element(By.ID,'pid1_title').text
name2=driver.find_element(By.ID,'pid2_title').text
name3=driver.find_element(By.ID,'pid3_title').text
name4=driver.find_element(By.ID,'pid4_title').text
name5=driver.find_element(By.ID,'pid5_title').text
name6=driver.find_element(By.ID,'pid6_title').text
name7=driver.find_element(By.ID,'pid7_title').text
name8=driver.find_element(By.ID,'pid8_title').text
print(f'Book names are \n {name1} \n {name2} \n {name3} \n {name4} \n {name5}\n {name6}\n {name7} \n {name8}')

# 6. 

