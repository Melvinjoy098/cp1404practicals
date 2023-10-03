
def main():
    MENU = """(G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
        elif choice == "P":
            result = generate_result(score)
            print(result)
        elif choice == "S":
            print_asterisks(score)

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def generate_result(score):
    """Return the result according to the score"""
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        elif score < 50:
            return "Bad"

def print_asterisks(count):
    """prints the astricks to the length of the password."""
    print('*' * int(count))

main()