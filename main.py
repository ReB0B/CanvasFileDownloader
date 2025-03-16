# Description: This file is the main file that will be run to start the program.
from src.canvas_scraper import Canvas
import getpass

username = input("Enter username: ") #username is generally your student ID
password = getpass.getpass('Enter Password:')

canvas_url = input("Enter Canvas URL: ") # Canvas URL is the URL of your university's canvas page

canvas = Canvas(username, password, canvas_url)
canvas.open_canvas()
canvas.initial_login()
canvas.okta_login()

# Check if an authenticator code is required
if canvas.check_authenticator_required():
    authenticator_code = input("Enter the authenticator code: ")
    canvas.enter_authenticator_code(authenticator_code)

canvas.close_browser()
print("Logged in")