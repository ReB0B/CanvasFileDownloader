from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time
import getpass

username = input("Enter username: ") #username is generally your student ID
password = getpass.getpass('Enter Password:')

canvas_url = input("Enter Canvas URL: ") # Canvas URL is the URL of your university's canvas page

# Set up Chrome WebDriver
chromedriver_location = os.getenv("CHROMEDRIVER_LOCATION")  # Set the location of the chromedriver
service = Service(chromedriver_location) # Set the service to the chromedriver location
chrome_options = Options() # Set the chrome options
# chrome_options.add_argument("--headless") # Uncomment to run the browser in headless mode
driver = webdriver.Chrome(service=service, options=chrome_options) # Set the driver to the chromedriver service and options
driver.implicitly_wait(5)  # Apply implicit wait globally

driver.get(canvas_url)
print("Opened Canvas")

username_input = driver.find_element(By.ID, "emailAuthCheck")
next_button = driver.find_element(By.CLASS_NAME, "uon-emailAuthCheckAction")
username_input.send_keys(username)
next_button.click()

time.sleep(5)
username_input = driver.find_element(By.ID, "input28")
password_input = driver.find_element(By.ID, "input36")
signin_button = driver.find_element(By.CSS_SELECTOR, "input.button.button-primary[value='Sign in']")
username_input.send_keys(username)
password_input.send_keys(password)
signin_button.click()

authenticator_code = input("Enter the authenticator code: ")
authenticator_input = driver.find_element(By.ID, "input69")
authenticator_input.send_keys(authenticator_code)
signin_button = driver.find_element(By.CSS_SELECTOR, "input.button.button-primary[value='Verify']")
signin_button.click()

time.sleep(10)
print("Logged in")
driver.quit()