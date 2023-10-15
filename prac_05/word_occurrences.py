"""
Word Occurrences Counter
Estimate: 30 minutes
Actual: 38 minutes
"""

user_input = input("Enter a string: ")

words = user_input.split()

word_counts = {}

for word in words:
    word = word.lower()

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

max_word_length = max(len(word) for word in word_counts.keys())

for word, count in sorted(word_counts.items()):
    print(f"{word:{max_word_length}} : {count}")
