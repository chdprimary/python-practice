squares = []
for val in range(1,11):
    squares.append(val**2)
print("For loop squares: " + str(squares))

lc_squares = [val**2 for val in range(1,11)]
print("List comp squares: " + str(lc_squares))