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
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)

driver.find_element(By.ID,'justAnInputBox').click()

drop_list=driver.find_element(By.CSS_SELECTOR,'#comboTree882171DropDownContainer > ul > li:nth-child(1) > span')

for ele in drop_list:
    print(ele.text)
    if ele.text=='choice 2':
        ele.click()
        break


time.sleep(4)