import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://qxf2.com/selenium-tutorial-main")
time.sleep(2)

# Print the title of the Page
get_title = driver.title
print(get_title)

# Scroll the page
driver.execute_script('window.scrollBy(0,1000)')
time.sleep(2)

# Fill the form
driver.find_element(By.ID,'name').send_keys('Tester')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="myform"]/div[2]/input').send_keys('rucha@yopmail.com')
time.sleep(2)
driver.find_element(By.ID,'phone')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="myform"]/div[4]/button').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="myform"]/div[4]/ul/li[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="myform"]/p/button').click()
time.sleep(2)


try:
	driver.find_element(By.XPATH,'//*[@id="phone"]')
except Exception as e:
	
	result_flag = False
else:
	result_flag = True


if result_flag is True:
	print("Validation message for Phone number is present")
else:
	print("Validation message for Phone number is NOT present")