
import random as re

class Password:
    '''
    Password class that models the user password
    
    Parameters:
    ----------

    password: str
    password_length: str

    Attributes:
    ----------

    The following attributes store the count of characters in password
    special_characters_count 
    lower_case_count
    upper_case_count
    digits_count
    valid: bool
    
    The following attributes refer to characters that that password should contain
    special_characters: str
    lower_case: str
    upper_case: str
    digits: str

    
 
    Methods:
    -------
    generate password()
        generates password

    validate_password()
        checks that password is valid

    '''

    special_characters_count = 0
    lower_case_count= 0
    upper_case_count= 0 
    digits_count = 0
    valid = False
    
    special_characters = "@#$%&*/\?"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234567890"


    def __init__(self, password, password_length=8):
        self.password = password
        self.password_length = int(password_length)
        

    def generate_password(self):

        '''
        Generates password and validates password by calling validate_password method
        '''


        while True:
            use_for_password = self.special_characters + self.lower_case + self.upper_case + self.digits

            self.password = "".join(re.sample(use_for_password, self.password_length))

            if self.validate_password() == True:
                return self.password

    
    def validate_password(self):
        '''
        validates password 
        '''
        
        for character in self.password:
            if character in self.special_characters:
                self.special_characters_count += 1
            
            if character in self.lower_case:
                self.lower_case_count += 1

            if character in self.upper_case:
                self.upper_case_count += 1
            
            if character in self.digits:
                self.digits_count += 1
            
        if self.special_characters_count > 0  and self.upper_case_count > 0 and self.lower_case_count > 0 and self.digits_count > 0:
            return True
