import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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

# 3. Click on 'Products' button
driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]').click()
time.sleep(1)
driver.execute_script('window.scrollBy(0,1000)')
time.sleep(1)


# 4. Hover over first product and click 'Add to cart'
a = ActionChains(driver)
r=driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]')
a.move_to_element(r).perform()
time.sleep(5)
a.send_keys(Keys.END)
time.sleep(5)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/main/div[2]/div[2]/div[1]/button"))).click()
wait=WebDriverWait(driver, 20)
a=wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a"))).click()
# driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a').click()

# # 5. Click 'Continue Shopping' button
# driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[3]/button').click()
# time.sleep(1)

# # 6. Hover over second product and click 'Add to cart'
# a = ActionChains(driver)
# r=driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[3]/div')
# a.move_to_element(r).perform()
# time.sleep(2)

# driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a').click()
# time.sleep(2)
# # 7. Click 'View Cart' button
# driver.find_element(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]/a').click()
# time.sleep(100)

# 8. Verify both products are added to Cart
# driver.find_element(By.XPATH,'')
