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
driver.get("http://live.techpanda.org/")
time.sleep(2)

# 2.Verify Title of page
get_title=driver.title

title='Home page'

if(get_title==title):
    print('This is demo site shown in the home page')
else:
    print('Nothing')

# driver.find_element(By.CLASS_NAME,'level0 ').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,'level0 ').click()
time.sleep(2)

# 4.Verify Title of the page
get_title1=driver.title

title1='Mobile'

if(get_title1==title1):
    print('Title Mobile is shown on the mobile list page')
else:
    print('Nothing')

# 5.In the list of all mobile,select 'sort by' dropdwon as 'name'.
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/select/option[2]').click()
time.sleep(2)

# 6.Verify all products are sorted by name
product_names=driver.find_elements(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[3]/div/h2')
time.sleep(2)

if(product_names):
    print('All 3 products sorted by name')