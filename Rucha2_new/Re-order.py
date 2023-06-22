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

# 2.Click on My account link
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[3]/div/div[4]/ul/li[1]/a').click()
time.sleep(2)

# 3.Login in application using previously created credential
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys('shreya.tagline@gmail.com')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys('Tester123')

driver.find_element(By.XPATH, '//*[@id="send2"]').click()
time.sleep(2)

# 4.Click on 'Reorder' link, change QTY & click update
driver.find_element(By.XPATH,'//*[@id="my-orders-table"]/tbody/tr[2]/td[6]').click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="shopping-cart-table"]/tbody/tr/td[4]/input').click()
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/form/table/tbody/tr/td[4]/input').send_keys('1')
time.sleep(2)
# driver.find_element(By.XPATH,'//*[@id="shopping-cart-table"]/tbody/tr/td[4]/button').click()
time.sleep(2)

# 5.Verify Grand Total is changed
grand_total=driver.find_element(By.XPATH,'//*[@id="shopping-cart-totals-table"]/tfoot/tr')

if(grand_total):
    print('Grand total is changed')
else:
    print('Grand total is not changed')

driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div/div/div[3]/div/ul/li[1]/button').click()
time.sleep(2)

# 6.Complete Billing & Shipping Information
driver.find_element(By.XPATH,'//*[@id="billing-buttons-container"]/button').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="shipping-method-buttons-container"]/button').click()
time.sleep(2)


driver.find_element(By.XPATH,'//*[@id="p_method_checkmo"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/ol/li[4]/div[2]/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="review-buttons-container"]/button').click()
time.sleep(2)

# 7.Verify order is generated and note the number
order=driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div/p[1]')

if(order):
    print('Order number is generated')
else:
    print('order number is not generated')
time.sleep(2)