import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# assign URL
# First Yahho.com na url p[ar aavyu]
# driver.get("https://login.yahoo.com/")
# print("First window title = " + driver.title)
# time.sleep(3)
# # switch to new window
# # Privacy value page new tab ma khulse
# driver.find_element_by_class_name("privacy").click()
# print(driver.window_handles)
# time.sleep(3)
# # Aapde je privacy value page kholyu hatu te window_handles[1] 
# # ma store hati. 0 = Yahoo ni window, 1 = privacy page.
# # Etle aapde nava window ma redirect thaya.
# driver.switch_to.window(driver.window_handles[1])
# print("Second window title = " + driver.title)
# time.sleep(3)

# # switch to new window
# driver.execute_script("window.open()")
# print(driver.window_handles)
# # Ahiya 2 no meaning ke haju ek window kholo browser ma 
# # and ema geeks for geeks ni website open kari.
# # 0 = Yahoo ni window, 
# # 1 = privacy page.
# # 2 = Geeks For Geeks 
# driver.switch_to.window(driver.window_handles[2])
# time.sleep(3)
# driver.get("https://www.geeksforgeeks.org/")
# print(driver.title)
# time.sleep(10)

# Open login yahoo for sample url
driver.get("https://login.yahoo.com/")

# print title of yahoo window
print("First window title = " + driver.title)

# Clicks on privacy and it opens in new window
driver.find_element_by_class_name("privacy").click()

# switch window in 7 seconds
time.sleep(7)

# window_handles[1] is a second window
driver.switch_to.window(driver.window_handles[1])

# prints the title of the second window
print("Second window title = " + driver.title)

# window_handles[0] is a first window
driver.switch_to.window(driver.window_handles[0])

# prints windows id
print(driver.window_handles)

