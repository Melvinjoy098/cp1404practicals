"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans: This error occurs when the numerator and denominator values given is not a valid integer.
2. When will a ZeroDivisionError occur?
Ans: This error occurs when denominator value given as zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator(not zero): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
