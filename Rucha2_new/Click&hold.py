# import webdriver
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# create webdriver object
# driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_link_text("Courses")

# create action chain object
action = ActionChains(driver)

# click and hold the item
action.click_and_hold(on_element=element)

# perform the operation
action.perform()
