from password import Password
import random 

def main():
    message = "Press 1 to auto-genetate a strong password\n"
    message += "Press 2 to enter a password you will like to validate its strength\n"

    user_input = input(message)

    if user_input == "1":
        password = Password(user_input)

        use_for_password = password.special_characters + password.lower_case + password.upper_case_count + password.digits_count
        password.password_length = 8

        generated_password = "".join(random.sample(use_for_password, password.password_length))
    
        print(f"Your generated password is {generated_password}")

    

if __name__ == "__main__":
    main()