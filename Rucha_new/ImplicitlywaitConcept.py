import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
# time out=10
# dynamic wait
# imp wait will be applied for all the web elements
# global wait
# find_element
# find_elements
# only for web elements


driver.get("https://app.hubspot.com/login")
print(driver.title)
user_name=driver.find_element(By.ID,'username')
user_name.send_keys("test@gmail.com")

driver.find_element(By.ID,'password').send_keys("test@12345")


time.sleep(3)
