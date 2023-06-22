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

# 1.Goto url
driver.get("http://live.techpanda.org/")
time.sleep(2)

# 2.Click on My account link
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[3]/div/div[4]/ul/li[1]/a').click()
time.sleep(2)

# 3.Login in application using previously created credential
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys('shreya.tagline@gmail.com')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys('Tester123')

driver.find_element(By.XPATH, '//*[@id="send2"]').click()

# 4.Click on 'My orders'
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/div/div[2]/ul/li[4]/a').click()

time.sleep(10)

# 5.Click on 'View order'

driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[6]/span').click() 
time.sleep(2)

# 6.Verify the previously created order is displayed in 'Recent orders' table and status is Pending
# Recent_orders=driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div')

# if(Recent_orders):
#     print('previously created order is displayed in Recent orders table and status is Pending')
# else:
#     print('nothing')

# time.sleep(2)

# 7.Click on 'Print Order' link
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div/div[1]/a[2]').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="sidebar"]//print-preview-button-strip//div/cr-button[2]').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div[4]/button').click()
time.sleep(2)