import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.youtube.com/")


searchbox=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
searchbox.send_keys('Automation Testing')
searchButton=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')
searchButton.click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="video-title"]/yt-formatted-string').click()
time.sleep(3)

# Likes
total_likes=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[5]/div[1]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-formatted-string')
time.sleep(1)
print(total_likes.text)

#Views
total_views=driver.find_element(By.XPATH,'//*[@id="count"]/ytd-video-view-count-renderer/span[1]')
time.sleep(1)
print(total_views.text)

# #Comments
# total_comments=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[1]/h2')
# print(total_comments.text)
# time.sleep(10)

# # Channel name
# channel_name=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[7]/div[2]/div[2]/ytd-video-secondary-info-renderer/div/div/ytd-video-owner-renderer/div[1]/ytd-channel-name')
# print(channel_name.text)
# time.sleep(2)

#subscribers
total_subscribers=driver.find_element(By.ID,'owner-sub-count')
print(total_subscribers.text)
time.sleep(10)


