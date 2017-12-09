# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

def get_middle(word):
    wordLen = len(word)
    middle = ''
    
    if (wordLen % 2 == 0):
        middle = word[wordLen//2-1] + word[wordLen//2]
    else:
        middle = word[wordLen//2]
    
    return middle