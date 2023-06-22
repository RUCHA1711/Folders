import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")

linksList=driver.find_elements(By.TAG_NAME,'a')
print(len(linksList))

for ele in linksList:
    link_text= ele.text
    print(link_text)
    print(ele.get_attribute('href')) 

imageList=driver.find_elements(By.TAG_NAME,'img')
print(len(imageList))

for ele in imageList:
    print(ele.get_attribute('src'))
