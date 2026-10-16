#1)
password = "1234"

for attempt in range(3):
    user_input = input("Enter the password: ")
    count = 3 - attempt - 1
    if user_input == password:
        print("Authentication successful.")
        break
    else:
        print("Incorrect password. You have", count, "attempts remaining.")

else:
    print("Authentication failed. You have exceeded the maximum number of attempts.")

#2)
def authenticate():
    password = "1234"
    max_attempts = 3

    for attempt in range(max_attempts):
        user_input = input("Enter the password: ")
        count = max_attempts - attempt - 1
        if user_input == password:
            print("Authentication successful.")
            break
        else:
            print("Incorrect password. You have", count, "attempts remaining.")
    else:
        print("Authentication failed. You have exceeded the maximum number of attempts.")

authenticate()

#3)
def authenticate(password, max_attempts):
    for attempt in range(max_attempts):
        user_input = input("Enter the password: ")
        count = max_attempts - attempt - 1
        if user_input == password:
            print("Authentication successful.")
            break
        else:
            print("Incorrect password. You have", count, "attempts remaining.")
    else:
        print("Authentication failed. You have exceeded the maximum number of attempts.")   

authenticate("1234", 3)

#4)
def authenticate(password, max_attempts):
    for attempt in range(max_attempts):
        user_input = input("Enter the password: ")
        count = max_attempts - attempt - 1
        if user_input == password:
            print("Authentication successful.")
            return True
        else:
            print("Incorrect password. You have", count, "attempts remaining.")
    else:
        print("Authentication failed. You have exceeded the maximum number of attempts.")
        return False

authenticate("1234", 3)