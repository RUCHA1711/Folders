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

# 2.Go to Mobile and add iPhone to cart
driver.find_element(By.XPATH,'//*[@id="nav"]/ol/li[1]/a').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[3]/div/div[3]/button').click()
time.sleep(2)

# 3.Enter Coupon code
driver.find_element(By.ID,'coupon_code').send_keys('GURU50')
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="discount-coupon-form"]/div/div/div/div/button').click()
time.sleep(2)

# 4.Verify the discount generated
discount=driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div/div/ul/li/ul/li')

if(discount):
    print('Price is discounted by 5%')
else:
    print('Price is not discounted by 5%')
time.sleep(2)