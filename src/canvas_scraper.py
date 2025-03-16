# Description: This file contains the Canvas class which is used to access the Canvas website and handle scraping of data.
# The Canvas class has methods to get and set the username, password, and Canvas URL.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

class Canvas:
    def __init__(self, username, password, canvas_url):
        # Load environment variables
        load_dotenv

        # initialize variables
        self.username = username
        self.password = password
        self.canvas_url = canvas_url

        # Set up Chrome WebDriver
        self.chromedriver_location = os.getenv("CHROMEDRIVER_LOCATION")  # Set the location of the chromedriver
        service = Service(self.chromedriver_location) # Set the service to the chromedriver location
        chrome_options = Options() # Set the chrome options
        # chrome_options.add_argument("--headless") # Uncomment to run the browser in headless mode
        self.driver = webdriver.Chrome(service=service, options=chrome_options) # Set the driver to the chromedriver service and options

        self.driver.implicitly_wait(5)  # Apply implicit wait globally

    def open_canvas(self):
        self.driver.get(self.canvas_url)
        print("Opened Canvas")

    def initial_login(self):
        username_input = self.driver.find_element(By.ID, "emailAuthCheck")
        next_button = self.driver.find_element(By.CLASS_NAME, "uon-emailAuthCheckAction")
        username_input.send_keys(self.username)
        next_button.click()

    def okta_login(self):
        username_input = self.driver.find_element(By.ID, "input28") # The ID of the username input field
        password_input = self.driver.find_element(By.ID, "input36") # The ID of the password input field
        signin_button = self.driver.find_element(By.CSS_SELECTOR, "input.button.button-primary[value='Sign in']") # The CSS selector of the sign in button
        username_input.send_keys(self.username) # Send the username to the username input field
        password_input.send_keys(self.password) # Send the password to the password input field
        signin_button.click()

    def check_authenticator_required(self):
        try:
            authenticator_input = self.driver.find_element(By.ID, "input69")
            return True
        except:
            return False

    def enter_authenticator_code(self, authenticator_code):
        authenticator_input = self.driver.find_element(By.ID, "input69")
        authenticator_input.send_keys(authenticator_code)
        signin_button = self.driver.find_element(By.CSS_SELECTOR, "input.button.button-primary[value='Verify']")
        signin_button.click()

    def close_browser(self):
        self.driver.quit()


    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_canvas_url(self):
        return self.canvas_url

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_canvas_url(self, canvas_url):
        self.canvas_url = canvas_url