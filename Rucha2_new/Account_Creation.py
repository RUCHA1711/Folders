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
driver.get("http://live.techpanda.org/index.php/customer/account/login/")
time.sleep(2)

# 2.Click on create account button
driver.find_element(By.XPATH,'//*[@id="login-form"]/div/div[1]/div[2]/a/span/span').click()
time.sleep(2)

# 3.Fill new user details 
driver.find_element(By.ID,'firstname').send_keys('Tester')
time.sleep(2)

driver.find_element(By.ID,'middlename').send_keys('Tagline')
time.sleep(2)

driver.find_element(By.ID,'lastname').send_keys('Tagline')
time.sleep(2)

driver.find_element(By.ID,'email_address').send_keys('rucha12yop@gmail.com')
time.sleep(2)

driver.find_element(By.ID,'password').send_keys('Tester123')
time.sleep(2)

driver.find_element(By.ID,'confirmation').send_keys('Tester123')
time.sleep(2)

# 5.Click on Register
driver.find_element(By.XPATH,'//*[@id="form-validate"]/div[2]/button').click()
time.sleep(2)

# 6.Verify Registration is done
verify=driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div/div/ul/li/ul/li/span')
time.sleep(2)

if(verify):
    print('Registration is done')
else:
    print('Registration is not done')

# 7.Goto TV menu
driver.find_element(By.XPATH,'//*[@id="nav"]/ol/li[2]/a').click()
time.sleep(2)

# 8.Add product to your wishlist
driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[1]/div/div[3]/ul/li[1]/a').click()
time.sleep(2)

# 9.Click on sharelist
driver.find_element(By.XPATH,'//*[@id="wishlist-view-form"]/div/div/button[1]/span/span').click()
time.sleep(2)

# 10.In next page enter Email and a message and click share wishlist
driver.find_element(By.ID,'email_address').send_keys('rucha.tagline@gmail.com')
time.sleep(2)

driver.find_element(By.ID,'message').send_keys('Hello')
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="form-validate"]/div[2]/button/span/span').click()
time.sleep(2)

# 11.Check wishlist is shared
wishlist=driver.find_element(By.XPATH,'//*[@id="top"]/body/div/div/div[2]/div/div[2]/div/div[1]/ul/li/ul')

if(wishlist):
    print('Wishlist shared successfully')
else:
    print('Wishlist is not shared successfully')