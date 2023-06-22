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

# 1. Navigate to url
driver.get("https://automationexercise.com/")
time.sleep(1)

# 2. Verify that home page is visible successfully
driver.get("https://automationexercise.com/")

if driver.current_url == "https://automationexercise.com/":
    print('Home page is visible successfully.')
else:
    print('Home page is not visible successfully')

# 3. Click on 'Signup / Login' button
driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a/i').click()
time.sleep(1)

# 4. Verify 'New User Signup!' is visible
form=driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div')

if(form):
    print('New User Signup is visible')
else:
    print('New User Signup is visible')

# 5. Enter name and email address
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[2]').click()
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys('Rucha')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[3]').click()
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys('rucha.tag@gmail.com')
time.sleep(1)   

# 6. Click 'Signup' button
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/button').click()
time.sleep(1)

# 7. Verify that 'ENTER ACCOUNT INFORMATION' is visible
account_information=driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div/div[1]')

if(account_information):
    print('Account information is visible')
else:
    print('Account information is not visible')
time.sleep(2)

# 8. Fill details: Title, Password, Date of birth
driver.find_element(By.XPATH,'//*[@id="id_gender2"]').click()
time.sleep(2)

driver.find_element(By.ID,'password').click()
driver.find_element(By.ID,'password').send_keys('Tagline@123')
driver.find_element(By.XPATH,'//*[@id="days"]/option[18]').click()
driver.find_element(By.XPATH,'//*[@id="months"]/option[7]').click()
driver.find_element(By.XPATH,'//*[@id="years"]/option[23]').click()
time.sleep(1)

# 9. Select checkbox 'Sign up for our newsletter!'
driver.find_element(By.ID,'newsletter').click()
time.sleep(1)

# 10. Select checkbox 'Receive special offers from our partners!'
driver.find_element(By.ID,'optin').click()
time.sleep(1)

# 11.  First name  
driver.find_element(By.XPATH,'//*[@id="first_name"]').click()
driver.find_element(By.XPATH,'//*[@id="first_name"]').send_keys('Rucha')
time.sleep(1)
# Last name
driver.find_element(By.ID,'last_name').click()
driver.find_element(By.ID,'last_name').send_keys('Tester')
time.sleep(1)
# Company
driver.find_element(By.ID,'company').click()
driver.find_element(By.ID,'company').send_keys('Tagline')
time.sleep(1)
# Address
driver.find_element(By.ID,'address1').click()
driver.find_element(By.ID,'address1').send_keys('Apple Square')
time.sleep(1)
# Country
driver.find_element(By.XPATH,'//*[@id="country"]/option[1]').click()
time.sleep(1)
# State
driver.find_element(By.ID,'state').click()
driver.find_element(By.ID,'state').send_keys('Gujarat')
# City
driver.find_element(By.ID,'city').click()
driver.find_element(By.ID,'city').send_keys('surat')
# Zipcode
driver.find_element(By.ID,'zipcode').click()
driver.find_element(By.ID,'zipcode').send_keys('394180')
time.sleep(1)
# Mobile number
driver.find_element(By.ID,'mobile_number').click()
driver.find_element(By.ID,'mobile_number').send_keys('9214282525')

# 13. Click 'Create Account button'
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div/div[1]/form/button').click()
time.sleep(1)

# 14. Verify that 'ACCOUNT CREATED!' is visible
ac_created = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div')
if (ac_created):
    print("'ACCOUNT CREATED!' is visible")
else:
    print("'ACCOUNT CREATED!' is not visible")
time.sleep(2)

# 15. Click 'Continue' button
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
time.sleep(2)

# 16. Verify that 'Logged in as username' is visible
check = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
if (ac_created):
    print("'Logged in as username' is visible")
else:
    print("'Logged in as username' is not visible")
time.sleep(2)

# 17. Click 'Delete Account' button
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a').click()
time.sleep(2)

# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
deleted = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2')
if (deleted):
    print("'ACCOUNT DELETED!' is visible")
else:
    print("'ACCOUNT DELETED!' is not visible")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
time.sleep(2)

driver.quit()
