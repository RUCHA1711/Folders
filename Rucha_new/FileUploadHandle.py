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
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

driver.find_element(By.NAME,'upfile').send_keys('Documents/Rucha/sel.py')


time.sleep(10)
driver.quit