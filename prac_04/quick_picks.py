import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def main():
    num_quick_picks = int(input("How many quick picks? "))

    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join("{:2}".format(num) for num in quick_pick))

def generate_quick_pick():
    numbers = range(MIN_NUMBER, MAX_NUMBER + 1)
    quick_pick = random.sample(numbers, NUMBERS_PER_LINE)
    quick_pick.sort()
    return quick_pick

main()
