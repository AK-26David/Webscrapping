from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
# Open the URL
url = "https://www.upl-ltd.com/es/Productos"
driver.get(url)

# Extract product categories
categories = driver.find_elements(By.CSS_SELECTOR, "from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
# Open the URL
url = "https://www.upl-ltd.com/es/Productos"
driver.get(url)

# Extract product categories
categories = driver.find_elements(By.CSS_SELECTOR, "#product-accordion > div:nth-child(1) > div.panel-heading.products-heading.ia-inpagenav.collapsed > div > div > div > h2 > span:nth-child(2)")

# Loop through categories and extract product details
for category in categories:
    category_name = category.text
    category.click()
    time.sleep(10)  # Adjust sleep time for the page to load
   
    products = driver.find_elements(By.CSS_SELECTOR, "div.product-name")
    for product in products:
        product_name = product.find_element(By.CSS_SELECTOR, "div.product-name").text
        active_ingredient = product.find_element(By.CSS_SELECTOR, "span.product-ingrd").text
        print(f"Category: {category_name}, Product: {product_name}, Active Ingredient: {active_ingredient}")
   
    driver.back()
    time.sleep(10)  # Adjust sleep time for the page to load

# Close the driver
driver.quit()")

# Loop through categories and extract product details
for category in categories:
    category_name = category.text
    category.click()
    time.sleep(10)  # Adjust sleep time for the page to load
   
    products = driver.find_elements(By.CSS_SELECTOR, "div.product-name")
    for product in products:
        product_name = product.find_element(By.CSS_SELECTOR, "div.product-name").text
        active_ingredient = product.find_element(By.CSS_SELECTOR, "span.product-ingrd").text
        print(f"Category: {category_name}, Product: {product_name}, Active Ingredient: {active_ingredient}")
   
    driver.back()
    time.sleep(10)  # Adjust sleep time for the page to load

# Close the driver
driver.quit()