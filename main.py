from password import Password
import random 

def main():
    message = "Press 1 to auto-genetate a strong password\n"
    message += "Press 2 to enter a password you will like to validate its strength\n"

    char_message = "How many characters (minimum 8 charaters): \n"
    repeat = True

    user_input = input(message)

    if user_input == "1":

        while True:

            password_length = input(char_message)

            if int(password_length) >= 8:

                password = Password(user_input, password_length)

                generated_password = password.generate_password()

                print(f"Your generated password is {generated_password}")

                break

            else:
                print("Your password needs to be atleast 8 characters") 



    if user_input == "2":

        while repeat:
            user_input = input("Enter your password below: \n")

            if len(user_input) >= 8:
                password = Password(user_input)

                valid = password.validate_password()

                if valid == True:
                    print("Your password is strong!")
                
                else:
                    print("Weak password! try a different combination for your password")

            else:
                print("Your password needs to be atleast 8 characters")
            

            repeat_message  = "Enter yes to try a new password or quit to end\n"

            while repeat: 

                repeat_message = input(repeat_message)

                if repeat_message == "yes":
                    break

                elif repeat_message == "quit":
                    repeat = False
                
                else:
                    print("Wrong input!")


if __name__ == "__main__":
    main()