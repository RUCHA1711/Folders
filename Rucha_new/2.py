# import selenium
# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import Select

# from selenium.webdriver.chrome.service import Service
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.get("https://www.flipkart.com/")
# time.sleep(2)

# link = driver.find_elements(By.TAG_NAME, 'a')
# print(len(link))
# return  links

# def print_name_of_links(link):
#     for i in link:
#         link_text=i.text
#         print(link_text)
#         print(i.get_attribute('href')) 

# link=(driver)
# print_name_of_links(link)
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


def count_flipkart_home_page_links(driver):
    driver.get("https://www.flipkart.com/")
    time.sleep(2)

    links = driver.find_elements(By.TAG_NAME, "a")
    print(len(links))

    # Return the links so that we can use it in
    # print_name_of_links function to print the name of the links
    return links


def print_name_of_links(links):
    for i in links:
        link_text = i.text
        print(link_text)
        print(i.get_attribute("href"))


links = count_flipkart_home_page_links(
    driver
)  # Pass the driver object as parameter to the function
print_name_of_links(links)
