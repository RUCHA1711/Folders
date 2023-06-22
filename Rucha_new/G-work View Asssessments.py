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

# View Assessments
driver.find_element(By.XPATH,'//*[@id="pills-second"]/div/div[2]/div[2]/div/div[3]/div[2]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="main-body"]/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div[4]/div/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="sub_assessment_div"]/div[2]/div[3]/div/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="mainDiv"]/div[1]/div/div/span/span[1]/span/span[2]').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "select2-selection__rendered ").click()
time.sleep(2)

ids = ['//*[@id="26"]', '//*[@id="27"]', '//*[@id="28"]', '//*[@id="29"]', '//*[@id="30"]']
for id in ids:
   select = Select(driver.find_element(By.XPATH, id))
#     # select by visible text
   select.select_by_visible_text("Average")
   time.sleep(2)