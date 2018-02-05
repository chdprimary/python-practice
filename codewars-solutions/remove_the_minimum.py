# https://www.codewars.com/kata/563cf89eb4747c5fb100001b

def remove_smallest(numbers):
    if not numbers:
        return []
    copy = numbers[:]
    copy.remove(min(copy))
    return copy