
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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1.Goto url
driver.get("http://live.techpanda.org/")
time.sleep(2)

# 2.Click on account link
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[3]/div/div[4]/ul/li[1]/a').click()
time.sleep(2)

# 3.Login in application using previously created credential
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys('shreya.tagline@gmail.com')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys('Tester123')
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="send2"]').click()

# 4.Click on My wishlist link
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[1]/div/div[2]/ul/li[8]/a').click()
time.sleep(2)

# 5.Click add to cart
driver.find_element(By.XPATH,'//*[@id="item_58663"]/td[5]/div/button').click()
time.sleep(2)

# 6.Click proceed to checkout
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div/div/div[1]/ul/li/button/span/span').click()
time.sleep(2)

# 7.Enter shipping information
driver.find_element(By.ID,'billing:company').send_keys('Tagline')
time.sleep(2)

driver.find_element(By.ID,'billing:street1').send_keys('abc')
time.sleep(2)

driver.find_element(By.ID,'billing:city').send_keys('New York')
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="billing:region_id"]/option[44]').click()
time.sleep(2)

driver.find_element(By.ID,'billing:postcode').send_keys('542896')
time.sleep(2)

driver.find_element(By.ID,'billing:telephone').send_keys('12345678')
time.sleep(2)

# 8.Click continue button
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/ol/li[1]/div[2]/form/div/div/button').click()
time.sleep(2)

# 9.Verify shipping cost generated
shipping_cost=driver.find_element(By.XPATH,'//*[@id="checkout-shipping-method-load"]/dl/dd/ul/li/label/span')

if(shipping_cost):
    print('Flat rate shipping of $10 is generated')
else:
    print('Fail')

driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/ol/li[3]/div[2]/form/div[3]/button').click()
time.sleep(2)

# 10.In Payment information select 'Checkout/Money order' radio button.Click continue
driver.find_element(By.XPATH,'//*[@id="p_method_checkmo"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/ol/li[4]/div[2]/div[2]/button').click()
time.sleep(2)

# 11.Click place order
driver.find_element(By.XPATH,'//*[@id="review-buttons-container"]/button').click()
time.sleep(2)

# 12.Verify order is generated
order=driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div/p[1]')

if(order):
    print('Order is placed')
else:
    print('Order is not placed.')

time.sleep(2)