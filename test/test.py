# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import os
# from dotenv import load_dotenv
# import time
# import getpass

# username = input("Enter username: ") #username is generally your student ID
# password = getpass.getpass('Enter Password:')

# canvas_url = input("Enter Canvas URL: ") # Canvas URL is the URL of your university's canvas page

# # Set up Chrome WebDriver
# chromedriver_location = os.getenv("CHROMEDRIVER_LOCATION")  # Set the location of the chromedriver
# service = Service(chromedriver_location) # Set the service to the chromedriver location
# chrome_options = Options() # Set the chrome options
# # chrome_options.add_argument("--headless") # Uncomment to run the browser in headless mode
# driver = webdriver.Chrome(service=service, options=chrome_options) # Set the driver to the chromedriver service and options
# driver.implicitly_wait(5)  # Apply implicit wait globally

# driver.get(canvas_url)
# print("Opened Canvas")
 
# username_input = driver.find_element(By.ID, "emailAuthCheck")
# next_button = driver.find_element(By.CLASS_NAME, "uon-emailAuthCheckAction")
# username_input.send_keys(username)
# next_button.click()

# # Wait for the page to load
# time.sleep(5)
# username_input = driver.find_element(By.ID, "input28") # The ID of the username input field
# password_input = driver.find_element(By.ID, "input36") # The ID of the password input field
# signin_button = driver.find_element(By.CSS_SELECTOR, "input.button.button-primary[value='Sign in']") # The CSS selector of the sign in button
# username_input.send_keys(username) # Send the username to the username input field
# password_input.send_keys(password) # Send the password to the password input field
# signin_button.click()

# authenticator_code = input("Enter the authenticator code: ")
# authenticator_input = driver.find_element(By.ID, "input69") # The ID of the authenticator input field
# authenticator_input.send_keys(authenticator_code) # Send the authenticator code to the authenticator input field
# signin_button = driver.find_element(By.CSS_SELECTOR, "input.button.button-primary[value='Verify']")
# signin_button.click()

# time.sleep(10)
# print("Logged in")
# driver.quit()

# ********************************************************************************************************************

from selenium_driverless import webdriver
from selenium_driverless.types.by import By
import asyncio


async def main():
    options = webdriver.ChromeOptions()
    async with webdriver.Chrome(options=options) as driver:
        await driver.get('https://www.selenium.dev/')
        await driver.sleep(0.5)
        await driver.wait_for_cdp("Page.domContentEventFired", timeout=15)
        
        # wait 10s for elem to exist
        elem = await driver.find_element(By.XPATH, '/html/body/div[2]/div/main/p[2]/a', timeout=10)
        await elem.click(move_to=True)

        alert = await driver.switch_to.alert
        print(alert.text)
        await alert.accept()

        print(await driver.title)


asyncio.run(main())