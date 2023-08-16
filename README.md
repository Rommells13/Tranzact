Tranzact

# Automated Test Cases using Selenium WebDriver and API Testing

This repository contains automated test scripts for both UI (using Selenium WebDriver) and API testing scenarios. It covers the "Sign In" test case and API tests for a web application.

## Pre-requisites

1. Python 3.x installed on your system.
2. PyCharm or any other Python IDE of your choice.
3. Chrome WebDriver installed (compatible with your Chrome browser version).
4. API key obtained from [CountryLayer](https://countrylayer.com/documentation).

## UI Test Scenario - Sign In

### Pre-requisites

- Generated customer with all customer data.

### Test Steps

1. Open [Home page](https://demo.evershop.io/)
2. Click *Sign in* button
3. Fill *Email address* and *Password* to create an account
4. Click *Create an account*
5. Log in
6. Select 3 different products and add them to the cart with different quantities
7. Go to the Checkout page and click on Checkout
8. Fill the shipping address and submit
9. Click on success to get correct card information
10. Fill payment information
11. Click Place Order

### Assertions

- Verify Order created successfully with the correct information: Contact, Payment, Shipping Address, Billing Address, and Items.

## API Test Scenarios

### Pre-requisites

- API key obtained from [CountryLayer](https://countrylayer.com/documentation).

### Test Scenarios

1. **Get Information for Individual Countries**

   - Get information for country "US" and validate the response
   - Get information for country "DE" and validate the response
   - Get information for country "GB" and validate the response

2. **Get Information for Inexistent Countries**

   - Try to get information for inexistent countries and validate the response (e.g., "XYZ")

3. **Validate New Country Addition Using POST (Future Development)**

   - Although the API does not currently support POST, a test template is provided for future development.
   - Example JSON body for POST:

     ```json
     {
        "name": "Test Country",
        "alpha2_code": "TC",
        "alpha3_code": "TCY"
     }
     ```

   - The test template includes response code validation.

## Note

- These test scripts serve as templates and should be customized according to the specific web application and test case requirements.
- Make sure to update locators, interactions, and assertions as per the actual web application's structure and API responses.

## Authors

Rommel Lopez

## License

This project is licensed under the [MIT License](LICENSE).
