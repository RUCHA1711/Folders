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

# 3.0 Click on 'Products' button
driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]').click()
time.sleep(1)

# 3.1 Click 'View Product' for any product on home page
driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul').click()
time.sleep(1)

# 3.2 Add products to cart
driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button').click()
time.sleep(2)

# 4. Click 'Cart' button
driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]').click()
time.sleep(1)

# 5. Verify that cart page is displayed
driver.get("https://automationexercise.com/view_cart")

if driver.current_url == "https://automationexercise.com/view_cart":
    print('Cart page is displayed')
else:
    print('Cart page is not displayed')

# 6. Click Proceed To Checkout
driver.find_element(By.XPATH,'//*[@id="do_action"]/div[1]/div/div/a').click()
time.sleep(1)

# 7. Click 'Register / Login' button
driver.find_element(By.XPATH,'//*[@id="checkoutModal"]/div/div/div[2]/p[2]').click()
time.sleep(1)

# 8. Fill all details in Signup and create account
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[2]').click()
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[2]').send_keys('Rucha')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[3]').click()
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys('rucha.t@gmail.com')
time.sleep(1)   

# 8.1 Click 'Signup' button
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/button').click()
time.sleep(1)

# 8.2 Fill details: Title, Password, Date of birth
driver.find_element(By.XPATH,'//*[@id="id_gender2"]').click()
time.sleep(2)

driver.find_element(By.ID,'password').click()
driver.find_element(By.ID,'password').send_keys('Tagline@123')
driver.find_element(By.XPATH,'//*[@id="days"]/option[18]').click()
driver.find_element(By.XPATH,'//*[@id="months"]/option[7]').click()
driver.find_element(By.XPATH,'//*[@id="years"]/option[23]').click()
time.sleep(1)

# 8.3 Select checkbox 'Sign up for our newsletter!'
driver.find_element(By.ID,'newsletter').click()
time.sleep(1)

# 8.4 Select checkbox 'Receive special offers from our partners!'
driver.find_element(By.ID,'optin').click()
time.sleep(1)

# 8.5  First name  
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

# 8.6 Click 'Create Account button'
driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div/div[1]/form/button').click()
time.sleep(1)

# 9. Verify that 'ACCOUNT CREATED!' is visible and Click 'Continue' button
ac_created = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div')
if (ac_created):
    print("'ACCOUNT CREATED!' is visible")
else:
    print("'ACCOUNT CREATED!' is not visible")
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
time.sleep(2)

# 10. Verify that 'Logged in as username' is visible
check = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
if (ac_created):
    print("'Logged in as username' is visible")
else:
    print("'Logged in as username' is not visible")
time.sleep(2)

# 11. Click 'Cart' button
driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]').click()
time.sleep(100)

# 12. Click 'Proceed To Checkout' button
driver.find_element(By.XPATH,'//*[@id="do_action"]/div[1]/div/div/a').click()
time.sleep(100)

# 13. Verify Address Details and Review Your Order
