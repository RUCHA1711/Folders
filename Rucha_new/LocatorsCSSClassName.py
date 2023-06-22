import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")

# driver.find_element(By.CSS_SELECTOR,'#username').send_keys('rucha.tagline@gmail.com')
# driver.find_element(By.CLASS_NAME,'login-email').send_keys('rucha.tagline@gmail.com')
# driver.find_element(By.CLASS_NAME,'login-password').send_keys('Test@1234')
# driver.find_element(By.CLASS_NAME,'login-submit').click()

# driver.find_element(By.CSS_SELECTOR,'input.form-control.private-form__control.login-email').send_keys('rucha.tagline@gmail.com')
# driver.find_element(By.XPATH,"//input[@class='form-control.private-form__control.login-email']").send_keys('rucha.tagline@gmail.com')
# driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/form/div[3]/div/div/div[2]/input').send_keys('rucha.tagline@gmail.com')

# driver.find_element(By.LINK_TEXT,'Sign up').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Sign').click()

# form-control private-form__control login-email
# form-control private-form__control login-password m-bottom-3 
# class="uiButton private-button private-button--primary private-button--default m-bottom-4 login-submit disabled private-button--disabled private-button--non-link"

time.sleep(3)



