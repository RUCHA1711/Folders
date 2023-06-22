import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# Navigate to Snapdeal site
driver.get("http://www.snapdeal.com")
time.sleep(2)

# Move to Sign in button and hold
sign_ele = driver.find_element(
    By.XPATH, '//*[@id="sdHeader"]/div[4]/div[2]/div/div[3]/div[3]/div/span[1]')
act_chains = ActionChains(driver)
act_chains.move_to_element(sign_ele).perform()
time.sleep(3)

# Move to Sign in button and click
driver.find_element(
    By.XPATH, '//*[@id="sdHeader"]/div[4]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/span[2]/a').click()
time.sleep(2)

# driver.find_element(By.XPATH,'/html/body/div/div/div/div[6]/form/div/input').send_keys('rucha.tagline@gmail.com')
# time.sleep(2)

# Enter valid Email Id and click continue
driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div/div/div/div[6]/form/div/input"))
).send_keys('rucha.tagline@gmail.com')

driver.find_element(By.ID, 'checkUser').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="j_number"]').send_keys('9662331425')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="j_name"]').send_keys('Rucha')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="j_password"]').send_keys('Tagline@123')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="userSignup"]').click()
time.sleep(2)

# Verify that the user is logged in successfully.
driver.get("https://www.snapdeal.com/login")

if driver.current_url == "https://www.snapdeal.com/login":
    print('user is logged in successfully.')
else:
    print('user is not logged in successfully.')
