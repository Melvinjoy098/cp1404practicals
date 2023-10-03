#1. writes the user given name to the file

user_name = input("Enter your name: ")
name_file = open('name.txt', 'w')
print(f"{user_name}", file=name_file)
name_file.close()

#2.opens "name.txt" and reads the name then prints

name_file = open('name.txt', 'r')
name = name_file.read()
print(f"Your name is {name}")

#3. opens "numbers.txt", reads only the first two numbers and adds them together then prints the result

numbers_file = open('numbers.txt', 'r')
num1 = int(numbers_file.readline())
num2 = int(numbers_file.readline())
total = num1 + num2
print(f"The sum of the first two numbers is: {total}")

#4.prints the total for all lines in numbers.txt

numbers_file = open('numbers.txt', 'r')
Lines = numbers_file.readlines()
total = 0
for line in Lines:
  total = total+int(line)
print(f"The total of all the numbers is: {total}")