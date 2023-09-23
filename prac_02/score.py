"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
def main():

    score = float(input("Enter score: "))
    result = generate_result(score)
    print(result)


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


main()

random_score = random.randint(10, 100)
result = generate_result(random_score)
print(random_score, result)