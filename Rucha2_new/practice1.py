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
driver.get("http://www.demo.guru99.com/V4/")
time.sleep(2)

# 2.Enter Valid Userid and Password
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[1]/td[2]/input').send_keys('mngr458738')
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td[2]/input').send_keys('UtUpUzY')
time.sleep(1)

# 3.Click login button
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[3]/td[2]/input[1]').click()
time.sleep(1)

# 4. Output
output=driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/marquee')

if(output):
    print('Successfully logged in')
else:
    print('Not abled to log in')




