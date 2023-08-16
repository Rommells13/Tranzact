from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Open the Home page
    driver.get("https://demo.evershop.io/")

    # Click Sign in button
    login_button = driver.find_element(By.CSS_SELECTOR, ".icon-wrapper .self-center:nth-child(3) a")
    login_button.click()
    create_account_button = driver.find_element(By.LINK_TEXT, "Create an account")
    create_account_button.click()

    # Fill Email address and Password to create an account
    fullName_field = driver.find_element(By.NAME, "full_name")
    fullName_field.send_keys("Full Name")
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("email111@example.com")
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("password")

    # Click Create an account
    sign_button = driver.find_element(By.CSS_SELECTOR, ".button")
    sign_button.click()

    # Log in
    login_button.click()
    email_field.send_keys("email111@example.com")
    password_field.send_keys("password")
    sign_button.click()

    # Select and add products to cart
    product1_button = driver.find_element(By.CSS_SELECTOR, ".page-width div.grid-cols-2 :nth-child(1) .product-name a")
    product1_button.click()
    quantity_field = driver.find_element(By.CSS_SELECTOR, "div.field-wrapper")
    quantity_field.send_keys("1")
    variant1_button = driver.find_element(By.CSS_SELECTOR, ".mt-2 div:nth-child(1) ul li:nth-child(1) a")
    variant1_button.click()
    variant2_button = driver.find_element(By.CSS_SELECTOR, ".mt-2 div:nth-child(2) ul li:nth-child(1) a")
    variant2_button.click()
    sign_button.click()
    home_button = driver.find_element(By.CLASS_NAME, "logo-icon")
    home_button.click()
    product2_button = driver.find_element(By.CSS_SELECTOR, ".page-width div.grid-cols-2 :nth-child(2) .product-name a")
    product2_button.click()
    quantity_field.send_keys("2")
    variant1_button.click()
    variant2_button.click()
    sign_button.click()
    home_button.click()
    product3_button = driver.find_element(By.CSS_SELECTOR, ".page-width div.grid-cols-2 :nth-child(3) .product-name a")
    product3_button.click()
    quantity_field.send_keys("3")
    variant1_button.click()
    variant2_button.click()
    sign_button.click()

    # Go to Checkout page and click on Checkout
    cart_button = driver.find_element(By.CSS_SELECTOR, ".icon-wrapper .self-center:nth-child(2) a")
    cart_button.click()
    checkout_button = driver.find_element(By.CSS_SELECTOR, ".mt-2 a")
    checkout_button.click()

    # Fill shipping address and submit
    fullName_shipping_field = driver.find_element(By.NAME, "address[full_name]")
    fullName_shipping_field.send_keys("Full Name")
    telephone_shipping_field = driver.find_element(By.NAME, "address[telephone]")
    telephone_shipping_field.send_keys("999999999")
    address_shipping_field = driver.find_element(By.NAME, "address[address_1]")
    address_shipping_field.send_keys("Example St.")
    city_shipping_field = driver.find_element(By.NAME, "address[city]")
    city_shipping_field.send_keys("Example")
    country_shipping_list = driver.find_element(By.NAME, "address[country]")
    country_shipping_list.click()
    country1_option = driver.find_element(By.CSS_SELECTOR, "#address\[country\] option:nth-child(6)")
    country1_option.click()
    province_shipping_list = driver.find_element(By.NAME, "address[province]")
    province_shipping_list.click()
    province1_option = driver.find_element(By.CSS_SELECTOR, "#address\[province\] option:nth-child(2)")
    province1_option.click()
    postcode_shipping_field = driver.find_element(By.NAME, "address[postcode]")
    postcode_shipping_field.send_keys("11111")
    shippingMethod_option = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > label span.radio-unchecked")
    shippingMethod_option.click()
    sign_button.click()

    # Click on success to get correct card information
    paymentMethod_option = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div > div > div > div.flex.justify-start.items-center.gap-1 a svg")
    paymentMethod_option.click()

    # Click Place Order
    sign_button.click()

    # Close the browser
    driver.quit()

except Exception as e:
    print("An error occurred:", e)
    driver.quit()