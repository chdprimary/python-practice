# https://www.codewars.com/kata/558f9f51e85b46e9fa000025/solutions/python/me/best_practice
# Description:
# Find the difference between the sum of the squares of the first n natural numbers (1 <= n <= 100) and the square of their sum. 

def difference_of_squares(x):
    sum_of_squares = sum([n**2 for n in range (1,x+1)])
    square_of_sum = sum(range(1,x+1))**2
    return abs(square_of_sum - sum_of_squares)