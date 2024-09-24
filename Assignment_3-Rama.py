# ASSIGNMENT 3 - Wednesday, September 18th
# 1. Create a program that removes all the vowels from user input and produces the outcome back to the user.

user_input = input("Enter a word or a phrase: ")
vowels = ['a','e','i','o','u']
user_output = ''
for thing in user_input:
    if thing in vowels:
        user_output = user_output + ' '
    else:
        user_output = user_output + thing
print(f"Here is your word/phrase without any vowels: {user_output}")

# 2. Create a password validator program that only accepts a password that fits a set of requirements.
#     These requirements are up to you. Make sure the user knows the requirements before they try a password.
#     Do not allow the program to end until the password meets all your requirements.
#     Try to use a dictionary to solve this, if you can manage it.

import string
digits = ['0','1','2','3','4','5','6','7','8','9']
special_chars = ['!','@','$','%','&','*']
upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
def password_validator(user_input):
    i = 0
    j = 0
    k = 0
    l = 0
    if len(user_input) > 8:
        for char in user_input:
            if char in digits:
                i = i + 1
            elif char in special_chars:
                j = j + 1
            elif char in upper_case:
                k = k + 1
            elif char in lower_case:
                l = l + 1
    else:
        print("Your password should atleast be 8 characters")

    print(f"{i},{j},{k},{l}")

    if i>=1 and j>=1 and k>=1 and l>=1:
       return(4)
    else:
        return(0)

try_1 = 0
while try_1 == 0:
    user_input = input("Enter your password. The requirements of the password are a minimum of 8 characters, minimum 1 upper case alphabet, minimum 1 lower case alphaber, minimum 1 special character (! @ $ % & *): ")
    validator = password_validator(user_input)
    print(validator)
    if validator == 4:
        print("Success.Your password is valid!")
        try_1 = 1
    elif validator == 0:
        print("The password you entered is invalid and does not meet the minimum requirements. Please try again.")
        try_1 = 0
