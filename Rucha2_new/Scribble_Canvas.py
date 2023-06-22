import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1. Goto url
driver.get("https://testpages.herokuapp.com/styled/gui-scribble.html")
time.sleep(5)

# 2. Draw in canvas
canvas=driver.find_element(By.ID,'canvas')
time.sleep(1)

drawing = ActionChains(driver)\
    .click_and_hold(canvas)\
    .move_by_offset(50, 55)\
    .move_by_offset(50, 32)\
    .move_by_offset(20, 25)\
    .release()
drawing.perform()