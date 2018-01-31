# https://www.codewars.com/kata/playing-with-digits
# Some numbers have funny properties. For example:
#   89 --> 8¹ + 9² = 89 * 1
#   695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
#   46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, 
# such as the sum of the digits of n taken to the successive powers of p is equal to k * n. In other words:
#   Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# If it is the case we will return k, if not return -1.
# Note: n, p will always be given as strictly positive integers.

# 1st solution
def dig_pow(n, p):
    sum = 0
    for idx, pow in enumerate(range(p, p+len(str(n)))):
        sum += int(str(n)[idx])**pow
    k = sum/n
    if k % 1 == 0:
        return k
    return -1

# 2nd, better solution
def dig_pow(n, p):
    sum = 0
    for i, d in enumerate(str(n)):
        sum += pow(int(d), p+i)
    return sum/n if sum%n == 0 else -1