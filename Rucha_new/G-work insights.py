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

# insights
driver.find_element(By.XPATH,'//*[@id="sidebar"]/ul/li[5]/a/span').click()
time.sleep(2)
# Add insight
# driver.find_element(By.XPATH,'//*[@id="main-body"]/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/ul/li[1]/a').click()
# time.sleep(2)
# # What challenge have you picked up in your Ways of Work?
# driver.find_element(By.XPATH,'//*[@id="title"]').send_keys('Test')
# time.sleep(5)
# # Next button
# driver.find_element(By.XPATH,'//*[@id="patternForm"]/div[1]/div[2]/div/a').click()
# time.sleep(2)
# # What is this obstacle or frustration connected to?
# driver.find_element(By.XPATH,'//*[@id="patternForm"]/div[2]/div[1]/div[2]/ul/li[3]').click()
# time.sleep(2)
# # Next button
# driver.find_element(By.XPATH,'//*[@id="patternForm"]/div[2]/div[2]/div/a').click()
# time.sleep(2)
# #Drop down
# driver.find_element(By.XPATH,'//*[@id="patternForm"]/div[3]/div[1]/span/span[1]/span/span[2]').click()
# time.sleep(2)
# #Select option from drop down
# driver.find_element(By.XPATH,'//*[@id="business_objective"]/option[5]').click()
# time.sleep(2)
# #Explain in your own words the impact: (*optional)
# driver.find_element(By.XPATH,'//*[@id="description"]').send_keys('Test')
# time.sleep(2)
# #Close drop down
# driver.find_element(By.XPATH,'//*[@id="patternForm"]/div[3]/div[1]/span/span[1]/span/span[2]/b').click()
# time.sleep(2)
# # Share button
# driver.find_element(By.XPATH,'//*[@id="patternForm"]/div[3]/div[3]/div').click()
# time.sleep(5)
# # Again share button
# driver.find_element(By.XPATH,'//*[@id="in_submit"]').click()
# time.sleep(2)
#Drag-drop
source=driver.find_element(By.XPATH,'//*[@id="671"]')
destination=driver.find_element(By.XPATH,'//*[@id="tag_dragable_proposed_1"]/img')

actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
time.sleep(2)

