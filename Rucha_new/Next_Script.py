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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1.Goto url
driver.get("http://live.techpanda.org/")
time.sleep(2)

# 2.Click on 'MOBILE' menu
driver.find_element(By.CLASS_NAME,'level0 ').click()
time.sleep(2)

# 3.Note the price of the Sony Experia
cost=driver.find_element(By.XPATH,'//*[@id="product-price-1"]/span')
# print(cost.text)

sony=cost.text

# 4.Click on Sony Experia mobile
driver.find_element(By.XPATH,'//*[@id="product-collection-image-1"]').click()
time.sleep(2)

# 5.Compare values in step 3 and step 5
read=driver.find_element(By.XPATH,'//*[@id="product-price-1"]/span')
# print(read.text)

price=read.text
if(price == sony):
    print('Test Pass')
else:
    print('Test fail')
   