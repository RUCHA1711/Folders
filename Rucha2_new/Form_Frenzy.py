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
driver.get("https://seleniumplayground.practiceprobs.com/contact/")
time.sleep(5)

# 2.Your Name
driver.find_element(By.XPATH,'//*[@id="contact-form"]/p[1]/label/input').send_keys('Rucha')
time.sleep(1)

# 3.Your Email
driver.find_element(By.XPATH,'//*[@id="contact-form"]/p[2]/label/input').send_keys('rucha.tagline@gmail.com')
time.sleep(1)

# 4.Your fav dog breed
driver.find_element(By.CLASS_NAME,'')


