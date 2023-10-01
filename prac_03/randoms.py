"""What did you see on line 1?
Print random integer from 5 to 20 inclusive
What was the smallest number you could have seen, what was the largest?
The smallest number is 5 and the largest number is 20"""

"""What did you see on line 2?
print random integer from 3 to 10 (exclusive) with incremental value of 2
What was the smallest number you could have seen, what was the largest?
Smallest number is 3 and largest number is 9
Could line 2 have produced a 4?
Not possible. The possible values are 3,5,7 and 9"""

"""What did you see on line 3?
prints random floating numbers between 2.5 and 5.5
What was the smallest number you could have seen, what was the largest?
smallest number is 2.5 and largest number is 5.5"""

"""Write code, not a comment, to produce a random number between 1 and 100 inclusive"""
import random
random_number = random.randint(1, 100)
print(random_number)
