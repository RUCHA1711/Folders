from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
y = driver.get('https://www.google.com')

query = driver.find_element(By.NAME, "q").send_keys("Jay Shree Ram")
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()

print(query)
time.sleep(10)