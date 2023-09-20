from app import app

class ErrorHandling:
    def __init__(self):
        self.is_fatal = False
        self.is_error = False
        self.is_success = False
    
    def exit_program(self,message):
        if self.is_fatal:
            print("Program failed with fatal error !!")
        elif self.is_error:
            print("Program end with an error !!")
        elif self.is_success:
            print("Program Ended Successfully !!")
    
    def set_fatal(self):
        self.is_fatal= True
    
    def set_error(self):
        self.is_error= True
    
    def set_success(self):
        self.is_success= True

