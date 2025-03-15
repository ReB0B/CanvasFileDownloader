# Description: This file is the main file that will be run to start the program.
from src.canvas_scraper import Canvas

username = input("Enter username: ") #username is generally your student ID
password = input("Enter password: ")

canvas_url = input("Enter Canvas URL: ") # Canvas URL is the URL of your university's canvas page

canvas = Canvas(username, password, canvas_url)