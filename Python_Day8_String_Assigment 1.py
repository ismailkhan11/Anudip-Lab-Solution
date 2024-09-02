# 1. Write a Python program to count the occurrences of each word in a given sentence 

# string = “To change the overall look of your document. To change the look available in the gallery”

import string

# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Normalize the sentence by converting to lowercase
sentence = sentence.lower()

# Remove punctuation from the sentence
translator = str.maketrans('', '', string.punctuation)
sentence = sentence.translate(translator)

# Split the sentence into words
words = sentence.split()

# Dictionary to store word counts
word_count = {}

# Count occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")


# Output:

# Word occurrences:
# to: 2
# change: 2
# the: 3
# overall: 1
# look: 2
# of: 1
# your: 1
# document: 1
# available: 1
# in: 1
# gallery: 1
