
import random as re

class Password:

    special_characters_count = 0
    lower_case = 0
    upper_case_count= 0 
    digits_count = 0


    special_characters = "@#$%&*/\?"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234567890"


    def __init__(self, password, password_length=8):
        self.password = password
        self.password_length = int(password_length)
        

    def generate_password(self):

        use_for_password = self.special_characters + self.lower_case + self.upper_case + self.digits

        generated_password = "".join(re.sample(use_for_password, self.password_length))
    
        return generated_password