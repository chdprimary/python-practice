# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd
# integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    parities = [n % 2 for n in integers]
    return integers[parities.index(0)] if parities.count(0) == 1 else integers[parities.index(1)]