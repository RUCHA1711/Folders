from curses import window
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://login.gwork.io/")
driver.maximize_window()


# driver.set_window_size(1024, 600)
# driver.maximize_window()


driver.find_element(By.ID, 'gdpr-cookie-accept').click()
driver.find_element(By.CLASS_NAME, 'reset-password').click()
driver.find_element(By.ID, 'identity').send_keys("rucha.tagline@gmail.com")
driver.find_element(By.CLASS_NAME, 'login-btn').click()

print (driver.title)
time.sleep(20)
driver.quit()