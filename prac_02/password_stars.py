def main():

    while True:
        password = get_password()
        if len(password) < 8:
            print(f"Error: The password must be at least 8 characters long.")
            continue
        break


    print_asterisks(len(password))


def print_asterisks(count):
    """prints the astricks to the length of the password."""
    print('*' * count)


def get_password():
    """gets the password from the user"""
    password = input("Please enter your password: ")
    return password


main()
