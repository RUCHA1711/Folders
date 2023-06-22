import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.amazon.com/")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="searchDropdownBox"]').click()
time.sleep(2)


def select_Amazon_Fashion_from_dropdown():
    driver.find_element(
        By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select/option[28]').click()
    time.sleep(2)

# Sena par click akravanu che batavmy orders
# Side valu my orders?yes

select_Amazon_Fashion_from_dropdown()


def watch():
    driver.find_element(
        By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('watch')
    time.sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys(Keys.ENTER)
    time.sleep(2)


watch()


def print_productnames():
    # Tu ahiya find_element lakhti hati, 's' lagavanu bhuli gayeli
    time.sleep(2)
    products = driver.find_elements(By.TAG_NAME, "h2")
    for product in products:
        print(product.text)


print_productnames()

"""
a-size-mini a-spacing-none a-color-base s-line-clamp-4
a-size-mini a-spacing-none a-color-base s-line-clamp-4
a-size-mini a-spacing-none a-color-base s-line-clamp-4

"""
