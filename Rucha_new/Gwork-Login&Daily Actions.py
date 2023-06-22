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

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://login-staging.gwork.io/")

# Login
driver.find_element(By.ID, "identity").send_keys("sandy@gmail.com")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "gdpr-cookie-accept").click()
driver.find_element(By.CLASS_NAME, "login-btn").click()
time.sleep(1)



# Assesments Result
driver.find_element_by_id("base_line").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='baseline_modal']/div/div/div[1]/button").click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="graph_type"]/option[2]').click()
time.sleep(4)
# Daily Actions
driver.find_element_by_id("pills-first-tab").click()
time.sleep(2)
# My pulse
driver.find_element(By.XPATH,'//*[@id="smiley_pulse"]/div[3]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="pulsecomment"]').send_keys("Test")
time.sleep(2)
 # Next button
driver.find_element(By.XPATH,'//*[@id="pills-first"]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/a').click()
time.sleep(2)
# Applause
driver.find_element(By.XPATH,'//*[@id="circle16"]/div').click()
time.sleep(2)
for _ in range(4):
    driver.find_element(By.XPATH,'//*[@id="give_applause_body"]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[2]/i').click()
    time.sleep(1)
    try:
        driver.find_element(By.ID,'30').click()
        time.sleep(2)
        break
    except: pass
# Comment
driver.find_element(By.ID,'comment_text_area').send_keys('Great work')
time.sleep(2)
# Give Applause  button
driver.find_element(By.XPATH,'//*[@id="give_applause_body"]/div/div[2]/div/div/button').click()
time.sleep(4)
print(driver.title)





