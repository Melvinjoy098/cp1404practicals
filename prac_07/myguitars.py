
from guitar import Guitar

def main():
    guitars = load_guitars()
    display_guitars(guitars)
    
    add_new_guitars(guitars)
    save_guitars(guitars)

def load_guitars():
    guitars = []
    with open("guitars.csv", "r") as file:
        for line in file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

def add_new_guitars(guitars):
    print("\nAdd a new guitar:")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.\n")

def save_guitars(guitars):
    guitars.sort()
    with open("guitars.csv", "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

if __name__ == "__main__":
    main()
