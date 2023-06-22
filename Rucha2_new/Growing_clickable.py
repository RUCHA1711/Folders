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

# 1.Goto url
driver.get("https://testpages.herokuapp.com/styled/challenges/growing-clickable.html")
time.sleep(5)

# 2.Click Me button
ele = driver.find_element(By.XPATH,'//*[@id="growbutton"]').click()
time.sleep(5)
action = ActionChains(driver)
action.double_click(on_element = ele)
action.perform()
