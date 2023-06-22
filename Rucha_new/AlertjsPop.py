import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")



driver.find_element(By.NAME,'proceed').click()
time.sleep(3)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
# alert.dismiss()
# alert.send_keys('Hello')
driver.switch_to.default_content()

time.sleep(2)
driver.close()

