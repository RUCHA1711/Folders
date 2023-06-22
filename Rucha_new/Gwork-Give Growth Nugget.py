import time
from select import select
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://login-staging.gwork.io/")

# Login
driver.find_element(By.ID, "identity").send_keys("sandy@gmail.com")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "gdpr-cookie-accept").click()
driver.find_element(By.CLASS_NAME, "login-btn").click()
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="sidebar"]/ul/li[4]/a/span').click()
time.sleep(1)
# Click on give growth nugget
driver.find_element(By.XPATH,'//*[@id="main-body"]/div[1]/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/a').click()
time.sleep(3)
# Click on add user
driver.find_element(By.XPATH,'//*[@id="select_user"]').click()
time.sleep(1)
# Select user
driver.find_element(By.XPATH,'//*[@id="learning-nugget"]/div/div[1]/div/div/div/div[2]/ul/li[4]/a/div/div/p').click()
time.sleep(1)
# Key-behavior
driver.find_element(By.XPATH,'//*[@id="title"]').send_keys("TEST")
time.sleep(1)
# Drop-down list
driver.find_element(By.XPATH,'//*[@id="learning-nugget"]/div/div[2]/div[2]/div[2]/div/div/span/span[1]/span/ul/li/input').click()
time.sleep(1)
# selection from drop-down
driver.find_element(By.XPATH,'//*[@id="learning-nugget"]/div/div[2]/div[2]/div[2]/div/div/select/option[4]').click()
time.sleep(2)
#Close drop-down
driver.find_element(By.XPATH,'//*[@id="learning-nugget"]/div/div[2]/div[2]/div[2]/div/div/span/span[1]/span/ul').click()
time.sleep(2)
# Action
driver.find_element(By.XPATH,'//*[@id="description"]').send_keys("TESTING")
time.sleep(2)
# submit button
driver.find_element(By.XPATH,'//*[@id="btn_submit"]').click()
time.sleep(2)
# Feedback
driver.find_element(By.XPATH,'//*[@id="vetting-form"]/table/tbody/tr[1]/td[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="vetting-form"]/table/tbody/tr[2]/td[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="vetting-form"]/table/tbody/tr[3]/td[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="vetting-form"]/button').click()
time.sleep(2)
# My prioritized feedback
# WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="heading-4"]/div/div[2]/a'))).click()
driver.find_element(By.XPATH, '//*[@id="heading-4"]/div/div[2]/a').click()
time.sleep(20)
source = driver.find_element(By.XPATH,'//*[@id="title558"]')
destination = driver.find_element(By.XPATH,'//*[@id="main-body"]/div[1]/div/div/div/div[1]/div/div[3]')

actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
time.sleep(3)
# Feedback I have mastered 
source = driver.find_element(By.XPATH,'//*[@id="title558"]')
destination = driver.find_element(By.XPATH,'//*[@id="main-body"]/div[1]/div/div/div/div[1]/div/div[4]')

actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
time.sleep(10)