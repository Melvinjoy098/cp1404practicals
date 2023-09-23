
while True:
    password = input("Please enter your password: ")
    if len(password) < 8:
        print(f"Error: The password must be at least 8 characters long.")
        continue
    break

print('*' * len(password))