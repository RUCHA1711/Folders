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

# 2.Click on 'MOBILE' menu
driver.find_element(By.CLASS_NAME, 'level0 ').click()
time.sleep(2)

# 3.Click on 'Add to compare' button in Sony Xperia
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/div/div[3]/ul/li[2]/a').click()
time.sleep(2)

# 4.Click on 'Add to compare' button in Iphone
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[2]/div/div[3]/ul/li[2]/a').click()
time.sleep(5)

# 5.Clik on 'Add to compare button' to compare 2 device
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[3]/div[1]/div[2]/div/button').click()
time.sleep(2)

# 6.Verify the pop-up window
verify=driver.find_element(By.XPATH,'//*[@id="top"]/body')
time.sleep(2)

if(verify):
    print('Pass')
else:
    print('Fail')
time.sleep(2)

# 7.Close the Popup Windows
driver.find_element(By.XPATH,'/html/body/div/div[2]/button').click()
time.sleep(10)