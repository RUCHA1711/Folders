import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(2)

def first_row_data():
    row_list=[]
    for r in row_list:
        row_list.append(r.text)
    return row_list
   
data=first_row_data()

header_xpath = driver.find_element()
empty_dictionary = {}
idx = 0
for column in header_xpath:
     empty_dictionary[column.text] = data[idx]

print(empty_dictionary)

# def entire_table():
#     whole_table_data = driver.find_elements(By.ID,'table1')
#     for a in whole_table_data:
#         print(a.text)
# entire_table()

# print({"Last Name": "Smith", "First Name": "John", "Email": "jsmith@gmail.com", "Due": "$50.00"})



