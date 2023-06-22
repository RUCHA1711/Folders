import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://demo-store.seleniumacademy.com/")
time.sleep(2)

driver.find_element(
    By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
time.sleep(2)
driver.find_element(
    By.XPATH, '//*[@id="header-account"]/div/ul/li[5]/a').click()
time.sleep(2)
driver.find_element(By.ID, 'firstname').send_keys('Tester')
time.sleep(2)
driver.find_element(By.ID, 'middlename').send_keys('Tagline')
time.sleep(2)
driver.find_element(By.ID, 'lastname').send_keys('Shreya')
time.sleep(2)
driver.find_element(By.ID, 'email_address').send_keys('shreya@yopmail.com')
time.sleep(2)
driver.find_element(By.ID, 'password').send_keys('Tester123')
time.sleep(2)
driver.find_element(By.ID, 'confirmation').send_keys('Tester123')
time.sleep(2)
driver.find_element(
    By.XPATH, '//*[@id="form-validate"]/div[1]/ul/li[4]/label').click()
time.sleep(2)
driver.find_element(
    By.XPATH, '//*[@id="form-validate"]/div[2]/button/span/span').click()
time.sleep(2)
