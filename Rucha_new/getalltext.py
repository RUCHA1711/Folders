# Importing necessary modules
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# WebDriver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# Target URL
driver.get("https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")

# print(driver.title)

# Printing the whole body text
print(driver.find_element_by_xpath("/html/body").text)

# Closing the driver
driver.close()

