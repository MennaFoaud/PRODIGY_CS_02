password = input("Please enter a password that doesn't exceed 8 characters, including uppercase letters, lowercase letters, numbers, and symbols: ")
char_arr = list(password)

def password_checker(password):
    if len(password) != 8:
        return "Password should be exactly 8 characters long."
    
    if not any(char.isalpha() for char in char_arr):
        return "Please include letters in the password."
    
    if not any(char.isupper() for char in char_arr):
        return "Please add at least one uppercase letter."
    
    if not any(char.islower() for char in char_arr):
        return "Please add at least one lowercase letter."
    
    if not any(char.isdigit() for char in char_arr):
        return "Please add at least one digit."
    
    if not any(char in "!@#$%^&*()-_+=<>?/{}~" for char in char_arr):
        return "Please add at least one special character (e.g., !, @, #, $, etc.)."

    return "Password is strong!!"

result = password_checker(password)
print(result)

while result != "Password is strong!!":
    password = input("Please try again. Ensure it meets all the criteria: ")
    char_arr = list(password)
    result = password_checker(password)
    print(result)
