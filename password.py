
class Password:

    special_characters_count = 0
    lower_case = 0
    upper_case_count= 0 
    digits_count = 0
    password_length = 0

    special_characters = "@#$%&*/\?"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case_count= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits_count = "1234567890"

    def __init__(self, password):
        self.password = password