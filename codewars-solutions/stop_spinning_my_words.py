https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/python
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed. 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# 1st solution
def spin_words(sentence):
    translation = []
    for word in sentence.strip().split():
        translation.append(word[::-1]) if len(word) >= 5 else translation.append(word)
    return ' '.join(translation)

# my 2nd solution (more concise)
def spin_words(sentence):
    return ' '.join(w if len(w) < 5 else w[::-1] for w in sentence.split())