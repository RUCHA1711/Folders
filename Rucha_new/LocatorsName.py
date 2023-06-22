import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/index.html")

print(driver.title)

username=driver.find_element(By.NAME,'username')
password=driver.find_element(By.NAME,'password')
login_button=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div/input')

username.send_keys('Rucha Tagline')
password.send_keys('Test@123')
login_button.click()


time.sleep(5)

