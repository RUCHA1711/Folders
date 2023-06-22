from select import select
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://login-staging.gwork.io/")

# Login
driver.find_element(By.ID, "identity").send_keys("sandy@gmail.com")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "gdpr-cookie-accept").click()
driver.find_element(By.CLASS_NAME, "login-btn").click()
time.sleep(1)
# Performance
driver.find_element(By.XPATH,'//*[@id="sidebar"]/ul/li[3]/a/span').click()
time.sleep(5)
# Percentage
# driver.find_element(By.XPATH,'//*[@id="main-body"]/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div/a').click()
# time.sleep(3)
# driver.find_element(By.XPATH,'//*[@id="overview1"]/div/div[1]/a/img').click()
# time.sleep(3)
# driver.find_element(By.XPATH,'//*[@id="main-body"]/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/a/img').click()
# time.sleep(3)
# driver.find_element(By.XPATH,'//*[@id="overview2"]/div/div[1]/a/img').click()
# time.sleep(3)
# Checkbox

# driver.find_element(By.XPATH,'//*[@id="convert_checkbox"]/input').click()
# time.sleep(2)
# driver.find_element(By.XPATH,'//*[@id="select2-type-container"]').click()
# time.sleep(2)

# Drop-down

# for i in range(2,8):
#     driver.find_element(By.XPATH,f'//*[@id="type"]/option[{i}]').click()
#     time.sleep(4)
   
driver.find_element(By.XPATH,'//*[@id="performance_tab"]/div[1]/div/div[4]').click()
time.sleep(2)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
# Create performance

driver.find_element(By.XPATH,'//*[@id="performance_tab"]/div[1]/div/div[4]/a').click()
time.sleep(3)

# for _ in range(4):
#  driver.find_element(By.XPATH,'//*[@id="projects-carousel"]/div[2]/div[2]/i').click()
#  time.sleep(2)
# User 
driver.find_element(By.XPATH,'//*[@id="projects-carousel"]/div[1]/div/div[1]/div/div').click()
time.sleep(2)
# Next button
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[4]/button[2]').click()
time.sleep(2)
# drop-down
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[2]/div[1]/div/div/div/select').click()
time.sleep(2)
# Select option(Monthly)
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[2]/div[1]/div/div/div/select/option[3]').click()
time.sleep(2)
#on which date submit review(drop-down)
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[2]/div[2]/div/div/div[3]/select').click()
time.sleep(2)
#(17 date selected)
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[2]/div[2]/div/div/div[3]/select/option[18]').click()
time.sleep(2)
# On which date like to disucuss results(drop-down)
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[2]/div[2]/div/div/div[4]/select').click()
time.sleep(2)
#(18 selected)
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[2]/div[2]/div/div/div[4]/select/option[19]').click()
time.sleep(2)
#End date
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[2]/div[3]/div/div/div/input').click()
time.sleep(2)
#end date(24)
driver.find_element(By.XPATH,'//*[@id="main-body"]/div[6]/div[1]/table/tbody/tr[4]/td[6]').click()
time.sleep(2)
# Next button
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[4]/button[2]').click()
time.sleep(2)
#Namne of PO
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[3]/div[1]/div/div[1]/div/div/div[1]/input').send_keys('Test')
time.sleep(2)
#Weighting 
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[3]/div[1]/div/div[1]/div/div/div[2]/input').send_keys('50')
time.sleep(2)
#Describe PO
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[3]/div[1]/div/div[2]/div/div/div/textarea').send_keys('Hello')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[3]/div[1]/div/div[2]/div/div/div/input').send_keys('Testing')
time.sleep(2)
# How will the performance objective be measured:
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[3]/div[1]/div/div[3]/div/div/div/div/div/div/div[1]/input').send_keys('creativity')
time.sleep(2)
#Weighting 
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[3]/div[1]/div/div[3]/div/div/div/div/div/div/div[2]/input').send_keys('100')
time.sleep(2)
#Ratings(3)
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[3]/div[1]/div/div[4]/div/div/div/div/div/div/div[1]/div/label[3]').click()
time.sleep(2)
#url
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[3]/div[1]/div/div[5]/div/div/div/input').send_keys('https://mail.google.com/mail/u/0/#inbox')
time.sleep(2)
#drop down
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[3]/div[1]/div/div[6]/div/div/div/div/select').click()
time.sleep(2)
#drop down selection(Happy Employees) 
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[2]/div[3]/div[1]/div/div[6]/div/div/div/div/select/option[5]').click()
time.sleep(5)
#Next Button 
driver.find_element(By.XPATH,'//*[@id="performance_from"]/div/div[4]/button[2]').click()
time.sleep(5)
# Confirm Button
driver.find_element(By.XPATH,'//*[@id="performance_from"]/button[2]').click()
time.sleep(4)





