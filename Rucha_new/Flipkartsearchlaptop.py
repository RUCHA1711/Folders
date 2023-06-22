
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
driver.get('https://www.flipkart.com/')
time.sleep(2)
# Click on cross button
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/button').click()
time.sleep(2)
#Search laptop model
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys('laptop')
time.sleep(2)
#Hit Enter
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys(Keys.ENTER)
time.sleep(2)
#Choose and click any one laptop model
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]').click()
time.sleep(2)
# Add to cart
driver.find_element(By.XPATH,'').click()
time.sleep(2)


