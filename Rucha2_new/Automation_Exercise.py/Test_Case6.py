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

# 3. Click on 'Contact Us' button
driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]').click()
time.sleep(1)

# 4. Verify 'GET IN TOUCH' is visible
Get_In_Touch=driver.find_element(By.XPATH,'//*[@id="contact-page"]/div[2]/div[1]/div')

if(Get_In_Touch):
    print('GET IN TOUCH is visible')
else:
    print('GET IN TOUCH is not visible')
time.sleep(1)

# 5. Enter name
driver.find_element(By.XPATH,'//*[@id="contact-us-form"]/div[1]/input').click()
driver.find_element(By.XPATH,'//*[@id="contact-us-form"]/div[1]/input').send_keys('Rucha')
time.sleep(1)

# email
driver.find_element(By.XPATH,'//*[@id="contact-us-form"]/div[2]/input').click()
driver.find_element(By.XPATH,'//*[@id="contact-us-form"]/div[2]/input').send_keys('rucha.tagline@gmail.com')
time.sleep(1)

# subject
driver.find_element(By.XPATH,'//*[@id="contact-us-form"]/div[3]/input').click()
driver.find_element(By.XPATH,'//*[@id="contact-us-form"]/div[3]/input').send_keys('Testing')
time.sleep(1)

# message
driver.find_element(By.XPATH,'//*[@id="message"]').click()
driver.find_element(By.XPATH,'//*[@id="message"]').send_keys('Hello Tester')
time.sleep(1)

# 6. Upload file and click submit button
ele=driver.find_element(By.XPATH,'//*[@id="contact-us-form"]/div[5]/input')
ele.send_keys('/Users/tagline_145/Downloads/rucha.jpeg')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="contact-us-form"]/div[6]/input').click()
time.sleep(1)

# 7. Click OK button
alert=driver.switch_to.alert
alert.accept()


# 8. Verify success message 'Success! Your details have been submitted successfully.' is visible
 
success_msg=driver.find_element(By.XPATH,'//*[@id="contact-page"]/div[2]/div[1]/div/div[2]')

if(success_msg):
    print('Success! Your details have been submitted successfully.')
else:
    print('Your details have not been submitted successfully.')

# 9. Click 'Home' button and verify that landed to home page successfully

driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[1]').click()
driver.get("https://automationexercise.com/")

if driver.current_url == "https://automationexercise.com/":
    print('Home page is visible successfully.')
else:
    print('Home page is not visible successfully')
