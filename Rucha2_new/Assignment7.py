import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver = webdriver.Chrome(executable_path="/Users/tagline_145/Downloads/chromedriver")
driver.maximize_window()
driver.get('https://www.gmail.com/')
time.sleep(2)
# driver.find_element(By.XPATH,'/html/body/header/div/div/div/a[2]').click()
# time.sleep(2)
driver.find_element(
    By.XPATH, '//*[@id="identifierId"]').send_keys('harshvaddoriya21@gmail.com')
time.sleep(2)
driver.find_element(
    By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
time.sleep(2)
driver.implicitly_wait(4)
driver.find_element(
    By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Tagline@123')
time.sleep(2)
driver.find_element(
    By.XPATH, '//*[@id="passwordNext"]/div/button/div[3]').click()
time.sleep(2)

if driver.current_url == "https://mail.google.com/mail/u/0/#inbox":
    print('gmail is logged in successfully')
else:
    print('gmail is not logged in successfully')
driver.find_element(
    By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div').click()
time.sleep(2)

if driver.current_url == "https://mail.google.com/mail/u/0/#inbox?compose=new":
    print('New window is opened')
else:
    print('New window is not opened')
time.sleep(2)

driver.find_element(
    By.XPATH, '//*[@id=":to"]').send_keys('rucha.tagline@gmail.com')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id=":pu"]').send_keys('Test Mail')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id=":r0"]').send_keys('Hey there')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id=":pk"]').click()
time.sleep(2)
