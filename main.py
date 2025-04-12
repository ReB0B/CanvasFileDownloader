# Description: This file is the main file that will be run to start the program.
from src.canvas_scraper import Canvas
import getpass
import time
import os
from dotenv import load_dotenv

load_dotenv()

def main():    
    # username = input("Enter username: ") #username is generally your student ID
    # password = getpass.getpass('Enter Password:')
    # canvas_url = input("Enter Canvas URL: ") # Canvas URL is the URL of your university's canvas page

    # Testing Purpose
    # Uncomment for testing
    username = os.getenv("USERNAME")
    password =os.getenv("PASSWORD")
    canvas_url = "https://canvas.newcastle.edu.au/"

    canvas = Canvas(username, password, canvas_url)
    canvas.open_canvas()
    canvas.initial_login()
    canvas.okta_login()

    # Check if an authenticator code is required
    if canvas.check_authenticator_required():
        authenticator_code = input("Enter the authenticator code: ")
        canvas.enter_authenticator_code(authenticator_code)

    canvas.handle_popups()
    
    time.sleep(3)
    canvas.open_courselist()
    time.sleep(3)
    selected_courses = canvas.get_past_enrollments()


if __name__ == "__main__":
    main()
    # canvas.close_browser()
    print("Logged in")