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
driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
driver.execute_script('window.scrollBy(0,500)')

# def select_values(element,value):
#     select=Select(element)
#     select.select_by_visible_text(value)

def select_values_from_dropdown(dropDownOptionsList, value):
    print(len(dropDownOptionsList))
    for ele in dropDownOptionsList : 
        print(ele.text)
        if ele.text == value :
            ele.click()
            break

country_options=driver.find_elements(By.XPATH,'//*[@id="Form_submitForm_Country"]')
select_values_from_dropdown(country_options,'America')
select_values_from_dropdown(country_options,'India') 

# ele_country=driver.find_element(By.ID,'Form_submitForm_Country')
# select_values(ele_country,'China')

# select=Select(ele_country)
# country_list=select.options

# for ele in country_list:
#     print(ele.text)
#     if(ele.text=="India"): 
#        ele.click()
#        break

# select=Select(ele_country)

# select.select_by_visible_text('Canada')
# select.select_by_index(2)
# select.select_by_value('France')

# country_options=driver.find_elements(By.XPATH,'//*[@id="Form_submitForm_Country"]')
# print(len(country_options))
# for ele in country_options:
#     print(ele.text)
#     if ele.text =='China':
#         ele.click()
#         break




time.sleep(3)