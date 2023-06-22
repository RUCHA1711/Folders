from selenium import webdriver
from faker import Faker
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Navigate to url
driver.get("https://magento.softwaretestingboard.com/")
time.sleep(1)

fake = Faker()

# Test Cases

# 1. Verify that the user can search for a product and the results are displayed correctly
driver.find_element(By.ID,'search').send_keys('Jackets for women')
driver.find_element(By.ID,'search').send_keys(Keys.ENTER)
time.sleep(2)
result = driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[1]/h1/span')
if(result):
    print('For a searched product the results are displayed correctly.')
else:
    print('Searched product results are incorrect.')
time.sleep(1)

# 2. Verify that the user can add a product to the cart and the products are displayed correctly.
a = ActionChains(driver)
n = driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[3]/div[1]/div[2]/div[2]/ol/li[1]')
a.move_to_element(n).perform()
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[3]/div[1]/div[2]/div[2]/ol/li[1]').click()
time.sleep(3)
# Tshirt size
driver.find_element(By.XPATH,'//*[@id="option-label-size-143-item-168"]').click()
time.sleep(1)
# Tshirt color
driver.find_element(By.XPATH,'//*[@id="option-label-color-93-item-50"]').click()
time.sleep(1)
# Add to cart button
driver.find_element(By.ID,'product-addtocart-button').click()
time.sleep(5)
# Click on add to cart 
driver.find_element(By.XPATH,'/html/body/div[1]/header/div[2]/div[1]').click()
time.sleep(5)
# Verify add to cart product
add_to_cart = driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[1]/div[2]')
if(add_to_cart):
    print('Products are added to cart successfully')
else:
    print('Products are not added to cart successfully')

# 3. Verify that the user can access the cart and the products are displayed correctly
driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[1]/div[2]/div/div/div/a').click()
time.sleep(1)
verify_product=driver.find_element(By.XPATH,'//*[@id="shopping-cart-table"]')
if(verify_product):
      print('Products are dispalyed correctly')
else:
    print('Products are not dispalyed correctly')
time.sleep(3)

# 4. Verify that the user can proceed to checkout and the checkout process is working correctly
driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/ul/li[1]/button').click()
time.sleep(3)
if driver.current_url=="https://magento.softwaretestingboard.com/checkout/#shipping":
    print('Checkout procees is working correctly')
else:
    print('Checkout procees is not working correctly')
time.sleep(5)

# 5. Verify that user can place an order and the order is placed correctly
# 1. Email
email_field= driver.find_element(By.ID,'customer-email')
email_field.send_keys(fake.email())
time.sleep(10)
# 2. First Name
first_name= driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[1]/div/input')
first_name.send_keys(fake.first_name())
time.sleep(3)
# 3. Last Name
last_name= driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[2]/div/input')
last_name.send_keys(fake.last_name())
time.sleep(3)
# 4. Company
company= driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[3]/div/input')
company.send_keys(fake.company())
time.sleep(3)
# 5. Street address
street_address= driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/fieldset/div/div[1]/div/input')
street_address.send_keys(fake.street_address())
time.sleep(3)
# 6. City
city= driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[4]/div/input')
city.send_keys(fake.city())
time.sleep(3)
# 7. State
drop=Select(driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[5]/div/select'))
drop.select_by_value("12")
time.sleep(10)
# 8. Zip code
postal_code=fake.postcode()
postal_code=driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[7]/div/input')
postal_code.send_keys(fake.postalcode())
time.sleep(10)
# 10. Phone no
phone_no= driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[9]/div/input')
phone_no.send_keys(fake.phone_number())
time.sleep(2)
# 11. Shipping
driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[1]/table/tbody/tr[1]/td[1]/input').click()
time.sleep(2)
# 12.Next button
driver.find_element(By.XPATH,'//*[@id="shipping-method-buttons-container"]/div/button/span').click()
time.sleep(5)

# 6. Verify that the user can place order and the order is placed correctly
if driver.current_url=="https://magento.softwaretestingboard.com/checkout/#payment":
    print('Order is placed successfully')
else:
    print('Order is not placed successfully')
time.sleep(50)

# 7. Verify that the user can view their order history and the order details are displayed correctly
driver.find_element(By.XPATH,'//*[@id="opc-sidebar"]/div[1]/div/div[1]').click()
time.sleep(2)
# driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div/div[2]/aside/div[2]/div/div/div[1]/div/div[2]/div')
# time.sleep(2)
