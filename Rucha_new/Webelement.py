import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/hris-hr-software-demo/")

print(driver.title)
first_name=driver.find_element(By.ID,'Form_submitForm_FirstName')
last_name=driver.find_element(By.ID,'Form_submitForm_LastName')
email=driver.find_element(By.ID,'Form_submitForm_Email')
phonenumber=driver.find_element(By.ID,'Form_submitForm_Contact')
country=driver.find_element(By.ID,'Form_submitForm_Country')
Platform_link= driver.find_element(By.LINK_TEXT,'Platform')

first_name.send_keys('Rucha ')
last_name.send_keys('Kardani')
email.send_keys('rucha.tagline@gmail.com')
phonenumber.send_keys('999999999')
country.send_keys('India')
Platform_link.click()

time.sleep(3)