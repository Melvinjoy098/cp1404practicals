numbers = [3, 1, 4, 1, 5, 9, 2]
'''numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = [3, 1, 4, 1, 5, 9]
numbers[3:4] = 1
5 in numbers = 9
7 in numbers =  IndexError: list index out of range
"3" in numbers = TypeError: list indices must be integers or slices, not str
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]'''

'''Change the first element of numbers to "ten" (the string, not the number 10)'''
numbers[0] = "ten"
print (numbers)
'''Change the last element of numbers to 1'''
numbers[-1] = 1
print (numbers)
'''Print all the elements from numbers except the first two (slice)'''
numbers[2:]
print (numbers)
'''Print whether 9 is an element of numbers'''
if 9 in numbers:
    print(" 9 is an element of the number")
else:
    print("9 is not an element of the numbers")