# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    for item in seq:
        indices = [i for i, v in enumerate(seq) if seq[i] == item]
        if len(indices) % 2 != 0:
            return seq[indices[0]]