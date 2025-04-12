# Description: This file contains the Canvas class which is used to access the Canvas website and handle scraping of data.
# The Canvas class has methods to get and set the username, password, and Canvas URL.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time
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
        self.driver.implicitly_wait(3)  # Apply implicit wait globally
        self.wait = WebDriverWait(self.driver, 10)

    def open_canvas(self):
        self.driver.get(self.canvas_url)
        print("Opened Canvas")

    def initial_login(self):
        username_input = self.wait.until(EC.presence_of_element_located((By.ID, "emailAuthCheck")))
        next_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "uon-emailAuthCheckAction")))
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
        authenticator_input = self.driver.find_element(By.ID, "input69") # The ID of the authenticator input field
        authenticator_input.send_keys(authenticator_code) # Send the authenticator code to the authenticator input field
        signin_button = self.driver.find_element(By.CSS_SELECTOR, "input.button.button-primary[value='Verify']") # The CSS selector of the sign in button
        signin_button.click()

    def handle_popups(self):
        try:
            close_button = self.driver.find_element(By.ID, "btnClosePrompt") # The ID of the close button
            close_button.click() # Click the close button
            print("Closed popup")
        except:
            print("No popup found")

    def open_courselist(self):
        courses_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#global_nav_courses_link")))
        courses_link.click()
        time.sleep(3)
        all_courses_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.css-treuhc-view-link")))
        all_courses_link.click()
        print("Opening courses list")

    def get_past_enrollments(self):
        past_courses = {}
        table = self.driver.find_element(By.ID, "past_enrollments_table")
        # Locate all rows in the table
        rows = table.find_elements(By.CSS_SELECTOR, 'tr.course-list-table-row')

        # Loop through each row and get the course title
        for index, row in enumerate(rows, start=1):
            course_title = row.find_element(By.CSS_SELECTOR, 'span.name').text
            past_courses[index] = course_title  # Assign number as key 

        if not past_courses:
            print("No past enrollments found.")
            return past_courses  # Return empty if no courses

        # Display past enrollments
        print("\nYour Past Enrollments:")
        for key, value in past_courses.items():
            print(f"{key}: {value}")

        # Allow user to select courses to remove
        selected_courses = input("\nEnter the numbers of the courses you want to remove, separated by commas: ")
        courses_selection = selected_courses.split(",")

        for course in courses_selection:
            try:
                course_number = int(course.strip())  # Convert input to integer
                if course_number in past_courses:
                    past_courses.pop(course_number)
                    print(f"Removed course {course_number}")
                else:
                    print(f"Course {course_number} not found.")
            except ValueError:
                print(f"Invalid input: {course}. Please enter numbers only.")

        # Display updated course list
        print("\nUpdated Course List:")
        for key, value in past_courses.items():
            print(f"{key}: {value}")

        return past_courses  # Return updated list
        
    # def get_all_course_files(self, selected_courses):
    #     for course in selected_courses:
    #         course_link = self.driver.find_element(By.LINK_TEXT, course)
    #         course_link.click()
    #         time.sleep(3)




    # def close_browser(self):
    #     self.driver.quit()