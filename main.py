from password import Password
import random 

def main():
    message = "Press 1 to auto-genetate a strong password\n"
    message += "Press 2 to enter a password you will like to validate its strength\n"

    user_input = input(message)

    if user_input == "1":

        password_length = input("How many characters: \n")

        password = Password(user_input, password_length)

        generated_password = password.generate_password()
    
        print(f"Your generated password is {generated_password}")

    # if user_input == "2":
    #     password = Password(user_input)







if __name__ == "__main__":
    main()