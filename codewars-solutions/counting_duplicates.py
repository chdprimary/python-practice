# https://www.codewars.com/kata/counting-duplicates/solutions/python
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    text = text.lower()    
    num_duplicates = sum([1 for c in set(text) if text.count(c) > 1])
    return num_duplicates