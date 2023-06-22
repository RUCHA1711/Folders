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

# 1.Goto url
driver.get("https://itera-qa.azurewebsites.net/home/automation")
time.sleep(2)

# 2.Name 
driver.find_element(By.ID,'name').send_keys('Tester')
time.sleep(1)

# 3.Mobile number
driver.find_element(By.ID,'phone').send_keys('9727768234')
time.sleep(1)

# 4.Email Address
driver.find_element(By.ID,'email').send_keys('rucha.tagline@gmail.com')
time.sleep(1)

# 5.Password
driver.find_element(By.ID,'password').send_keys('Tester@123')
time.sleep(1)

# 6.Address
driver.find_element(By.ID,'address').send_keys('Apple Square')
time.sleep(1)

# 7.Click on submit button
driver.find_element(By.NAME,'submit').click()
time.sleep(2)


driver.execute_script('window.scrollBy(0,2000)')

# 8.Gender
driver.find_element(By.ID,'female').click()
time.sleep(1)

# 9.Which days of the week are best to start something new?
driver.find_element(By.ID,'tuesday').click()
time.sleep(1)
driver.find_element(By.ID,'friday').click()
time.sleep(1)


# driver.execute_script('window.scrollBy(0,2000)')
# 10.Where do you plan to travel this year?
driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/select/option[2]').click()
time.sleep(1)    

# 11.Select the Radio button (2 years) for category Years of experience in test automation 
driver.find_element(By.XPATH,'/html/body/div/div[5]/div[2]/div[1]/div[2]/label').click()
time.sleep(1)

# 12.Check the Check Box ‘Selenium Webdriver’ and TestNG for category ‘Which automation tools/frameworks do you use?'
driver.find_element(By.XPATH,'/html/body/div/div[5]/div[2]/div[2]/div[1]/label').click()
time.sleep(1)

driver.quit()
