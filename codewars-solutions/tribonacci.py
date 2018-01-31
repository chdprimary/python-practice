# https://www.codewars.com/kata/tribonacci-sequence/python
# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. 
# You need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

def tribonacci(signature, n):
    ret = signature
    if len(ret) >= n:
        return ret[:n]
    while len(ret) < n:
        ret.append(sum(ret[-3:]))
    return ret