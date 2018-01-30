# Given parameters:
# p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)
# the function nb_year should return n number of entire years needed to get a population greater or equal to p.
# aug is an integer, percent a positive or null number, p0 and p are positive integers (> 0)

def nb_year(p0, percent, aug, p):
    curr_pop = p0
    years = 0
    while curr_pop < p:
        curr_pop += curr_pop*percent*.01 + aug
        years += 1
    return years