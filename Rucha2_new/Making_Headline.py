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
driver.get("https://seleniumplayground.practiceprobs.com/")
time.sleep(5)

# 2.Print headline
drop_down=driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div[1]/div/div/nav/label/a')
print(drop_down.get_attribute('title'))
time.sleep(1)

