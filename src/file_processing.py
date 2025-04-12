import os

class FileHandler:
    def __init__(self, course_name):
        self.course_name = course_name
        self.base_path = os.path.join(os.getcwd(), "downloads", course_name)
        self.create_folder()

    def create_folder(self):
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        
 