import selenium
import time
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# browserName= "chrome"

if browserName == "chrome" :
   driver = webdriver.Chrome(ChromeDriverManager().install())
# elif browserName == "firefox" :
#     driver = webdriver.Firefox(executable_path=GeckoDriverManager.install)
# elif browserName == "safari" :
#     driver = webdriver.Safari()
# else:
#     print('please pass the correct browser name :'+ browserName)

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, 'username').send_keys("rucha.tagline@gmail.com")
driver.find_element(By.ID, 'password').send_keys("Test@1234")
driver.find_element(By.ID, 'loginbtn').click()

print (driver.title)
time.sleep(4)
driver.quit()