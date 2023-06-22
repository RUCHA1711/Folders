import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import pandas as pd

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://demo-store.seleniumacademy.com/")


# Read the csv file
data = pd.read_csv('/Users/tagline_145/Downloads/test.csv')

# Print it 
print(data)

for row in data.index:
     name = data.loc[row, "name"]
     total_results = data.loc[row, "total_results"]
     print(name, total_results)


def search_name(name,total_results):
    
