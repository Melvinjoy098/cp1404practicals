"""
Word Occurrences Counter
Estimate: 35minutes
Actual: 50 minutes
"""


def extract_name(email):
    parts = email.split('@')
    if len(parts) == 2:
        name = parts[0].replace('.', ' ').title()
        return name
    else:
        return None


user_data = {}

while True:
    email = input("Email: ")
    if email == "":
        break

    name = extract_name(email)
    if name is not None:
        print(f"Is your name {name}? (Y/n)")
        confirm = input()
        if confirm == "" or confirm.lower() == "y":
            user_data[email] = name
        else:
            print("Please enter your name:")
            user_name = input()
            user_data[email] = user_name.title()

for email, name in user_data.items():
    print(f"{name} ({email})")
