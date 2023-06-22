from re import S
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
options=webdriver.ChromeOptions()
options.headless=True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(ChromeDriverManager().install(),options= options)
driver.maximize_window()
driver.get("https://seleniumplayground.practiceprobs.com/dogs/")

driver.find_element(By.XPATH,'/html/body/div[3]/main/div/div[1]/div/div/nav/ul/li[2]/nav/ul/li/div').click()
time.sleep(1)

S=lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('dogsbreed.png')
driver.quit()