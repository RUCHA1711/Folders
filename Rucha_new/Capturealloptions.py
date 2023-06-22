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
  
# Web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
  
  
# Find id of option
x = driver.find_element_by_id('RESULT_RadioButton-9')
drop = Select(x)
# x is object variable name
# Count number of options
print(len(drop.options))
  
# Capture all the options
# for i in drop.options:
#     print(i.text)
  
# driver.close()