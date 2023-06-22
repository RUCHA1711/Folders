import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("http://www.google.com")

driver.find_element(By.NAME,'q').send_keys("pizza ")
# optionList=driver.find_elements(By.CSS.SELECTOR, )

print(len(optionList))

for ele in optionList:
     print(ele.text)

print(driver.title)


time.sleep(5)
driver.quit()