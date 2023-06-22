from re import S
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service
options=webdriver.ChromeOptions()
options.headless=True
driver = webdriver.Chrome(ChromeDriverManager().install(),options= options)
driver.implicitly_wait(10)
driver.get("https://www.reddit.com/")
# driver.get_screenshot_as_file('reddit 1.png')

S=lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_full_1.png')